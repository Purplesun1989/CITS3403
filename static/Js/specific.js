const pics = metainfo.slice(4, 10);

function creatbar(sliderId, inputId, startValue = 5) {
  const sliderEl = document.getElementById(sliderId);
  const inputEl  = document.getElementById(inputId);
  if (!sliderEl || !inputEl) return;

  noUiSlider.create(sliderEl, {
    start: [ startValue ],
    range: { min: 0, max: 5 },
    step: 1,
    connect: [ true, false ],
    tooltips: true,
    format: {
      to:   v => Math.round(v),
      from: v => Number(v)
    }
  });

  // 每次值变化时，把最新值写到隐藏 input 的 value
  sliderEl.noUiSlider.on('update', (values) => {
    inputEl.value = values[0];
  });
}

function createSlider(id, value) {
  const slider = document.getElementById(id);

  if (!slider) return;
  noUiSlider.create(slider, {
    start: [value],
    range: { min: 0, max: 5 },
    step: 1,
    connect: [true, false],
    tooltips: true,
    behaviour: "none",
    format: { to: v => Math.round(v), from: v => Number(v) }
  });
  slider.setAttribute('disabled', true);
}



// ==================== DOM 渲染逻辑 ====================

document.addEventListener('DOMContentLoaded', async () => {

  //评论区
const comment_box = document.querySelector(".comment-section-box");
if (comment_box) {
  comment_box.innerHTML = fakeData.map(item => {
    const stars = Array.from({ length: 5 }, (_, i) => {
      const active = i < item.rating ? 'active' : '';
      return `<span class="rate-star ${active}" data-value="${i + 1}">&#9733;</span>`;
    }).join('');

    return `
    <a>
      <div class="comment-box">
        <div class="comment-text">${item.comment}</div>
        <div class="starContainer">${stars}</div>
        <div class="comment-meta">
          <span class="comment-author">${item.author}</span>
          <span class="comment-date">${item.date}</span>
        </div>
      </div>
    </a>
    `;
  }).join('');
}

  // 饼图
  charts.forEach(cfg => {
    const dom = document.getElementById(cfg.id);
    if (!dom) return;
    const chart = echarts.init(dom);
    chart.setOption({
      title: { text: cfg.title, left: 'center' },
      tooltip: { trigger: 'item' },
      legend: { bottom: 0 },
      series: [{
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
      }]
    });
  });

  // 缩略图轮播
  let currentIndex = 0;
  const mainImg = document.querySelector('.pic-box .main-slider img');
  const thumbsContainer = document.querySelector('.pic-box .thumbs-container');
  pics.forEach((src, idx) => {
    const wrapper = document.createElement('div');
    wrapper.className = 'thumb-item';
    const img = document.createElement('img');
    img.src = src;
    img.addEventListener('click', () => showImage(idx));
    wrapper.appendChild(img);
    thumbsContainer?.appendChild(wrapper);
  });
  const showImage = idx => {
    if (mainImg && pics[idx]) {
      mainImg.src = pics[idx];
      thumbsContainer?.children[idx]?.scrollIntoView({ behavior: 'smooth', inline: 'center' });
      currentIndex = idx;
    }
  };
  document.querySelector('.thumb-prev')?.addEventListener('click', () => {
    if (currentIndex > 0) showImage(currentIndex - 1);
  });
  document.querySelector('.thumb-next')?.addEventListener('click', () => {
    if (currentIndex < pics.length - 1) showImage(currentIndex + 1);
  });
  showImage(0);

  // 搜索框交互
  const input = document.querySelector('.search-box input');
  const gallery = document.querySelector('.specific-display-box');
  const when_search = document.querySelector('.when-search-box');
  const comments = document.querySelector('.comment-section-box');
  input?.addEventListener('focus', () => {
    gallery.style.display = 'none';
    when_search.style.display = 'block';
    comments.style.display = 'none';
  });
  document.addEventListener('click', e => {
    if (!input?.contains(e.target) && !when_search?.contains(e.target)) {
      gallery.style.display = 'block';
      when_search.style.display = 'none';
      comments.style.display = 'block';
    }
  });

  // 评分滑块
  const container = document.getElementById('ratings-container');
  ratingsData.forEach((r, idx) => {
    const card = document.createElement('div');
    card.className = 'rating-card';
    card.innerHTML = `
      <div class="rating-label">${r.name}</div>
      <div class="d-flex align-items-center">
        <div class="label-left text-muted">${r.left}</div>
        <div id="slider${idx}" class="slider-wrapper"></div>
        <div class="label-right text-muted">${r.right}</div>
      </div>`;
    container?.appendChild(card);
    createSlider(`slider${idx}`, r.score);
  });

  const uploadcontainer = document.getElementById('upload-bar-box');
  ratingsData.forEach((r, idx) => {
    const fieldName = r.name.toLowerCase().replace(/\s+/g, '_');
    const sliderId = `upload-slider-${idx}`;
    const inputId  = `input-${fieldName}`;
    const card = document.createElement('div');
    card.className = 'rating-card';
    card.innerHTML = `
    <div class="rating-label fw-bold">${r.name}</div>
    <div class="d-flex align-items-center">
      <div class="label-left text-muted me-2">${r.left}</div>
      <div id="${sliderId}" class="slider-wrapper flex-grow-1"></div>
      <input type="hidden" name="${fieldName}" id="${inputId}">
      <div class="label-right text-muted ms-2">${r.right}</div>
    </div>
  `;
    uploadcontainer?.appendChild(card);
    creatbar(sliderId, inputId, 2);
  });

  // 地图
  const mapContainer = document.getElementById('spe-map');
  if (mapContainer) {
    const map = L.map('spe-map').setView([metainfo[11], metainfo[12]], 16);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);
    L.marker([metainfo[11], metainfo[12]]).addTo(map).bindPopup('<b>I am here!</b>').openPopup();
  }

  // 点赞列表
const likebox = document.querySelector(".liked-box-content");
if (likebox) {
  likebox.innerHTML = likeData.map(item => `
   <a href="/index/${item.spotid}">
    <div class="liked-box-items" id="${item.spotid}">
      <img src="${item.path}" alt="${item.name.slice(0,10).replaceAll("_", " ")}" class="likedlist-icon" loading="lazy">
      <div class="likedlist-text">${item.name.slice(0, 10).replaceAll("_", " ")}<br><span class="text-muted-sm"></span></div>
      <i class="bi bi-heart-fill liked-heart-icon"></i>
      <i class="bi bi-chat-dots"></i>
    </div> </a>
`).join('');
}

  //用户名称，头像，消息渲染,地点名称加载
const profile_pic = document.querySelector(".profile-box");
const secondP = document.querySelector(".navright-box p:nth-of-type(2)");
const h4Element = document.querySelector(".banner-box .banner-text h4")
const likenum = document.getElementById("index-like-count")
h4Element.textContent = metainfo[10].replaceAll("_", " ");;
likenum.textContent = metainfo[13]
if (profile_pic) {
  profile_pic.src = metainfo[2];
}

if (secondP) {
  secondP.textContent = metainfo[0];
}
// 地点描述
  const distxt = document.querySelector(".spe-decription-box")
  distxt.textContent = metainfo[14]
//like dislike

    const likeBtn = document.getElementById("index-like");
    const dislikeBtn = document.getElementById("index-dislike");
    const likeCount = document.getElementById("index-like-count");

    let liked = false;
    let disliked = false;

    function showFloatNumber(target, text) {
      const floatNum = document.createElement("div");
      floatNum.className = "index-float-number";
      floatNum.textContent = text;
      floatNum.style.left = target.offsetLeft + "px";
      floatNum.style.top = "-20px";
      target.appendChild(floatNum);
      setTimeout(() => {
        target.removeChild(floatNum);
      }, 1000);
    }

    likeBtn.addEventListener("click", () => {
      if (liked) {
        likeCount.textContent = parseInt(likeCount.textContent) - 1;
        likeBtn.classList.remove("index-liked");
        showFloatNumber(likeBtn, "-1");
        liked = false;
      } else {
        likeCount.textContent = parseInt(likeCount.textContent) + 1;
        likeBtn.classList.add("index-liked");
        showFloatNumber(likeBtn, "+1");
        liked = true;
        if (likebox) {
          fetch(`/index/like/${metainfo[1]}`)
          .then(res => res.json())
          .then(likeData => {
          likebox.innerHTML = likeData.map(item => `
        <a href="/index/${item.spotid}">
          <div class="liked-box-items" id="${item.spotid}">
            <img src="${item.path}" alt="${item.name.slice(0,10)}" class="likedlist-icon" loading="lazy">
            <div class="likedlist-text">${item.name.slice(0, 10)}<br><span class="text-muted-sm"></span></div>
            <i class="bi bi-heart-fill liked-heart-icon"></i>
            <i class="bi bi-chat-dots"></i>
          </div>
        </a>
      `).join('');
    })
    .catch(error => console.error("Failed to load liked data:", error));
}
        if (disliked) {
          dislikeBtn.classList.remove("index-disliked");
          disliked = false;
        }
      }
    });

    dislikeBtn.addEventListener("click", () => {
      if (disliked) {
        dislikeBtn.classList.remove("index-disliked");
        disliked = false;
      } else {

        dislikeBtn.classList.add("index-disliked");
        disliked = true;
        const box = document.getElementById(metainfo[1]);
        box.remove();
        fetch(`/index/dislike/${metainfo[1]}`).then(res => { /* … */ });

        if (parseInt(likeCount.textContent) > 0) {
          likeCount.textContent = parseInt(likeCount.textContent) - 1;
          likeBtn.classList.remove("index-liked");
          showFloatNumber(likeBtn, "-1");
          liked = false;
        }
      }
    });


});
