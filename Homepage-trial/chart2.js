document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById('studySpotsChart').getContext('2d');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Campus Library', 'Coffee Corner', 'Quiet Cafe', 'Reading Room', 'Study Lounge'],
      datasets: [{
        label: '',
        data: [92, 88, 85, 82, 79],
        backgroundColor: [
          '#4cc9f0',
          '#4895ef',
          '#4361ee',
          '#3f37c9',
          '#7209b7'
        ],
        borderRadius: 10, // Rounded bars for a softer look
        borderSkipped: false
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      plugins: {
        legend: {
          display: false
        },
        title: {
          display: true,
          color: 'white',
          font: {
            size: 18
          }
        }
      },
      scales: {
        x: {
          beginAtZero: true,
          max: 100,
          grid: {
            color: 'rgba(255, 255, 255, 0.1)'
          },
          ticks: {
            color: 'white'
          },
          title: {
            display: true,
            text: '',
            color: 'white'
          }
        },
        y: {
          grid: {
            display: false
          },
          ticks: {
            color: 'white'
          },
          title: {
            display: true,
            text: '',
            color: 'white'
          }
        }
      }
    }
  });
});
