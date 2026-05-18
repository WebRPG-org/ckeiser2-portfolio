---
layout: page
title: my games
permalink: /games/
description: A growing collection of my game related projects.
nav: true
nav_order: 2
display_categories: [games 🎮]
horizontal: false
---

<!-- pages/games.md -->
<div class="games">
{% if site.enable_game_categories and page.display_categories %}
  <!-- Display categorized games -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_games = site.games | where: "category", category %}
  {% assign sorted_games = categorized_games | sort: "importance" %}
  <!-- Generate cards for each game -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for game in sorted_games %}
      {% include games_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for game in sorted_games %}
      {% include games.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display games without categories -->

{% assign sorted_games = site.games | sort: "importance" %}

  <!-- Generate cards for each game -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for game in sorted_games %}
      {% include games_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for game in sorted_games %}
      {% include games.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>
