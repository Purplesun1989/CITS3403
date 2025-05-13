const findBox = document.getElementById("find");
const searchInput = document.getElementById("searchInput");

// 渲染用户卡片
function renderUsers(filteredUsers) {
  findBox.innerHTML = "";
  filteredUsers.forEach(user => {
    const div = document.createElement("div");
    div.className = "friendcard d-flex align-items-center mb-2";

    div.innerHTML = `
      <img src="${user.path}" alt="${user.name}" class="rounded-circle me-2" width="30" height="30">
      <span class="friend-name">${user.name}</span>
      <input type="text" value="Hi, let's be friends!" class="msg-input w-75 ms-2">
      <i class="bi bi-send-fill action-icon text-success ms-2" style="cursor:pointer;"></i>
    `;

    const input = div.querySelector(".msg-input");
    const sendIcon = div.querySelector(".bi-send-fill");

    sendIcon.addEventListener("click", () => {
      const message = input.value;
      fetch(`/profile/enlistfriend/${user.uid}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
      }).then(res => {
        if (res.status === 204) {
          sendIcon.classList.remove("bi-send-fill");
          sendIcon.classList.add("bi-check-circle");
          sendIcon.style.color = "gray";
          input.disabled = true;
        } else {
          console.warn("failed：" + res.status);
        }
      }).catch(err => {
        console.error("network fai：", err);
      });
    });

    findBox.appendChild(div);
  });
}


document.addEventListener('DOMContentLoaded', async () => {

  const wallpaperImg = document.querySelector(".wall-paper-box img");
  if (wallpaperImg) {
    wallpaperImg.src = user[2];
  }


  const avatarImg = document.querySelector(".profile-box img");
  if (avatarImg) {
    avatarImg.src = user[1];
  }


  const container = document.getElementById("friends");
  friend.forEach(item => {
    const div = document.createElement("div");
    div.className = "friendcard d-flex align-items-center";
    div.dataset.uid = item.uid
    div.innerHTML = `
      <img src="${item.path}" alt="avatar" class="friend-avatar">
      <span class="friend-name">${item.name}</span>
      <i class="bi bi-x-circle action-icon"></i>
    `;
    const decline = div.querySelector(".bi-x-circle");
    decline.addEventListener("click", () => {
      fetch(`/profile/remove/${item.uid}`, {
        method: "GET",
     })
      .then(res => {
      if (res.ok) {
      div.remove();
      } else {
      alert("failed", res.status);
    }
    })
      .catch(err => {
    console.error("failed", err);
     });
    });
    container.appendChild(div);

  });


  // 渲染好友请求
const requestContainer = document.getElementById("requests");

newrequest.forEach(item => {
  const div = document.createElement("div");
  div.className = "friendcard d-flex align-items-center";

  div.innerHTML = `
    <img src="${item.path}" alt="avatar" class="friend-avatar">
    <span class="friend-name">${item.name} : ${item.message}</span>
    <i class="bi bi-check-circle action-icon text-success" style="cursor:pointer;"></i>
    <i class="bi bi-x-circle action-icon" style="cursor:pointer;"></i>
  `;

  const acceptIcon = div.querySelector(".bi-check-circle");
  const rejectIcon = div.querySelector(".bi-x-circle");

  // 点击确认请求
acceptIcon.addEventListener("click", async () => {
  try {
    // 1. 发起 GET 请求
    const res = await fetch(`/profile/confirm/${item.uid}`);
    if (!res.ok) throw new Error(`networks errors：${res.status}`);

    // 2. 解析成 JS 数组
    const users = await res.json();


    // 3. 找到当前点击对应的那条记录
    const uidNum = Number(item.uid);
    const me = users.find(u => u.uid === uidNum);
    if (!me) {
      console.warn("no user uid =", uidNum);
      return;
    }


    const { uid, name, path } = me;
    const container = document.getElementById("friends");
    const friendDiv = document.createElement("div");
    friendDiv.className = "friendcard d-flex align-items-center";
    friendDiv.dataset.uid = uid;
    friendDiv.innerHTML = `
      <img src="${path}" alt="avatar" class="friend-avatar">
      <span class="friend-name">${name}</span>
      <i class="bi bi-x-circle action-icon" style="cursor:pointer;"></i>
    `;
    friendDiv
      .querySelector(".action-icon")
      .addEventListener("click", () => friendDiv.remove());
    container.appendChild(friendDiv);


    div.remove();

  } catch (err) {
    console.error("failed：", err);
  }
});


  rejectIcon.addEventListener("click", () => {
    fetch(`/profile/decline/${item.uid}`)
    div.remove();
  });
  requestContainer.appendChild(div);
});


  renderUsers(allUsers);

  searchInput.addEventListener("input", () => {
    const keyword = searchInput.value.toLowerCase();
    const filtered = allUsers.filter(user => user.name.toLowerCase().includes(keyword));
    renderUsers(filtered);
  });
});
