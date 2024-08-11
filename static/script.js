(function ($) {
	'use strict';

	// Bulma CSS Config
	$(".navbar-burger").click(function () {
		$(".navbar-burger").toggleClass("is-active");
		$(".navbar-menu").toggleClass("is-active");
	});

	$(".dropdown").click(function(event) {
		event.stopPropagation();
		dropdown.toggleClass('is-active');
	});

	// Sticky Menu
	$(window).scroll(function () {
		if ($('.navbar').offset().top > 100) {
			$('.navbar').addClass('nav-bg');
		} else {
			$('.navbar').removeClass('nav-bg');
		}
	});

	var typed = new Typed(".auto-typed", {
		strings: ["Software Developer", "Competitive Programmer", "Video Editor"],
		typeSpeed: 100,
		backSpeed: 100,
		smartBackspace: true,
		loop: true
	});

	// Background-images
	$('[data-background]').each(function () {
		$(this).css({
			'background-image': 'url(' + $(this).data('background') + ')'
		});
	});

	// background color
	$('[data-color]').each(function () {
		$(this).css({
			'background-color': $(this).data('color')
		});
	});

	// progress bar
	$('[data-progress]').each(function () {
		$(this).css({
			'bottom': $(this).data('progress')
		});
	});


	var lastMouseX = 0;
	var lastMouseY = 0;
	$('.hero-area').mousemove(function(e) {
		// Determine direction by comparing current mouse position with last position
		var moveLeft = e.pageX < lastMouseX;
		var moveUp = e.pageY < lastMouseY;
		lastMouseX = e.pageX;
		lastMouseY = e.pageY;
	
		// Calculate translation values
		var translateX = moveLeft ? 10 : -10; // Move right if moving left, else move left
		var translateY = moveUp ? 10 : -10; // Move down if moving up, else move up
	
		// Apply movement to the opposite direction
		$('.hero-img-wrap').css('transform', `translate(${translateX}px, ${translateY}px)`);
	});
	
	$('.hero-area').mouseleave(function() {
		// Reset position when mouse leaves the area
		$('.hero-img-wrap').css('transform', 'translate(0, 0)');
	});

	// testimonial-slider
	$('.testimonial-slider').slick({
		dots: true,
		infinite: true,
		speed: 300,
		slidesToShow: 1,
		arrows: false,
		adaptiveHeight: true
	});


	// clients logo slider
	$('.client-logo-slider').slick({
		infinite: true,
		slidesToShow: 5,
		slidesToScroll: 1,
		autoplay: true,
		dots: false,
		arrows: false,
		responsive: [{
				breakpoint: 1024,
				settings: {
					slidesToShow: 3,
					slidesToScroll: 1
				}
			},
			{
				breakpoint: 600,
				settings: {
					slidesToShow: 3,
					slidesToScroll: 1
				}
			},
			{
				breakpoint: 480,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 1
				}
			},
			{
				breakpoint: 400,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1
				}
			}
		]
	});

	// Shuffle js filter and masonry
	var Shuffle = window.Shuffle;
	var jQuery = window.jQuery;

	var myShuffle = new Shuffle(document.querySelector('.shuffle-wrapper'), {
		itemSelector: '.shuffle-item',
		buffer: 1
	});

	jQuery('input[name="shuffle-filter"]').on('change', function (evt) {
		var input = evt.currentTarget;
		if (input.checked) {
			myShuffle.filter(input.value);
		}
	});


	// Check for click events on the navbar burger icon
	$(".filter-menu .button").click(function () {
		$(this).addClass("is-active").siblings().removeClass('is-active');
	});

	ScrollReveal().reveal('.section', {delay: 200, interval: 50});
	ScrollReveal().reveal('#skills .card', {delay: 200, reset: true, interval: 100});
	ScrollReveal().reveal('#education .card', {delay: 50, reset: true, interval: 50});
	ScrollReveal().reveal('#portfolio .card', {delay: 200, interval: 50});
	ScrollReveal().reveal('.list-hero-social a', {reset: true, interval: 20});
	ScrollReveal().reveal('.about-text span', {delay:200, reset: true, interval: 200});

	$(document).ready(function(){
		$('a').on('click', function(event) {
		  if (this.hash !== "") {
			event.preventDefault();
			var hash = this.hash;
			$('html, body').animate({
			  scrollTop: $(hash).offset().top
			}, 800, function(){
			  window.location.hash = hash;
			});
		  }
		});
	  });

})(jQuery);