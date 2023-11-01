const toggleButton = document.getElementById('toggle-button');
const body = document.body;
const header = document.header;

const darkMode = localStorage.getItem('darkMode');

if (darkMode) {
    body, header.classList.add('dark-mode');
}

toggleButton.onclick = function() {
    body, header.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', body, header.classList.contains('dark-mode'));
}