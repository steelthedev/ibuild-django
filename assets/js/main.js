
$(document).ready(function() {

//nav-bar

$(".fa-bars").on("click",function(){

$(".sidebar").toggleClass('show');



});

$(".nav-button").on("click",function(){

$("nav").toggleClass('bar');



});



$(window).on("scroll",function(){


if($(window).scrollTop()){

$('nav').addClass('blue');
}

else{

$('nav').removeClass('blue');

}




});


$('.owl-carousel').owlCarousel({
margin: 20,
autoplay: true,
autoplayTimeout: 4000,
autoplayHoverPause: true,
responsive: {
0: {
items: 1,
}
}
	
});

$('nav a').on("click", function() {
		$('nav ul').collapse('hide');
		
		
	});



});
