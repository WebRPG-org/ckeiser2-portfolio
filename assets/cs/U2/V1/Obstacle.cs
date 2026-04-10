using UnityEngine;

public class Obstacle : MonoBehaviour
{
    public enum AsteroidType { Default, Ice, Fire, Blackhole, White }
    public AsteroidType asteroidType;

    [Header("Size & Speed")]
    public float minSize = 0.5f;
    public float maxSize = 3.0f;
    public float minSpeed = 50f;
    public float maxSpeed = 150f;
    public float maxSpinSpeed = 10f;

    [Header("Effects")]
    public GameObject bounceEffectPrefab;
    public GameObject iceTrailPrefab;
    public GameObject fireTrailPrefab;
    public GameObject blackTrailPrefab;
    public GameObject whiteTrailPrefab;

    Rigidbody2D rb;
    private Transform playerTransform;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        playerTransform = FindObjectOfType<PlayerController>()?.transform;

        // Random size
        float randomSize = Random.Range(minSize, maxSize);
        transform.localScale = new Vector3(randomSize, randomSize, 1);

        // Base speed adjusted for type
        float baseSpeed = Random.Range(minSpeed, maxSpeed) / randomSize;

        switch (asteroidType)
        {
            case AsteroidType.Ice:
                baseSpeed *= 1.3f; // faster than default
                rb.linearDamping = 0.2f;    // slippery
                rb.angularDamping = 0.05f;
                if (iceTrailPrefab)
                {
                    GameObject trail = Instantiate(iceTrailPrefab, transform.position, Quaternion.identity, transform);
                }
                break;

            case AsteroidType.Blackhole:
                baseSpeed *= 1f; 
                if (blackTrailPrefab)
                {
                    GameObject trail = Instantiate(blackTrailPrefab, transform.position, Quaternion.identity, transform);
                }
                break;

            case AsteroidType.White:
                baseSpeed *= 1; 
                if (whiteTrailPrefab)
                {
                    GameObject trail = Instantiate(whiteTrailPrefab, transform.position, Quaternion.identity, transform);
                }
                break;

            case AsteroidType.Fire:
                baseSpeed *= 1.8f; // very fast
                rb.linearDamping = 0.5f;
                rb.angularDamping = 0.1f;
                if (fireTrailPrefab)
                {
                    GameObject trail = Instantiate(fireTrailPrefab, transform.position, Quaternion.identity, transform);
                }

                // Slight homing toward player
                if (playerTransform != null)
                {
                    Vector2 directionToPlayer = (playerTransform.position - transform.position).normalized;
                    rb.AddForce(directionToPlayer * 20f);
                }
                break;

            case AsteroidType.Default:
                rb.linearDamping = 0.3f;
                rb.angularDamping = 0.1f;
                break;
        }

        // Random movement and spin
        Vector2 randomDirection = Random.insideUnitCircle.normalized;
        rb.AddForce(randomDirection * baseSpeed);
        float randomTorque = Random.Range(-maxSpinSpeed, maxSpinSpeed);
        rb.AddTorque(randomTorque);
    }

    void OnCollisionEnter2D(Collision2D collision)
    {
        // Collision with projectile
        if (collision.gameObject.CompareTag("Projectile"))
        {
            // Update score
            PlayerController player = FindObjectOfType<PlayerController>();
            if (player != null)
                player.AddScore(50);

            //  explosion effect
            if (bounceEffectPrefab)
            {
                Vector2 contactPoint = collision.GetContact(0).point;
                GameObject effect = Instantiate(bounceEffectPrefab, contactPoint, Quaternion.identity);
                Destroy(effect, 1f);
            }

            Destroy(collision.gameObject);
            Destroy(gameObject);
            return;
        }

        // Bounce effect for other collisions
        if (bounceEffectPrefab)
        {
            Vector2 contactPoint = collision.GetContact(0).point;
            GameObject effect = Instantiate(bounceEffectPrefab, contactPoint, Quaternion.identity);
            Destroy(effect, 1f);
        }
    }
}