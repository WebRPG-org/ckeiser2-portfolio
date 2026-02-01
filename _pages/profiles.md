---
layout: profiles
permalink: /about_me/
title: about me
description:
nav: false
nav_order: 7

profiles:
  # if you want to include more than one profile, just replicate the following block
  # and create one content file for each profile inside _pages/
  - align: right
    image: pfp.png
    content: about_einstein.md
    image_circular: false # crops the image to make it circular
    more_info: >
      Information Sciences
      University of Illinois (UIUC)
      St. Louis, MO
---


<div class="row">
{% include about/skills.html title="Design // Development" source=site.data.Game_Design-skills %}
</div>

<div class="row">
{% include about/skills.html title="Python/Data Skills" source=site.data.data-skills %}
</div>

<div class="row">
{% include about/skills.html title="Programming Languages" source=site.data.other-skills %}
</div>

<div class="row">
{% include about/timeline.html %}
</div>

