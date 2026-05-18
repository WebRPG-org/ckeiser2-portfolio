---
title: 🎮 Twine Game - "A Myconid's Story" [Playable in Browser]🖋️ 🕹️
category: games 🎮
img: assets/pngs/html_story.png
layout: page
description: Choose your own adventure short story, with 18 possible endings. Playable within Browser.

---
## Skills showcased
*HTML & CSS* *In-Engine Tools* *JavaScript*


##### Role: Solo Developer

## Playable Version of game below 🕹️
<iframe
  src="{{ 'assets/games/dnd.html' | relative_url }}"
  width="140%"
  height="750"
  style="border: none; border-radius: 8px;"
  loading="lazy">
</iframe>

---

### Refer to the below for Development details and game features!

#### Description
Creative writing DND-esque story with multiple endings written in HTML and CSS along with the Twine engines own language to hold onto and remember variables. Showcases a choose your own adventure story with questionable writing but cool mechanics for being text based. Decisions matter and even programmed a stats system in one of the storylines. Clicking on page will send you to an itch.io page where you can enjoy the html or Twine's own language "Twee" version. Different pathways have different story modes including a stat system in the (Dungeon Quest) and paths and choices being unlocked when you uncover different information in the picture below you can see a visualization of the different pathways with 18 unique endings. 

*Below is a picture of story nodes along with an embedded version of the game*

<img src="{{ site.baseurl }}/assets/pngs/html_story.png" alt="Breakdown of story nodes in Twine Engine">


## Features

There are sections throughout the game below where your choices will effect other choices. In the middle of the game you can choose three different kinds of quests. When you choose the "Dungeon Quest" the game remembers 5 outcomes to dice you roll at a tavern. Refer to the below backend:

##### Your rolls
```js
You choose the Dungeon Quest hanging on the bulletin board. It calls for the exploration of the abandon Dwarven mines of Skarsgarl. You remember the Myconid colony of the Astarians now live in these dungeons. There will be a journey to the mines ,hopefully your party is both ready... and *lucky*...

	Before the group leaves Brimly introduces you to one of the games in the tavern.
    
   Brimly remarks "$name role the dice and hit large so we have great fortune on our journey!!!"
   
   You hunch over the betters table and for fun role a whole set of dice... your outcomes are:
   *D4: $D4
   
   D6: $D6
   
   D8: $D8
   
   D20: $D20
   
   D100: $D100*
   
After seeing your *luck* you are ready for your journey.
[ [[Path to Skarsgarl]] ]
```
##### Your rolls dictacting which dialgoue options you have.
```js
The party leaves the small village with no guarntee they will return to collect their prize of 500 Gold. The group decides to cut through the Orlan's Thicket, a densly packed forest with narrow paths that'll make traversal challenging for the group. 

(if: $unite is true) [
You remember that this forest is home to one of the other Myconid colonies the Penterelle. You could see out their aid to help your party gain passage through the forest. [[Seek the aid of the Penterelle]] 
]

(if: $D8 is >1) + (if: $unite is false) [
*Your combat check: D8: $D8 *
	The party can think of no aid to help them through the thicket. They venture forth, and encounter a Cockatrice. A large chicken like creature with a tail reminiscent of a lizard's. The party braves for the encounter... The Cockatrice is swiftly defeated as Lysandra casts a hex on the creature binding it to the ground, while Fried swiftly shadow steps appearing through the creatures shadow knocking it out, in the coolest of fashion. The party continue on their way to the [[Iron Gate of Skarsgarl]] 
<img src="C:\Users\colto\Dropbox\Cockatrice.png"\>
]

(if: $D8 is <=1) + (if:$unite is false) [
*Your combat check: D8: $D8*
	The party can think of no aid to help them through the thicket. They venture forth, and encounter a Cockatrice. A large chicken like creature with a tail reminiscent of a lizard's. The party braves for the encounter...Some how, some way... The entire party has been bested by little more than a chicken. You thought the gods were throwing you an underhand with your first encounter. But from sheer incompetence or not being favored by the gods, you have not been favored by this world's cruel gods. You pass away not as a glorious and worshipped adventurer but as a lowsy chicken's dinner. 
<img src="C:\Users\colto\Dropbox\Cockatrice.png"\> 
Ending 2/18
]

(if: $D100 is >=25) + (if: $D6 is >=3)[
*Your perception check D100: $D100 and D6: $D6 *
	The party comes across an old man, a Hermit. He offers his aid to get through the thicket. He lives in a cottage near the entrance of the dense woods. An old man but once a great warrior and companion of the King of Caldea He could be quite helpful in helping the party cross the Thicket. [[Accept Hermit Aid]]
]
```





