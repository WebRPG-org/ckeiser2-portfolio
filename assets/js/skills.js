document.addEventListener("DOMContentLoaded", () => {
  const bars = document.querySelectorAll(".skill-bar");

  if (!bars.length) return;

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
