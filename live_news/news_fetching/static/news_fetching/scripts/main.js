// function showNews(type) {
//     const sections = {
//         all: document.getElementById('all'),
//         trending: document.getElementById('trending'),
//         sports:document.getElementById('sports'),
//         science:document.getElementById('science'),
//     };

//     const buttons = {
//         all: document.getElementById('btn-all'),
//         trending: document.getElementById('btn-trending'),
//         sports:document.getElementById('btn-sports'),
//         science:document.getElementById('btn-science'),

//     };

//     // Show the selected section and hide the other
//     Object.keys(sections).forEach(key => {
//         sections[key].style.display = (key === type) ? 'block' : 'none';
//     });

//     // Toggle the active class on buttons
//     Object.keys(buttons).forEach(key => {
//         buttons[key].classList.toggle('w3-black', key === type);
//         buttons[key].classList.toggle('w3-white', key !== type);
//     });
// }

// Script to open and close sidebar



// // Show 'all' news on page load
// window.onload = () => showNews('all');


