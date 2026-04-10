using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.UIElements;
using UnityEngine.SceneManagement;

public class PlayerController : MonoBehaviour
{
    private float elapsedTime = 0f;
    private float score = 0f;
    public float scoreMultiplier = 5f;
    public float thrustForce = 1f;
    public float maxSpeed = 5f;
    public GameObject boosterFlame;
    Rigidbody2D rb;
    public UIDocument uiDocument;
    private Label scoreText;
    private Button restartButton;
    public GameObject explosionEffect; 
    public GameObject projectilePrefab;
    public Transform firePoint;
    public float fireCooldown = 0.25f;
    private float lastFireTime = 0f;
    private int bonusScore = 0;
    public int asteroidsDestroyed = 0;
    public static bool IsPlayerAlive = true; 

    
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        scoreText = uiDocument.rootVisualElement.Q<Label>("ScoreLabel");
        restartButton = uiDocument.rootVisualElement.Q<Button>("RestartButton");
        restartButton.style.display = DisplayStyle.None;
        restartButton.clicked += ReloadScene;
    }
    void Update()
    {
        UpdateScore();
        MovePlayer();

    if (Keyboard.current.spaceKey.isPressed && Time.time > lastFireTime + fireCooldown)
    {
        Shoot();
        lastFireTime = Time.time;
    }

    }

    void UpdateScore()
    {
        elapsedTime += Time.deltaTime;
        score = Mathf.FloorToInt(elapsedTime * scoreMultiplier) + bonusScore;
        scoreText.text = "Score: " + score;
    }
    public void AddScore(int amount)
    {
        bonusScore += amount;
        asteroidsDestroyed++;
    }

    void MovePlayer()
    {
        
        if (Mouse.current.leftButton.isPressed)
        {
            // Calculate mouse direction
            Vector3 mousePos = Camera.main.ScreenToWorldPoint(Mouse.current.position.value);
            Vector2 direction = (mousePos - transform.position).normalized;

            // Move player in direction of mouse
            transform.up = direction;
            rb.AddForce(direction * thrustForce);
        }

        // Velocity 
        if (rb.linearVelocity.magnitude > maxSpeed)
        {
        rb.linearVelocity = rb.linearVelocity.normalized * maxSpeed;
        }

        // Animation for booster
        if (Mouse.current.leftButton.wasPressedThisFrame)
        {
            boosterFlame.SetActive(true);
        }

        else if (Mouse.current.leftButton.wasReleasedThisFrame)
        {
            boosterFlame.SetActive(false);
        }
    }

    void OnCollisionEnter2D(Collision2D collision)
    {
        Instantiate(explosionEffect, transform.position, transform.rotation);

        IsPlayerAlive = false;

        Destroy(gameObject);

        restartButton.style.display = UnityEngine.UIElements.DisplayStyle.Flex;
    }
    void Shoot()
    {
        Vector2 direction = transform.up;

        GameObject projectile = Instantiate(projectilePrefab, firePoint.position, transform.rotation);

        projectile.GetComponent<Projectile>().Fire(direction);
        rb.AddForce(-transform.up * 0.2f, ForceMode2D.Impulse);
    }

    void ReloadScene()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }

}
