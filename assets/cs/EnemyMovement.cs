using UnityEngine;
using UnityEngine.AI;

public class EnemyMovement : MonoBehaviour
{
    public Transform player;
    private NavMeshAgent navMeshAgent;
    private float loseSightTimer = 0f;
    [SerializeField] private float loseSightDelay = 2f;
    private bool isChasing = false;

    void Start()
    {
        navMeshAgent = GetComponent<NavMeshAgent>();
    }

    void Update()
    {
        if (isChasing && player != null)
        {
            navMeshAgent.SetDestination(player.position);
        }
        else
        {
            navMeshAgent.ResetPath();
        }
    }

    public void SetChasing(bool chasing)
    {
        isChasing = chasing;
    }
}