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

In progress PlayerController.cs script handles player movement and physics and contact with enemies.
{% highlight cs linenos %}

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
{% endhighlight %}


{% highlight cs linenos %}

// Camera follows player movement, as player is a ball ensures camera does not rotate with the balls rotation.

// CameraController.cs

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
{% endhighlight %}

Rotator.cs

{% highlight cs linenos %}

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
{% endhighlight %}

EnemyMovement.cs

{% highlight cs linenos %}

// Script for an enemy tracking player movement within a mesh
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
