document.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('myChart').getContext('2d');

    const data = {
      labels: ['Main Library', 'Ezone', 'Great Court Lawn', 'Guild Cafe', 'Hackett Hall'],
      datasets: [{
        label: 'Number of Reviews',
        data: [45, 30, 20, 10, 5], // Example review counts
        backgroundColor: [
          '#081C8F',
          '#FF007F',
          '#FFD738',
          '#000000',
          '#15bde7',
        ],
        borderWidth: 1
      }]
    };

    const config = {
      type: 'pie',
      data: data,
      options: {
        responsive: true,
        layout: {
            padding: {
                top: 0,
                bottom: 0,
            },
        },
        plugins: {
          legend: {
            position: 'right',
            labels: {
              color: 'black'
            }
          },
        }
      },
    };

    new Chart(ctx, config);
  });
