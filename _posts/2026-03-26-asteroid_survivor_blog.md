---
layout: post
title: Asteroid Survivors Development
description: Learning 2D game development in Unity.
tags: Unity, C#
categories: gamedev
---

[Refer_to_this_page_for_playable_version](https://ckeiser2.github.io/portfolio/projects/asteroid_survivors/)

```md
Recently added features:
### Shop
Can buy multiple new power ups / features
- Mr.S: A deployable satellite that provides the player with a reuseable shield.
- Mr.B: A deployable satellite that provides the player with another blaster.
- Atk Up: More attack speed.
- Thruster: Gives the player a dash using "Left Shift" on a keyboard.

### More UI

### More Sound Effects

### New custom cursor

### More objects!!
- Added the colorful comet!!!
- Points now scale with asteroid type and size.
- Adding more features in the future!!
```

### Steps of Development

Role: Solo Developer

Early version poc with 2D game: 

<iframe src="{{ site.baseurl }}/assets/video/poc_u2.2.mp4"
        width="100%"
        height="400px"
        frameborder="0"
        style="border: 1px solid #ccc; border-radius: 8px;">
</iframe>

---

Added more features including the blaster, updated ship design, and new asteroids including white dward star, black hole, fire asteroid, and ice planet. Still developing models for them.

Each flying object has it's own:
- Gravity
- Visual Effects
- Traits

<iframe src="{{ site.baseurl }}/assets/video/poc_u2.3.mp4"
        width="100%"
        height="400px"
        frameborder="0"
        style="border: 1px solid #ccc; border-radius: 8px;">
</iframe>

---


### **Special Objects Guide**

##### Ice Asteroids

- Largest special object so far.
- cool blue partical effects.
- working on functionality that when shot breaks into pieces.

<img src="{{ site.baseurl }}/assets/img/iceplanet.png" alt="iceplanet">


##### Fire Asteroids / Fireball

- When spawns is extremely fast.
- Has multiple partical effects including fire trail and embers.
- Fastest special object.

<img src="{{ site.baseurl }}/assets/img/fireball.png" alt="fireball">


##### White Dwarf

- Work in progress.

<img src="{{ site.baseurl }}/assets/img/whitedwarf.png" alt="whitedwarf">


##### Black Hole

- Blends into background as both are black.
- Working on making it bigger the more it sucks up.
- Has its own gravity, very minor effect as of right now.
- Has major partical effects so player should rely on that to tell position.

<iframe src="{{ site.baseurl }}/assets/video/black_hole_showcase.mp4"
        width="100%"
        height="400px"
        frameborder="0"
        style="border: 1px solid #ccc; border-radius: 8px;">
</iframe>



##### New Feature 5.21.2026

- Added in recently was a radar to aid players with predicting fast paced objects coming from offscreen and also to identify other objects to rack up points.
- Drew the radar myself in Krita and imported and scripted all assets tied to new feature.

<img src="{{ site.baseurl }}/assets/pngs/game_radar.png" alt="GameRadar">
