document.addEventListener('DOMContentLoaded', () => {
  const input       = document.querySelector('.search-box input');
  const gallery     = document.querySelector('.gallery-box');
  const historyBox  = document.querySelector('.when-search-box');
  const historyList = document.getElementById('history-list');

  const KEY       = 'searchHistory';  // localStorage 键
  const MAX_COUNT = 10;               // 最多保留几条

  // 读取历史，返回数组
  function loadHistory() {
    try {
      const arr = JSON.parse(localStorage.getItem(KEY));
      return Array.isArray(arr) ? arr : [];
    } catch {
      return [];
    }
  }

  // 存储历史
  function saveHistory(arr) {
    localStorage.setItem(KEY, JSON.stringify(arr));
  }

  // 根据 filter 渲染 list
  function renderHistory(filter = '') {
    const hist = loadHistory()
      .filter(item => item.includes(filter));
    historyList.innerHTML = '';

    if (hist.length === 0) {
      historyList.innerHTML = '<li class="no-history" style="padding:8px 12px;color:#888">No search history</li>';
      return;
    }

    hist.forEach((text, idx) => {
      const li = document.createElement('li');
      li.className = 'history-item';
      li.innerHTML = `
        <span>
          <span class="icon">⏱</span>
          <span class="text">${text}</span>
        </span>
        <button class="remove-hist" data-index="${idx}">Remove</button>
      `;
      historyList.appendChild(li);
    });
    historyBox.style.display = 'block';
    gallery.style.display    = 'none';
  }

  function searchAcrossCategories(query) {
    const lowerQuery = query.toLowerCase();
    let results = [];
  
    for (const [category, items] of Object.entries(dataByCategory)) {
      const matchedItems = items.filter(item =>
        item.name.toLowerCase().includes(lowerQuery)
      );
      results = results.concat(matchedItems);
    }
  
    return results;
  };

  input.addEventListener('input', () => {
    const query = input.value.trim().toLowerCase();
  
    if (query === '') {
      renderHistory(); // ✅ Only show history if input is empty
      document.querySelector('.filter-buttons').style.display = 'flex';
      return;
    }
  
    const results = searchAcrossCategories(query);
    const historyList = document.getElementById('history-list');
    const historyBox  = document.querySelector('.when-search-box');
    const gallery     = document.querySelector('.gallery-box');
  
    historyList.innerHTML = '';
  
    if (results.length === 0) {
      historyList.innerHTML = '<li class="no-history" style="padding:8px 12px;color:#888">No results found</li>';
    } else {
      results.forEach(item => {
        const li = document.createElement('li');
        li.className = 'history-item';
        li.innerHTML = `<a href="${item.link}">${item.name}</a>`;
        historyList.appendChild(li);
      });
    }
  
    historyBox.style.display = 'block';
    gallery.style.display = 'none';
    document.querySelector('.filter-buttons').style.display = 'none';
  });
  
  input.addEventListener('focus', () => {
    renderHistory(input.value.trim());
    document.querySelector('.filter-buttons').style.display = 'flex'; // or 'block' depending on your layout
  });

  // 全局点击，点击输入框或历史列表外时隐藏
  document.addEventListener('click', e => {
    if (!input.contains(e.target) && !historyBox.contains(e.target)) {
      historyBox.style.display = 'none';
      gallery.style.display    = 'block';
    }

  // 历史列表内点击：选中 vs 删除
  historyList.addEventListener('click', e => {
    const btn = e.target.closest('.remove-hist');
    if (btn) {
      // 删除历史
      const idx = +btn.dataset.index;
      const arr = loadHistory();
      arr.splice(idx, 1);
      saveHistory(arr);
      renderHistory(input.value.trim());
      return;
    }
    const item = e.target.closest('.history-item');
    if (item) {
      // 选中历史，填入输入框，并隐藏
      const text = item.querySelector('.text').textContent;
      input.value = text;
      historyBox.style.display = 'none';
      gallery.style.display    = 'block';
      // TODO: 这里可以触发真正的搜索请求
      return;
    }
  });

  // 回车时，把当前值加入历史
  input.addEventListener('keydown', e => {
    if (e.key === 'Enter') {
      const val = input.value.trim();
      if (!val) return;
      let arr = loadHistory()
        .filter(x => x !== val);  // 去重
      arr.unshift(val);           // 最新排前
      if (arr.length > MAX_COUNT) arr = arr.slice(0, MAX_COUNT);
      saveHistory(arr);
      historyBox.style.display = 'none';
      gallery.style.display    = 'block';
      // TODO: 这里发起你的搜索逻辑
    }
  });
});

const dataByCategory = {
  'study-spot': [
    { name: 'Reid Library', link: '/reid-library.html' },
    { name: 'Law Library', link: '/law-library.html' },
    { name: 'Business School', link: '/business-school.html' },
    { name: 'Barry J Library', link: '/barry-j-library.html' },
    { name: 'EZONE', link: '/ezone.html' }
  ],
  'food-places': [
    { name: 'Refectory', link: '/refectory.html' },
    { name: 'UWA Tavern', link: '/uwa-tavern.html' },
    { name: 'IGA', link: '/iga.html' },
    { name: 'Hackett Cafe', link: '/hackett-cafe.html' }
  ],
  'units': [
    { name: 'CITS3403', link: '/cits3403.html' },
    { name: 'CITS3400', link: '/cits3400.html' },
    { name: 'CITS2429', link: '/cits2429.html' },
    { name: 'CITS3592', link: '/cits3592.html' }
  ],
  'events': [
    { name: 'O-Day', link: '/oday.html' },
    { name: 'Open Day', link: '/open-day.html' },
    { name: 'Autumn Feast', link: '/autumn-feast.html' },
    { name: 'Spring Feast', link: '/spring-feast.html' },
    { name: 'PROSH', link: '/prosh.html' }
  ],
  'organizations': [
    { name: 'Robotics Club', link: '/robotics-club.html' },
    { name: 'Sober?', link: '/sober.html' },
    { name: 'Coders for Cause', link: '/coders-for-cause.html' },
    { name: 'Data Science Club', link: '/data-science-club.html' },
    { name: 'Computer Science Society', link: '/css.html' }
  ]
};

document.querySelectorAll('.filter-btn').forEach(button => {
  button.addEventListener('click', () => {
    const category = button.dataset.category;
    const data = dataByCategory[category];
    const historyList = document.getElementById('history-list');
    const historyBox = document.querySelector('.when-search-box');  // reselect if not in outer scope
    const gallery = document.querySelector('.gallery-box');         // reselect if needed

    if (!data) return;

    historyList.innerHTML = '';
    data.forEach(item => {
      const li = document.createElement('li');
      li.className = 'history-item';
      li.innerHTML = `<a href="${item.link}">${item.name}</a>`;
      historyList.appendChild(li);
    });

    // SHOW the box after filtering
    historyBox.style.display = 'block';
    gallery.style.display = 'none';

    document.querySelector('.filter-buttons').style.display = 'none';

  });
});
});