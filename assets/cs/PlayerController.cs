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
