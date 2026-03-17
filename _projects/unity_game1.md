---
layout: page
title: In Progress! [Roll-a-Ball] 🎮
description: Unity demo excercise where you play as a ball collecting consumables, dodging enemies.
img:
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

In progress PlayerController.cs script handles player movement and physics.

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

    }
    void OnMove(InputValue movementValue)
    {
        Vector2 movementVector = movementValue.Get<Vector2>();

        movementX = movementVector.x; 
        movementY = movementVector.y; 
    }

    void SetCountText()
    {
        countText.text = "Count: " + count.ToString();
    }
    void FixedUpdate()
    {
        Vector3 movement = new Vector3(movementX, 0.0f, movementY);
        rb.AddForce(movement * speed);

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

Camera follows player movement, as player is a ball ensures camera does not rotate with the balls rotation.

CameraController.cs
```cs
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
For the collectibles in the game, to give a visual *Pop* we have this simple rotating script.

```cs
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

Script for an enemy tracking player movement within a mesh
```cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;


public class EnemyMovement : MonoBehaviour
{
    public Transform player;
    private NavMeshAgent navMeshAgent;
    
    void Start()
    {
        navMeshAgent = GetComponent<NavMeshAgent>();
    }

    void Update()
    {
        if (player != null)
        {
            navMeshAgent.SetDestination(player.position);
        }
    }
}
```