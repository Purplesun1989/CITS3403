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

const likeData = [
  { name: "Fremantle_Quey_Beach",      path: "/static/Assets/Chill/Fremantle_Quey_Beach/P1040614.webp",          likes: 124 },
  { name: "Great_Court_South",         path: "/static/Assets/Chill/Great_Court_South/P1038411.webp",             likes: 385 },
  { name: "Hillarys_Beach",            path: "/static/Assets/Chill/Hillarys_Beach/P1040852.webp",                likes: 276 },
  { name: "Johns_national_park",       path: "/static/Assets/Chill/Johns_national_park/图片_20250423152225.webp", likes: 499 },
  { name: "Scarborough",               path: "/static/Assets/Chill/Scarborough/P1038320.webp",                  likes: 213 },

  { name: "AQWA",                      path: "/static/Assets/Fun/AQWA/P1040824.webp",                            likes: 578 },
  { name: "Beach_Club",                path: "/static/Assets/Fun/Beach_Club/P1040060.webp",                      likes: 44  },
  { name: "Causeway_Bridge",           path: "/static/Assets/Fun/Causeway_Bridge/P1038572.webp",                likes: 337 },
  { name: "Caversham_Wildlife_park",   path: "/static/Assets/Fun/Caversham_Wildlife_park/P1041098.webp",        likes: 450 },
  { name: "Governor_House_opening_day",path: "/static/Assets/Fun/Governor_House_opening_day/P1039862.webp",      likes: 159 },
  { name: "Italy_Festival",            path: "/static/Assets/Fun/Italy_Festival/图片_20250423152308.webp",       likes: 521 },
  { name: "Japanese_Festival",         path: "/static/Assets/Fun/Japanese_Festival/P1038927.webp",              likes: 310 },
  { name: "Royal_show",                path: "/static/Assets/Fun/Royal_show/图片_20250423152324.webp",           likes: 89  },
  { name: "Street_Artist",             path: "/static/Assets/Fun/Street_Artist/P1040483.webp",                  likes: 392 },
  { name: "UWA_Tennis_court",          path: "/static/Assets/Fun/UWA_Tennis_court/P1038672.webp",               likes: 267 },

  { name: "Bangkok_bros",              path: "/static/Assets/Grub/Bangkok_bros/图片_20250423152310.webp",        likes: 146 },
  { name: "Sushi_Hub",                 path: "/static/Assets/Grub/Sushi_Hub/图片_20250423152314.webp",           likes: 223 },
  { name: "The_shoe_bar",              path: "/static/Assets/Grub/The_shoe_bar/图片_20250423152247.webp",         likes: 587 },

  { name: "London_Street",             path: "/static/Assets/Shop/London_Street/图片_20250423152302.webp",        likes: 301 },

  { name: "Art_museum_wa",             path: "/static/Assets/Snap/Art_museum_wa/图片_20250423152255.webp",        likes: 68  },
  { name: "City_of_Fremantle",         path: "/static/Assets/Snap/City_of_Fremantle/P1039411.webp",              likes: 532 },
  { name: "City_of_Mandurah",          path: "/static/Assets/Snap/City_of_Mandurah/P1039669.webp",               likes: 178 },
  { name: "City_of_Perth",             path: "/static/Assets/Snap/City_of_Perth/P1038740.webp",                  likes: 419 },
  { name: "UWA_tower",                 path: "/static/Assets/Snap/UWA_tower/P1038027.webp",                      likes: 246 },

  { name: "Ezone",                     path: "/static/Assets/Study/Ezone/图片_20250423152245.webp",               likes: 389 }
];

const charts = [
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


const pics = [
    '/static/Assets/Fun/AQWA/P1040827.webp',
    '/static/Assets/Fun/Beach_Club/P1040031.webp',
    '/static/Assets/Fun/Causeway_Bridge/P1038620.webp',
    '/static/Assets/Grub/Bangkok_bros/图片_20250423152049.webp'
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

charts.forEach(cfg => {
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

  // 生成缩略图列表

  let currentIndex = 0;
  const mainImg = document.querySelector('.pic-box .main-slider img');
  const thumbsContainer = document.querySelector('.pic-box .thumbs-container');
  const btnPrev = document.querySelector('.pic-box .thumb-prev');
  const btnNext = document.querySelector('.pic-box .thumb-next');
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

document.addEventListener('DOMContentLoaded',()=>{
  const likebox = document.querySelector(".liked-box-content");
  likeData.forEach((items,idx)=>{
    const likecard = document.createElement('div');
    likecard.classList='liked-box-items';
    likecard.innerHTML = `
        <div class="likedlist-icon"  style="background: url('${items.path}') center/cover no-repeat;">></div>
            <div class="likedlist-text" >${items.name}<br><span class="text-muted-sm"></span></div>
            <i class="bi bi-heart-fill heart-icon"></i>
            <i class="bi bi-chat-dots"></i>
        </div>
    `;
    likebox.appendChild(likecard)
  });
});








