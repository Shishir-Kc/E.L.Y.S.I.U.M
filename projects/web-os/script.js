function updateClock() {
    const now = new Date();
    document.getElementById('clock').innerText = now.toLocaleTimeString();
}
setInterval(updateClock, 1000);
updateClock();

const startBtn = document.getElementById('start-btn');
const startMenu = document.getElementById('start-menu');

startBtn.onclick = () => {
    startMenu.classList.toggle('hidden');
};

function changeWallpaper(url) {
    document.getElementById('desktop').style.backgroundImage = `url('${url}')`;
    startMenu.classList.add('hidden');
}

function openApp(appId) {
    const container = document.getElementById('window-container');
    
    // Avoid opening multiple instances of the same app for this demo
    if (document.getElementById(`win-${appId}`)) return;

    const win = document.createElement('div');
    win.id = `win-${appId}`;
    win.className = 'window';
    win.style.top = '100px';
    win.style.left = '100px';

    let contentHtml = '';
    let title = '';

    if (appId === 'settings') {
        title = 'Settings';
        contentHtml = `
            <div style="padding: 20px; text-align: center;">
                <h3>OS Settings</h3>
                <p>Change your wallpaper from the Start Menu!</p>
                <input type="text" id="wall-url" placeholder="Enter Image URL" style="width: 80%; padding: 10px;">
                <button onclick="applyCustomWallpaper()" style="padding: 10px 20px; margin-top: 10px;">Apply</button>
            </div>
        `;
    } else {
        title = appId.charAt(0).toUpperCase() + appId.slice(1);
        // Games are hosted in separate files in the game dir
        const gamePath = appId === 'surprise' ? '../game dir/surprise/index.html' : `../game dir/${appId}/index.html`;
        contentHtml = `<iframe src="${gamePath}"></iframe>`;
    }

    win.innerHTML = `
        <div class="window-header">
            <div class="window-title">${title}</div>
            <div class="window-controls">
                <button class="close-btn" onclick="closeApp('${appId}')">X</button>
            </div>
        </div>
        <div class="window-content">${contentHtml}</div>
    `;

    container.appendChild(win);
    makeDraggable(win);
}

function closeApp(appId) {
    const win = document.getElementById(`win-${appId}`);
    if (win) win.remove();
}

function applyCustomWallpaper() {
    const url = document.getElementById('wall-url').value;
    if (url) {
        changeWallpaper(url);
    }
}

function makeDraggable(elmnt) {
    let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    const header = elmnt.querySelector('.window-header');
    
    header.onmousedown = dragMouseDown;

    function dragMouseDown(e) {
        e.preventDefault();
        pos3 = e.clientX;
        pos4 = e.clientY;
        document.onmouseup = closeDragElement;
        document.onmousemove = elementDrag;
        // Bring to front
        document.querySelectorAll('.window').forEach(w => w.style.zIndex = 1);
        elmnt.style.zIndex = 10;
    }

    function elementDrag(e) {
        e.preventDefault();
        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;
        elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
        elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
    }

    function closeDragElement() {
        document.onmouseup = null;
        document.onmousemove = null;
    }
}
