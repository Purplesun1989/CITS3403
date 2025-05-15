document.addEventListener('DOMContentLoaded', () => {
  const input       = document.querySelector('.search-box input');
  const gallery     = document.querySelector('.gallery-box');
  const historyBox  = document.querySelector('.when-search-box');
  const historyList = document.getElementById('history-list');
  const KEY       = 'searchHistory';
  const MAX_COUNT = 10;

  function loadHistory() {
    try {
      const arr = JSON.parse(localStorage.getItem(KEY));
      return Array.isArray(arr) ? arr : [];
    } catch {
      return [];
    }
  }

  function saveHistory(arr) {
    localStorage.setItem(KEY, JSON.stringify(arr));
  }

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
      renderHistory();
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
      // historyBox.style.display = 'none';
      // gallery.style.display    = 'block';
    }


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
      return;
    }
  });

  // 回车时，把当前值加入历史
input.addEventListener('keydown', e => {
  if (e.key === 'Enter') {
    const val = input.value.trim();
    if (!val) return;

    let arr = loadHistory().filter(x => x !== val); // 去重
    arr.unshift(val);                               // 最新排前
    if (arr.length > MAX_COUNT) arr = arr.slice(0, MAX_COUNT);
    saveHistory(arr);

    historyBox.style.display = 'none';

    fetch('/index/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ inputValue: val })
    })
    .then(response => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // 根据后端返回格式决定
    })
    .then(data => {
       if (data.spot_id) {
       window.location.href = `/index/${data.spot_id}`;
     } else {
       alert("No matching spot found.");
    }
})

    .catch(error => {
      alert('Search request failed:', error);
    });
  }
});

});



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


    historyBox.style.display = 'block';
    gallery.style.display = 'none';

    document.querySelector('.filter-buttons').style.display = 'none';

  });
});

  trophy = document.querySelector(".bi-trophy")
  if(trophy){
    trophy.addEventListener('click',()=>{
       window.location.href ='/awards/study'
    })
  }

 var exit = document.querySelector(".bi-box-arrow-right")
  if(exit){
    exit.addEventListener('click',()=>{
       window.location.href ='/exit'
    })
  }


});