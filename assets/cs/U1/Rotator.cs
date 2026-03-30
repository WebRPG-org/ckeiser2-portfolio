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