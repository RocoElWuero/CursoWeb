/*
$(elemento).ready(function(){
	
})
*/
$(document).ready(function(){
	$("#iraarticulo1").click(function(){
		var posicion = $("#articulo2").offset().top;
		//$("algo").animate({
		//que quiero que haga
		//},tiempoenmiliseg.quehagodespues);
		$("html,body").animate({
			scrollTop : posicion
		},2000)
	});
	$(".btn1").click(function(){
		$(".img-responsive").fadeOut();
	});
	$(".btn2").click(function(){
		$(".img-responsive").fadeIn();
	});
	$("#articulo2")
	.mouseenter(function(){
		$("#articulo2").addClass("cambialetra")
	})
	.mouseout(function(){
		$("#articulo2").removeClass("cambialetra")
	})
})