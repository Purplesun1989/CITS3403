
const fakeData = [
  {
    author: 'Alice Johnson', date: 'May 1, 2025', comment: `It's not as easy as some of the reviews say, still requires a lot of work. This is expected, but among
all my biomed units this unit needed a lot more attention…`, rating: 5
  },
  { author: 'Bob Smith', date: 'May 2, 2025', comment: 'Quite good, but could use more details.', rating: 4 },
  { author: 'Carol Williams', date: 'May 3, 2025', comment: 'It was okay, nothing special.', rating: 3 },
  { author: 'David Brown', date: 'May 4, 2025', comment: 'Too short, please expand next time.', rating: 2 },
  { author: 'Eve Davis', date: 'May 5, 2025', comment: 'Not very satisfied with the content.', rating: 1 },
  { author: 'Frank Miller', date: 'May 6, 2025', comment: 'Visited again—still love it!', rating: 5 },
  { author: 'Grace Wilson', date: 'May 7, 2025', comment: 'Thumbs up to the author 👍', rating: 5 },
  { author: 'Henry Moore', date: 'May 8, 2025', comment: 'Learned a lot, thanks for sharing.', rating: 4 },
  { author: 'Ivy Taylor', date: 'May 9, 2025', comment: 'Felt it lacked depth.', rating: 3 },
  { author: 'Jack Anderson', date: 'May 10, 2025', comment: 'Stars ⭐ all around!', rating: 5 }
];


function fetchComments() {
  return new Promise(resolve => {
    setTimeout(() => resolve(fakeData), 300);
  });
}

function setRating(box, rating) {
  const stars = box.querySelectorAll('.starContainer .rate-star');
  stars.forEach((star, i) => {
    star.classList.toggle('active', i < rating);
  });
}



document.addEventListener('DOMContentLoaded', async () => {
  const data = await fetchComments();
  const authors = data.map(item => item.author);
  const dates = data.map(item => item.date);
  const comments = data.map(item => item.comment);
  const ratings = data.map(item => item.rating);

  const boxes = document.querySelectorAll('.comment-box');
  boxes.forEach((box, idx) => {
    box.querySelector('.comment-author').textContent = authors[idx] || '';
    box.querySelector('.comment-date').textContent = dates[idx] || '';
    box.querySelector('.comment-text').textContent = comments[idx] || '';
    setRating(box, ratings[idx] || 0);
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const likediconUrls = [
    'Assets/Fun/AQWA/P1040827.JPG',
    'Assets/Fun/Beach_Club/P1040031.JPG',
    'Assets/Fun/Causeway_Bridge/P1038620.JPG',
    'Assets/Grub/Bangkok_bros/图片_20250423152049.jpg',
    'Assets/Study/Ezone/图片_20250423152245.jpg',
    'Assets/Grub/The_shoe_bar/图片_20250423152248.jpg',
    'Assets/Snap/City_of_Fremantle/P1039326.JPG',
    'Assets/Fun/Governor_House_opening_day/P1039926.JPG',
    'Assets/Fun/Italy_Festival/图片_20250423152304.jpg',
    'Assets/Chill/Johns_national_park/图片_20250423152102.jpg',
    'Assets/Chill/Hillarys_Beach/P1040862.JPG',
    'Assets/Chill/Great_Court_South/P1038411.JPG',
    'Assets/Snap/City_of_Perth/P1038754.JPG',
    'Assets/Shop/London_Street/图片_20250423152302.jpg',
    'Assets/Shop/London_Street/图片_20250423152302.jpg',
    'Assets/Shop/London_Street/图片_20250423152302.jpg',
    'Assets/Shop/London_Street/图片_20250423152302.jpg',
    'Assets/Shop/London_Street/图片_20250423152302.jpg',
    'Assets/Shop/London_Street/图片_20250423152302.jpg',
    'Assets/Shop/London_Street/图片_20250423152302.jpg',
  ];

  const likedlisticons = document.querySelectorAll('.likedlist-icon');
  likedlisticons.forEach((item, index) => {
    if (likediconUrls[index]) {
      item.style.backgroundImage = `url('${likediconUrls[index]}')`;
    }
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const input = document.querySelector('.search-box input');
  const gallery = document.querySelector('.specific-display-box');
  const when_search = document.querySelector('.when-search-box');
  const comments = document.querySelector('.comment-section-box');

  input.addEventListener('focus', () => {
    gallery.style.display = 'none';
    when_search.style.display = 'block';
    comments.style.display ='none';
  });

  document.addEventListener('click', e => {
    if (!input.contains(e.target) && !when_search.contains(e.target)) {
      when_search.style.display = 'none';
      gallery.style.display = 'block';
      comments.style.display = 'block';
    }
  });
});




document.addEventListener('DOMContentLoaded', function () {
  // 三张图各自的配置：容器 id、标题、和数据
  const configs = [
    {
      id: 'pie1',
      title: 'Agepalooza',
      data: [
        { value: 335, name: '12-18' },
        { value: 310, name: '18-25' },
        { value: 234, name: '25+' }
      ]
    },
    {
      id: 'pie2',
      title: 'Genderpalooza',
      data: [
        { value: 524, name: 'male' },
        { value: 635, name: 'female' },
        { value: 235, name: 'none binary' }
      ]
    },
    {
      id: 'pie3',
      title: 'WeekiVisits',
      data: [
        { value: 1548, name: '1' },
        { value: 535, name: '<3' },
        { value: 510, name: '3+' }
      ]
    }
  ];

  configs.forEach(cfg => {
    const dom = document.getElementById(cfg.id);
    const chart = echarts.init(dom);
    const option = {
      title: {
        text: cfg.title,
        left: 'center'
      },
      tooltip: {
        trigger: 'item'
      },
      legend: {
        bottom: 0
      },
      series: [
        {
          name: cfg.title,
          type: 'pie',
          radius: '50%',
          data: cfg.data,
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          }
        }
      ]
    };
    chart.setOption(option);
  });
});

document.addEventListener('DOMContentLoaded', () => {
  // 要展示的图片路径数组
  const pics = [
    'Assets/Fun/AQWA/P1040827.JPG',
    'Assets/Fun/Beach_Club/P1040031.JPG',
    'Assets/Fun/Causeway_Bridge/P1038620.JPG',
    'Assets/Grub/Bangkok_bros/图片_20250423152049.jpg'
  ];
  let currentIndex = 0;

  const mainImg = document.querySelector('.pic-box .main-slider img');
  const thumbsContainer = document.querySelector('.pic-box .thumbs-container');
  const btnPrev = document.querySelector('.pic-box .thumb-prev');
  const btnNext = document.querySelector('.pic-box .thumb-next');

  // 生成缩略图列表
  pics.forEach((src, idx) => {
    const wrapper = document.createElement('div');
    wrapper.className = 'thumb-item';
    const img = document.createElement('img');
    img.src = src;
    img.alt = `Thumb ${idx + 1}`;
    img.addEventListener('click', () => showImage(idx));
    wrapper.appendChild(img);
    thumbsContainer.appendChild(wrapper);
  });

  // 切换主图并滚动当前缩略图到中间
  function showImage(idx) {
    currentIndex = idx;
    mainImg.src = pics[idx];
    thumbsContainer.children[idx]
      .scrollIntoView({ behavior: 'smooth', inline: 'center' });
  }

  btnPrev.addEventListener('click', () => {
    if (currentIndex > 0) showImage(currentIndex - 1);
  });
  btnNext.addEventListener('click', () => {
    if (currentIndex < pics.length - 1) showImage(currentIndex + 1);
  });

  // 初始化第一张
  showImage(0);
});


// Ratings Data
const ratingsData = [
  { name: "Cleanliness", left: "Dirty", right: "Spotless", score: 8 },
  { name: "Atmosphere", left: "Unpleasant", right: "Welcoming", score: 7 },
  { name: "Comfort", left: "Uncomfortable", right: "Cozy", score: 9 },
  { name: "Accessibility", left: "Inconvenient", right: "Convenient", score: 8 },
  { name: "Value", left: "Overpriced", right: "Worth It", score: 7 },
  { name: "Service Quality", left: "Poor", right: "Excellent", score: 9 },
  { name: "Noise Level", left: "Too Loud", right: "Quiet", score: 6 },
  { name: "Crowdedness", left: "Too Crowded", right: "Spacious", score: 5 },
];

function createSlider(id, value) {
  const slider = document.getElementById(id);
  noUiSlider.create(slider, {
    start: [value],
    range: { min: 0, max: 10 },
    step: 1,
    connect: [true, false],
    tooltips: true,
    behaviour: "none",
    format: { to: v => Math.round(v), from: v => Number(v) }
  });
  slider.setAttribute('disabled', true);
}

document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('ratings-container');
  ratingsData.forEach((rating, idx) => {
    const card = document.createElement('div');
    card.className = 'rating-card';
    card.innerHTML = `
          <div class="rating-label">${rating.name}</div>
          <div class="d-flex align-items-center">
            <div class="label-left text-muted">${rating.left}</div>
            <div id="slider${idx}" class="slider-wrapper"></div>
            <div class="label-right text-muted">${rating.right}</div>
          </div>
        `;
    container.appendChild(card);
    createSlider(`slider${idx}`, rating.score);
  });
});

function creatbar(id) {
  const slider = document.getElementById(id);
  noUiSlider.create(slider, {
    start: [5],
    range: { min: 0, max: 10 },
    step: 1,
    connect: [true, false],
    tooltips: true,
    format: { to: v => Math.round(v), from: v => Number(v) }
  });
}

document.addEventListener('DOMContentLoaded', () => {
  const uploadcontainer = document.getElementById('upload-bar-box');
  ratingsData.forEach((upload, idx) => {
    const card = document.createElement('div');
    card.classList = 'rating-card';
    card.innerHTML = `
            <div class="rating-label">${upload.name}</div>
            <div class="d-flex align-items-center">
            <div class="label-left text-muted">${upload.left}</div>
            <div id="upload-slider${idx}" class="slider-wrapper"></div>
            <div class="label-right text-muted">${upload.right}</div>
          </div>
        `;
    uploadcontainer.appendChild(card);
    creatbar(`upload-slider${idx}`);
  });
});

document.addEventListener('DOMContentLoaded', () => {
  var map = L.map('spe-map').setView([-31.97903, 115.81822], 16);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);
  L.marker([-31.9795, 115.8187]).addTo(map)
    .bindPopup('<b>I am here!</b>').openPopup();
});








