// top_reviews_chart.js

window.addEventListener('DOMContentLoaded', () => {
  // Find the existing container in the HTML
  const chartContainer = document.getElementById("chart-container");
  if (!chartContainer) {
    console.error("Chart container not found!");
    return;
  }

  // Create and style chart wrapper
  const container = document.createElement('div');
  container.style.padding = '40px';
  container.style.backgroundColor = '#ffff';
  container.style.fontFamily = 'Arial, sans-serif';

  // Add heading
  const heading = document.createElement('h2');
  heading.textContent = 'Top 5 Best-Reviewed Spots (Place holder)';
  heading.style.color = '#333';
  container.appendChild(heading);

  // Create canvas element
  const canvas = document.createElement('canvas');
  canvas.id = 'review-chart';
  canvas.style.background = '#fff';
  canvas.style.borderRadius = '8px';
  canvas.style.boxShadow = '0 4px 12px rgba(0,0,0,0.1)';
  canvas.style.padding = '20px';
  container.appendChild(canvas);

  // Append chart container to page
  chartContainer.appendChild(container);

  // Create the chart
  const ctx = canvas.getContext("2d");
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ["Spot1", "Spot2", "Spot3", "Spot4", "Spot5"],
      datasets: [{
        label: "Average Review (out of 5)",
        backgroundColor: "#081C8F",
        data: [4.9, 4.8, 4.6, 4.5, 4.3]
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      plugins: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Top 5 Products by Review Average'
        },
        tooltip: {
          callbacks: {
            label: function(context) {
              return context.dataset.label + ': ' + context.parsed.x.toFixed(1);
            }
          }
        }
      },
      scales: {
        x: {
          min: 0,
          max: 5,
          title: {
            display: true,
            text: 'Average Rating'
          }
        },
        y: {
          ticks: {
            callback: function(value) {
              return value;
            }
          }
        }
      }
    }
  });
});
