
// const tendency = [
//   [12, 19, 3, 5, 2],
//   [2, 29, 5, 5, 20],
//   [3, 10, 13, 15, 22],
//   [5, 15, 8, 12, 16],
//   [7, 6, 18, 3, 10],
//   [8, 14, 6, 18, 12]
// ];


var coordinates = [[-31.97903, 115.81822],[-31.980522864646908, 115.81999644399392]];

// ============ DOM 逻辑优化 ============ //
document.addEventListener('DOMContentLoaded', () => {

  // 1. 折线图（echarts）
  const chartDom = document.getElementById('echart-line');
  if (chartDom) {
    const myChart = echarts.init(chartDom, null, { renderer: 'canvas' });
    myChart.setOption({
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
      grid: { top: 60, bottom: 30, left: 50, right: 150 },
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
        { name: 'Snap', type: 'line', smooth: true, data: tendency[0] },
        { name: 'Chill', type: 'line', smooth: true, data: tendency[1] },
        { name: 'Study', type: 'line', smooth: true, data: tendency[2] },
        { name: 'Shop', type: 'line', smooth: true, data: tendency[3] },
        { name: 'Grub', type: 'line', smooth: true, data: tendency[4] },
        { name: 'Fun', type: 'line', smooth: true, data: tendency[5] }
      ]
    });
    window.addEventListener('resize', () => myChart.resize());
  }

  // 2. 横向柱状图（chart.js）
  const ctx = document.getElementById('ranking-chart');
  if (ctx) {
    new Chart(ctx.getContext('2d'), {
      type: 'bar',
      data: {
        labels: top5.map(d => d.spot),
        datasets: [{
          label: 'heats',
          data: top5.map(d => d.value),
          backgroundColor: ['#6a040f', '#d00000', '#e85d04', '#f77f00', '#fcbf49'],
          borderRadius: 10,
          borderSkipped: false
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        plugins: { legend: { display: false } },
        scales: {
          x: { ticks: { color: 'white' }, grid: { color: '#444' } },
          y: { ticks: { color: 'white' }, grid: { color: '#444' }, barPercentage: 0.4, categoryPercentage: 0.5 }
        },
        elements: { bar: { barThickness: 10 } }
      }
    });
  }

  // 3. 渲染 popular 图像（top6）
  const cards = document.querySelectorAll('.gallery-popular-box .half');
  cards.forEach((card, idx) => {
  if (top6[idx]) {
    const imgDiv = card.querySelector('.square-imgs');
    const p = card.querySelector('p');

    if (imgDiv) {
      imgDiv.style.backgroundImage = `url('${top6[idx].path}')`;
      imgDiv.style.backgroundSize = 'cover';
      imgDiv.style.backgroundPosition = 'center';
    }

    if (p) {
      p.textContent = top6[idx].name;
    } else {
      // 如果 <p> 是纯文本 placeholder，要替换成 <p>
      card.innerHTML = card.innerHTML.replace('this is a place holder', `<p>${top6[idx].name}</p>`);
    }
  }
});


  // 4. 推荐
  const likebox = document.querySelector(".liked-box-content");
  if (likebox) {
    let html = '';
    likeData.forEach(items => {
      html += `
   <a href= "/index/${items.id}">
    <div class="liked-box-items">
      <img src="${items.path}" alt="${items.name}" class="likedlist-icon" loading="lazy">
      <div class="likedlist-text">${items.name}<br><span class="text-muted-sm"></span></div>
      <i class="bi bi-heart-fill heart-icon"></i>
      <i class="bi bi-chat-dots"></i>
    </div>
   </a>
  `;
});

    likebox.innerHTML = html;
  }

  // 5. 搜索框交互
  const input = document.querySelector('.search-box input');
  const gallery = document.querySelector('.gallery-box');
  const when_search = document.querySelector('.when-search-box');
  if (input && gallery && when_search) {
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
  }

  // 6. Leaflet 地图渲染
const mapContainer = document.getElementById('map');
if (mapContainer && coordinates.length > 0) {
  const map = L.map('map').setView(coordinates[0], 16);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  top5.forEach((item, idx)=> {
   if (item.lat !== undefined && item.lon !== undefined) {
    // const marker = L.marker([item.lat, item.lon]).addTo(map);
    // marker.bindPopup(`<a href="/index/${item.id}"><b>${item.spot}</b></a>`);

    const offset = idx * 0.00005;  // 每个点轻微偏移
    const marker = L.marker([item.lat + offset, item.lon + offset]).addTo(map);
    marker.bindPopup(`<a href="/index/${item.id}"><b>${item.spot}</b></a>`);
  }
  });
}


//7.用户名称，头像，消息渲染
const profile_pic = document.querySelector(".profile-box");
const secondP = document.querySelector(".navright-box p:nth-of-type(2)");

if (profile_pic) {
  profile_pic.src = metainfo[2];
}

if (secondP) {
  secondP.textContent = metainfo[0];
}

});
