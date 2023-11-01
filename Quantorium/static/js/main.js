const toggleButton = document.getElementById('toggle-button');
const body = document.body;

const darkMode = localStorage.getItem('darkMode');

if (darkMode) {
    body.classList.add('dark-mode');
}

toggleButton.onclick = function() {
    body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', body.classList.contains('dark-mode'));
}