using UnityEngine;


[RequireComponent(typeof(MeshFilter))]
public class FieldOfView : MonoBehaviour
{
    [Header("Vision Settings")]
    [SerializeField] private LayerMask obstacleMask;
    [SerializeField] private float fov = 90f;
    [SerializeField] private float viewDistance = 15f;
    [SerializeField] private float eyeHeight = 1.5f;

    [Header("References")]
    [SerializeField] private Transform enemyTransform;

    [Header("Movement")]
    [SerializeField] private float moveSpeed = 5f;

    private EnemyMovement enemyMovement;

    private Mesh mesh;
    private float startingAngle;
    private Transform player;
    private bool canSeePlayer;

    private void Start()
    {
        enemyMovement = enemyTransform.GetComponent<EnemyMovement>();

        mesh = new Mesh();
        GetComponent<MeshFilter>().mesh = mesh;

        player = GameObject.FindGameObjectWithTag("Player").transform;
    }

    private void LateUpdate()
    {
        Vector3 origin = enemyTransform.position + Vector3.up * eyeHeight;
        canSeePlayer = false;

        SetAimDirection(enemyTransform.forward);

        int rayCount = 50;
        float angle = startingAngle;
        float angleIncrease = fov / rayCount;

        Vector3[] vertices = new Vector3[rayCount + 2];
        Vector2[] uv = new Vector2[vertices.Length];
        int[] triangles = new int[rayCount * 3];

        vertices[0] = transform.InverseTransformPoint(origin);

        int vertexIndex = 1;
        int triangleIndex = 0;

        for (int i = 0; i <= rayCount; i++)
        {
            Vector3 direction = GetVectorFromAngle(angle);

            Vector3 vertex = origin + direction * viewDistance;

            RaycastHit hit;

            if (Physics.Raycast(origin, direction, out hit, viewDistance, obstacleMask))
            {
                // Stop vision at first object hit
                vertex = hit.point;

                if (hit.collider.CompareTag("Player"))
                {
                    canSeePlayer = true;
                    enemyMovement.SetChasing(true);
                }
            }
            else
            {
                // Nothing hit → full vision range
                vertex = origin + direction * viewDistance;
            }

            vertices[vertexIndex] = transform.InverseTransformPoint(vertex);

            if (i > 0)
            {
                triangles[triangleIndex + 0] = 0;
                triangles[triangleIndex + 1] = vertexIndex - 1;
                triangles[triangleIndex + 2] = vertexIndex;

                triangleIndex += 3;
            }

            vertexIndex++;
            angle -= angleIncrease;
        }

        mesh.vertices = vertices;
        mesh.uv = uv;
        mesh.triangles = triangles;
        mesh.RecalculateBounds();

        DetectPlayer(origin);

        HandleMovement();
    }

    private void DetectPlayer(Vector3 origin)
    {
        float distanceToPlayer = Vector3.Distance(origin, player.position);

        if (distanceToPlayer <= viewDistance)
        {
            Vector3 dirToPlayer = (player.position - origin).normalized;
            float angleToPlayer = Vector3.Angle(enemyTransform.forward, dirToPlayer);

            if (angleToPlayer < fov / 2f)
            {
                if (!Physics.Raycast(origin, dirToPlayer, distanceToPlayer, obstacleMask))
                {
                    canSeePlayer = true;
                    enemyMovement.SetChasing(canSeePlayer);
                }
            }
        }
    }

    private void HandleMovement()
    {
        enemyMovement.SetChasing(canSeePlayer);
    }

    public static Vector3 GetVectorFromAngle(float angle)
    {
        float angleRad = (angle + 90f) * Mathf.Deg2Rad; // shift by +90 degrees
        return new Vector3(Mathf.Cos(angleRad), 0, Mathf.Sin(angleRad));
    }

    public void SetAimDirection(Vector3 aimDirection)
    {
        startingAngle = GetAngleFromVectorFloat(aimDirection) - fov / 2f;
    }

    public static float GetAngleFromVectorFloat(Vector3 dir)
    {
        dir = dir.normalized;
        float angle = Mathf.Atan2(dir.z, dir.x) * Mathf.Rad2Deg;
        if (angle < 0) angle += 360;
        return angle;
    }
}