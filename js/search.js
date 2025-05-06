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
      historyList.innerHTML = '<li class="no-history" style="padding:8px 12px;color:#888">暂无搜索记录</li>';
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
        <button class="remove-hist" data-index="${idx}">移除</button>
      `;
      historyList.appendChild(li);
    });
    historyBox.style.display = 'block';
    gallery.style.display    = 'none';
  }

  // 聚焦和输入时，渲染并显示历史
  input.addEventListener('focus', ()   => renderHistory(input.value.trim()));
  input.addEventListener('input', ()   => renderHistory(input.value.trim()));

  // 全局点击，点击输入框或历史列表外时隐藏
  document.addEventListener('click', e => {
    if (!input.contains(e.target) && !historyBox.contains(e.target)) {
      historyBox.style.display = 'none';
      gallery.style.display    = 'block';
    }
  });

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
