// top_reviews_chart.js

document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('.award-button');
  const statsSection = document.getElementById('award-stats');
  const chartContainer = document.getElementById('chart-container');
  const titleElement = document.getElementById('award-title');

  buttons.forEach(button => {
    button.addEventListener('click', () => {
      const category = button.dataset.category;
      const metric = button.dataset.metric;
      const title = button.dataset.title;

      if (!category || !metric) {
        console.error("Missing category or metric on button.");
        return;
      }

      // Show stats section
      statsSection.style.display = 'block';
      titleElement.textContent = title || 'Top Spots';

      // Clear chart container
      chartContainer.innerHTML = '';

      const canvas = document.createElement('canvas');
      canvas.id = 'review-chart';
      chartContainer.appendChild(canvas);

      const ctx = canvas.getContext('2d');

      // Fetch the chart data from backend
      fetch(`/awards/top_reviews_data?category_id=${category}&metric=${metric}`)
        .then(response => response.json())
        .then(data => {
          const labels = data.map(item => item.name);
          const values = data.map(item => item.avg);

          new Chart(ctx, {
            type: 'bar',
            data: {
              labels: labels,
              datasets: [{
                label: 'Score (out of 10)',
                backgroundColor: '#081C8F',
                data: values
              }]
            },
            options: {
              indexAxis: 'y',
              responsive: true,
              plugins: {
                legend: { display: false },
                title: {
                  display: true,
                  text: title
                },
                tooltip: {
                  callbacks: {
                    label: ctx => `Score: ${ctx.parsed.x.toFixed(1)}`
                  }
                }
              },
              scales: {
                x: {
                  min: 0,
                  max: 10,
                  title: {
                    display: true,
                    text: 'Rating'
                  }
                }
              }
            }
          });
        })
        .catch(err => {
          console.error("Error loading chart data:", err);
        });
    });
  });
});
