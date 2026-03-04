Graduated from the University of Illinois with a Bachelor’s in Information Sciences and a Minor in Game Studies and Design in Spring 2024. Currently working as an IT Auditor for a consulting firm while also involved in their internal application/tool development team as a python backend developer.


<div class="row">
{% include about/skills.html source=site.data.Game_Design-skills %}
</div>

<div class="row">
{% include about/skills.html source=site.data.data-skills %}
</div>

<div class="row">
{% include about/skills.html source=site.data.other-skills %}
</div>

<script>
document.addEventListener("DOMContentLoaded", () => {
  const bars = document.querySelectorAll(".skill-bar");

  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const bar = entry.target;
          const value = bar.dataset.percentage;

          if (value) {
            bar.style.width = value + "%";
          }

          observer.unobserve(bar);
        }
      });
    },
    { threshold: 0.3 }
  );

  bars.forEach(bar => observer.observe(bar));
});
</script>

