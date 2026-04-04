---
layout: page
title: Playable and In Progress! [Asteroid Survivors] 🎮
description: 2D Unity demo [In Progress]
img: assets/img/title_screen.png
category: games 🎮


---
##### Work in progress using Unity Learn as an aid for this project.

**In the process of updating soon, still early in development**

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


### **Desktop Web version of Asteroid Survivors**
*Note*: Will only work on Desktop, as no mobile inputs are in source code. Use scroll wheel to find fullscreen icon in bottom right corner. Click "esc" to exit fullscreen mode.

```md
Left mouse click: Control the ship
Space bar: shoot
```

<div class="game-frame">
  <iframe
    src="{{ site.baseurl }}/assets/games/asteroid_survivors/index.html"
    width="120%"
    height="1000"
    frameborder="0"
    allowfullscreen>
  </iframe>
</div>