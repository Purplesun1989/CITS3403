// review_quality_pie_chart.js

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
  container.style.backgroundColor = '#fff';
  container.style.fontFamily = 'Arial, sans-serif';

  // Add heading
  const heading = document.createElement('h2');
  heading.textContent = 'Review Distribution Breakdown';
  heading.style.color = '#333';
  container.appendChild(heading);

  // Create canvas element
  const canvas = document.createElement('canvas');
  canvas.id = 'pie-chart';
  canvas.style.background = '#fff';
  canvas.style.borderRadius = '8px';
  canvas.style.boxShadow = '0 4px 12px rgba(0,0,0,0.1)';
  canvas.style.padding = '20px';
  container.appendChild(canvas);

  // Append chart container to page
  chartContainer.appendChild(container);

  // Review quality data
  const labels = ["100%", "90%", "80%", "70%", "60%", "50%", "40%", "30%", "20%", "10%"];
  const data = [120, 90, 75, 60, 50, 40, 30, 20, 10, 5]; // Example data

  const backgroundColors = [
    "#003f5c", "#2f4b7c", "#665191", "#a05195", "#d45087",
    "#f95d6a", "#ff7c43", "#ffa600", "#c2c2c2", "#969696"
  ];

  // Render pie chart
  const ctx = canvas.getContext("2d");
  new Chart(ctx, {
    type: 'pie',
    data: {
      labels: labels,
      datasets: [{
        label: "Review Distribution",
        backgroundColor: backgroundColors,
        data: data
      }]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Distribution of Reviews by Percentage Rating'
        },
        legend: {
          position: 'bottom'
        },
        tooltip: {
          callbacks: {
            label: function(context) {
              const value = context.parsed;
              const label = context.label;
              return `${label}: ${value} reviews`;
            }
          }
        }
      }
    }
  });
});
