---
layout: page
permalink: /repositories/
title: repositories
description: A look at the repo behind this page and my other github projects. *Note* my previous portfolio page (ckeiser2) has over 200 commits to it over the past 2 years of development. But, since I pushed those updates from my IDE with a different email than my github, it did not count as a contribution.
nav: true
nav_order: 4
---

{% if site.data.repositories.github_users %}

## GitHub users

<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for user in site.data.repositories.github_users %}
    {% include repository/repo_user.liquid username=user %}
  {% endfor %}
</div>

---

{% if site.repo_trophies.enabled %}
{% for user in site.data.repositories.github_users %}
{% if site.data.repositories.github_users.size > 1 %}

  <h4>{{ user }}</h4>
  {% endif %}
  <div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% include repository/repo_trophies.liquid username=user %}
  </div>

---

{% endfor %}
{% endif %}
{% endif %}

{% if site.data.repositories.github_repos %}

## GitHub Repositories

<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.liquid repository=repo %}
  {% endfor %}
</div>
{% endif %}

--- 

{% if site.repo_langs.enabled %}
## Top Languages in Repositories

*Notes*: 
- Most code found in "Jupyter Notebooks" would be Python.
- Removed tracking of html, css, liquid and scss as two projects are portfolios, did not want to skew the numbers.

<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% include repository/repo_langs.liquid username=site.repo_langs.username %}
</div>
{% endif %}