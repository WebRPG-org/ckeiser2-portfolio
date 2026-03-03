---
title: 🎮 Concept Redesign ROR2 🕹️
#permalink: /games/:name/
category: games 🎮
#tools: [Design]
img: assets/pngs/galvin.png
layout: page
description: Addressing my redesign concept for a fighting game character 
---

##### Role: Solo Designer

#### Goal of this project is to redesign Rivals of Aether II character Galvin! Specifically the characters main mechanic galvinazation!

For my character redesign I chose a character from a personal favorite game series of mine "**Rivals of Aether**". This is a platform fighter that is heavily inspired by the fast paced combat seen in the Super Smash Bros series. What is notable in this game series is it's character designs as every character has an "aether" or elemental focus that they have dynamically integrated within their kits. This is usually shown through an emphasis on stage control (i.e. covering the stage in smoke, ice or a crytsal field). These elements will range from the 4 major kingdoms in the game fire, water, wind and earth. For the character we will be discussing **Galvin**, is affiliated with an earth related element with it's aether being metal/magnetism. 

A character's design should incorporate their narrative, thematic, and kit, reinforcing one another synergistically. Galvin's lore emphasizes a dinosaur-esque creature revived into the modern aether world. Enhanced with augments from the engineer who revived the dinosaur, in this Frankenstein-esque fantasy. The key mechanic with Galvin is his ability to enter a "Galvinized" state where the rust covering it's metal body falls off enhancing his charge/strong and special attacks. This additionally, turns the metal that covers his body from a tarnished green color to a pronounced shiny silver, emphasizing how he is in an empowered state. I will outline below the conditions that need to happen in order to both gain this "Galivinized" state and lose it, while providing visuals to aid the current understanding of how it works.

##### Standard model without galvinized mechanic
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/pngs/galvin1.png" title="Galvin" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Gaining Galvinzization:
- Hit a basic physical atttack

Losing Galvinsization:
- Get hit by any attack
- Using certain special or charge/strong attack (As it was enhanced by the state)
- Get parried
- Lose a stock (What platform fighting games will call lifes)

##### Model change when galvinized
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/pngs/galvin2.png" title="Galvin" class="img-fluid rounded z-depth-1" %}
    </div>
</div>


##### Gameplay example of Galvin Game play as reference

{% include video.liquid
   path="assets/mp4/galvin.mp4"
   autoplay=true
   muted=true
   loop=true
   controls=false
   class="w-100"
%}

##### Proposition to rework this mechanic

As we can currently see by my demonstration in the video and how I have described preivously. Galvin's empowered state of galvinization is quite confusing. There are many inconsistencies with how its been implemented and the animation around its activation. Within the fantasy of Galvin we are suppose to hit the apex of being a heavy fighting game character when the rust falls off the character and you enter this enhanced state. The galvinized state shows that the fantasy to be a heavy with a good *advantage state* (*In a fighting game where an individual is in the advantage. Which usually involves comboing or in the process of attacking the opponent*). With a single blow or missed ability you lose it once again. Additionally, when hitting an opponent (only in certain conditions) your character becomes shiny in this very jarring and unrewarding animation. My idea for a rework would be to essentially lock the empowered state (*Galvinzation*) behind a resource mechanic. This would be displayed at the bottom of the screen in which as a Galvin deals damage *of any sort*, this bar would start to fill up. With the completition of the bar there would be a visual animation and significant sound queue of the rust following off the metal dinosaur, revealing the shiny metal underneath. Due to the significant increase in difficulty in achieving state it would last significantly longer as the resource meter starts to drain. As the metal begins to rust again. In this time Galvin gets to use the enhanced versions of all of it's attacks while not having to worry about the constant switching between the two states. To emphasize the fantasy still of being a heavy character with a good advantage state, the Galvin can slow down the degrade of the resource meter by staying in the *advantage state* (*i.e. staying on the offensive*). Refer to below for a visual UI *Proof of Concept*.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/pngs/galvin3.png" title="Galvin" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
