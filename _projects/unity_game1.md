---
layout: page
title: In Progress! [Roll-a-Ball] 🎮
description: Unity demo excercise where you play as a ball collecting consumables, dodging enemies.
img: assets/img/v3.png
category: games 🎮


---
##### Work in progress using Unity Learn as an aid for this project.

** Developed in Unity 6.3 LTS **  

In Progress V0.00.01 demonstration of scripts below:

<iframe src="{{ site.baseurl }}/assets/video/ball_demo_v0.01.mp4"
        width="100%"
        height="600px"
        frameborder="0"
        style="border: 1px solid #ccc; border-radius: 8px;">
</iframe>

In Progress V0.00.02 expanding scripts and start of level design and finishing of gameplay loop:
<iframe src="{{ site.baseurl }}/assets/video/demov.2.mp4"
        width="100%"
        height="600px"
        frameborder="0"
        style="border: 1px solid #ccc; border-radius: 8px;">
</iframe>


In progress V0.00.03 Experimenting with level design for first level and LOS(Line of Sight) for initial enemies:
<iframe src="{{ site.baseurl }}/assets/video/demo3.mp4"
        width="100%"
        height="600px"
        frameborder="0"
        style="border: 1px solid #ccc; border-radius: 8px;">
</iframe>

In progress PlayerController.cs script handles player movement and physics and contact with enemies.
```cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;
using TMPro;


public class PlayerController : MonoBehaviour
{
    public float speed = 0;
    public TextMeshProUGUI countText;
    public GameObject winTextObject;
    private Rigidbody rb;
    private float movementX;
    private float movementY;
    // Count variable for UI to keep track of collectibles
    private int count;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
        count = 0;

        SetCountText();


        winTextObject.SetActive(false);

    }
    private void OnMove(InputValue movementValue)
    {
        Vector2 movementVector = movementValue.Get<Vector2>();

        movementX = movementVector.x; 
        movementY = movementVector.y; 
    }

    private void SetCountText()
    {
        countText.text = "Count: " + count.ToString();

        if(count >= 13)
        {
            winTextObject.SetActive(true);

            // Destroy enemy
            Destroy(GameObject.FindGameObjectWithTag("Enemy"));
        }
    }
    private void FixedUpdate()
    {
        Vector3 movement = new Vector3(movementX, 0.0f, movementY);
        rb.AddForce(movement * speed);

    }

    private void OnCollisionEnter(Collision collision)
    {
       if (collision.gameObject.CompareTag("Enemy"))
       {
           // Destroy the current object
           Destroy(gameObject); 
           
           // Update the winText to display "You Lose!"
           winTextObject.gameObject.SetActive(true);
           winTextObject.GetComponent<TextMeshProUGUI>().text = "You Lose!";
       }
    }

    // On contact will disable game objects with "PickUp" tag. Aka our collectibles in the demo.
    private void OnTriggerEnter(Collider other)
    {
        if(other.gameObject.CompareTag("PickUp"))
        {
            other.gameObject.SetActive(false);
            count = count + 1;

            SetCountText();
        }
        
    }
    
}

```

CameraController.cs
```cs

// Camera follows player movement, as player is a ball ensures camera does not rotate with the balls rotation.



using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{
    public GameObject player;
    private Vector3 offset;

    void Start()
    {
        offset = transform.position - player.transform.position;
    }

    void LateUpdate()
    {
        transform.position = player.transform.position + offset;
    }
}
```
Rotator.cs

```cs


// For the collectibles in the game, to give a visual *Pop* we have this simple rotating script.

using UnityEngine;
using System.Collections;
using System.Collections.Generic;


public class Rotator : MonoBehaviour
{

    // Every frame the object will be rotated on the x,y,z 
    void Update()
    {
        transform.Rotate(new Vector3(15, 30, 45) * Time.deltaTime);
    }
}
```
EnemyMovement.cs

```cs

// Script for an enemy tracking player movement within a mesh
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
```

FieldOfView.cs
```cs
// Controls the field of view for enemies to detect player character. Experimenting with cone vision vs 360 degrees in version 3.
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
```