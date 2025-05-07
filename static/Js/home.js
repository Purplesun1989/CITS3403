
  const top5 = [
    { spot: 'AQWA', value: 162057403 },
    { spot: 'Beach Club', value: 160388407 },
    { spot: 'Causeway', value: 137052885 },
    { spot: 'Ezone', value: 90569873 },
    { spot: 'Shoe Bar', value: 85514673 }
  ];

  const top6 = [
      '/static/Assets/Fun/AQWA/P1040827.webp',
      '/static/Assets/Grub/Bangkok_bros/图片_20250423152049.webp',
      '/static/Assets/Study/Ezone/图片_20250423152245.webp',
      '/static/Assets/Chill/Great_Court_South/P1038411.webp',
      '/static/Assets/Snap/City_of_Perth/P1038754.webp',
      '/static/Assets/Shop/London_Street/图片_20250423152302.webp',
    ];

  const coordinates = [-31.97903, 115.81822]
  const page_info = ["","",""]

  document.addEventListener('DOMContentLoaded', () => {

    const chartDom = document.getElementById('echart-line');
    const myChart = echarts.init(chartDom, null, { renderer: 'canvas' });
    const option = {
      title: {
        text: 'Tendency in last 5 days',
        left: 'center',
        textStyle: { color: '#fff' }
      },
      tooltip: { trigger: 'axis' },
      legend: {
        right: 10,
        top: 'middle',
        orient: 'vertical',
        textStyle: { color: '#eee' },
        data: ['Snap', 'Chill', 'Study', 'Shop', 'Grub', 'Fun']
      },
      grid: {
        top: 60, bottom: 30, left: 50, right: 150
      },
      xAxis: {
        type: 'category',
        data: ['1', '2', '3', '4', '5'],
        axisLine: { lineStyle: { color: '#444' } },
        axisLabel: { color: '#ccc' }
      },
      yAxis: {
        type: 'value',
        axisLine: { lineStyle: { color: '#444' } },
        splitLine: { lineStyle: { color: '#444' } },
        axisLabel: { color: '#ccc' }
      },
      series: [
        { name: 'Snap', type: 'line', smooth: true, data: [12, 19, 3, 5, 2] },
        { name: 'Chill', type: 'line', smooth: true, data: [2, 29, 5, 5, 20] },
        { name: 'Study', type: 'line', smooth: true, data: [3, 10, 13, 15, 22] },
        { name: 'Shop', type: 'line', smooth: true, data: [5, 15, 8, 12, 16] },
        { name: 'Grub', type: 'line', smooth: true, data: [7, 6, 18, 3, 10] },
        { name: 'Fun', type: 'line', smooth: true, data: [8, 14, 6, 18, 12] }
      ]
    };
    myChart.setOption(option);
    window.addEventListener('resize', () => myChart.resize());
  });


  document.addEventListener('DOMContentLoaded', () => {
    const halfs = document.querySelectorAll('.gallery-popular-box .half');
    halfs.forEach((half, idx) => {
      const imgDiv = half.querySelector('.square-imgs');
      if (imgDiv && top6[idx]) {
        imgDiv.style.backgroundImage = `url('${top6[idx]}')`;
        imgDiv.style.backgroundSize = 'cover';
        imgDiv.style.backgroundPosition = 'center';
      }
    });
  });
  const ctx = document.getElementById('ranking-chart').getContext('2d');

  const chart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: top5.map(d => d.spot),
      datasets: [{
        label: 'votes',
        data: top5.map(d => d.value),
        backgroundColor: [
          '#6a040f',
          '#d00000',
          '#e85d04',
          '#f77f00',
          '#fcbf49',
        ],
        borderRadius: 10,
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
      },
      scales: {
        x: {
          ticks: {
            color: 'white'
          },
          grid: {
            color: '#444'
          }
        },
        y: {
          ticks: {
            color: 'white'
          },
          grid: {
            color: '#444'
          },
          barPercentage: 0.4,
          categoryPercentage: 0.5
        }
      },
      elements: {
        bar: {
          barThickness: 10
        }

      }
    }
  });

  document.addEventListener('DOMContentLoaded', () => {
    const input = document.querySelector('.search-box input');
    const gallery = document.querySelector('.gallery-box');
    const when_search = document.querySelector('.when-search-box');

    input.addEventListener('focus', () => {
      gallery.style.display = 'none';
      when_search.style.display = 'block';
    });

  document.addEventListener('click', e => {
      if (!input.contains(e.target) && !when_search.contains(e.target)) {
        when_search.style.display = 'none';
        gallery.style.display = 'block';
      }
    });
  });


  var map = L.map('map').setView(coordinates, 16);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);
  var marker = L.marker(coordinates).addTo(map);
  marker.bindPopup('<b>I am here !!!</b>').openPopup();