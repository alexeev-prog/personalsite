const burger = document.querySelector(".burger");
const menu = document.querySelector(".top__menu");

burger.onclick = function() {
	burger.classList.toggle("closed");
	menu.classList.toggle("opened");
};


window.addEventListener('scroll', function() {
	const header = document.getElementById('header');

	if (window.scrollY > 50) {
		header.classList.add('scroll-header');
	} else {
		header.classList.remove('scroll-header');
	}
})