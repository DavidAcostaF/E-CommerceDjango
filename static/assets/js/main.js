let $ = jQuery.noConflict();

jQuery(document).ready(function($) {

	"use strict";

	[].slice.call( document.querySelectorAll( 'select.cs-select' ) ).forEach( function(el) {
		new SelectFx(el);
	});

	jQuery('.selectpicker').selectpicker;


	

	$('.search-trigger').on('click', function(event) {
		event.preventDefault();
		event.stopPropagation();
		$('.search-trigger').parent('.header-left').addClass('open');
	});

	$('.search-close').on('click', function(event) {
		event.preventDefault();
		event.stopPropagation();
		$('.search-trigger').parent('.header-left').removeClass('open');
	});

	$('.equal-height').matchHeight({
		property: 'max-height'
	});

	// var chartsheight = $('.flotRealtime2').height();
	// $('.traffic-chart').css('height', chartsheight-122);


	// Counter Number
	$('.count').each(function () {
		$(this).prop('Counter',0).animate({
			Counter: $(this).text()
		}, {
			duration: 3000,
			easing: 'swing',
			step: function (now) {
				$(this).text(Math.ceil(now));
			}
		});
	});


	 
	 
	// Menu Trigger
	$('#menuToggle').on('click', function(event) {
		var windowWidth = $(window).width();   		 
		if (windowWidth<1010) { 
			$('body').removeClass('open'); 
			if (windowWidth<760){ 
				$('#left-panel').slideToggle(); 
			} else {
				$('#left-panel').toggleClass('open-menu');  
			} 
		} else {
			$('body').toggleClass('open');
			$('#left-panel').removeClass('open-menu');  
		} 
			 
	}); 

	 
	$(".menu-item-has-children.dropdown").each(function() {
		$(this).on('click', function() {
			var $temp_text = $(this).children('.dropdown-toggle').html();
			$(this).children('.sub-menu').prepend('<li class="subtitle">' + $temp_text + '</li>'); 
		});
	});


	// Load Resize 
	$(window).on("load resize", function(event) { 
		var windowWidth = $(window).width();  		 
		if (windowWidth<1010) {
			$('body').addClass('small-device'); 
		} else {
			$('body').removeClass('small-device');  
		} 
		
	});
  
 
});

function abrirModalEdicion(url){
$('#edicion').load(url,function(){
	$(this).modal('show');
});
}

function abrirModalCreacion(url){
$('#creacion').load(url,function(){
	$(this).modal('show');
});
}
function abrirModalEliminacion(url){
	$('#eliminacion').load(url,function(){
		$(this).modal('show');
	});
	}
function cerrar_modal_creacion(){
	$('#creacion').modal('hide');
}
function cerrar_modal_edicion(){
	$('#edicion').modal('hide');
}

function cerrar_modal_eliminacion(){
	$('#eliminacion').modal('hide');
}

function activarBoton(){
	if($('#boton_creacion').prop('disabled')){
		$('#boton_creacion').prop('disabled',false);
	}else{
		$('#boton_creacion').prop('disabled',true)
	}
}

function mostrarErroresCreacion(errores){
	$('#errores').html("");
	let error = "";
	for(let item in errores.responseJSON.error){
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errores').append(error);
}

function mostrarErroresEdicion(errores){
	$('#erroresEdicion').html("");
	let error = "";
	for(let item in errores.responseJSON.error){
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errores').append(error);
}

function notificacionError(mensaje){
	Swal.fire({
		title: 'Error!',
		text:mensaje,
		icon:'error'
	})
}

function notificacionSuccess(mensaje){
	Swal.fire({
		title: 'Buen Trabajo!',
		text:mensaje,
		icon:'success'
	})
}


// function cargarProductos(){
// 	$.ajax({
// 		url:'/lista_productos/',
// 		method:'get',
// 		dataType:'json',
// 		success:function(response){
// 			let listaProducto = document.querySelector('#listaProductos')
// 			for(let i = 0;i<response.length;i++){
//                 let fila = '<section class="col m-3">';
//                 fila +='<label>' + (i+1) + '</label>'
// 				//fila +='<div class="col">';
//                 fila +=`<img class="img-fluid rounded mx-auto" style="width:200px; height:200px;" src="${window.location.origin+"/"+response[i]["fields"]["imagen"]}">`;
// 				fila += '<br>';
//                 fila +='<label>' + response[i]["fields"]['nombre'] + '</label>';//[i]["fields"]["imagen"]
// 				fila += '<br>';
//                 fila +='<label>' + response[i]["fields"]['descripcion'] + '</label>';
// 				fila += '<br>';
//                 fila +='<label>' + response[i]["fields"]['costo'] + '</label>';
// 				fila += '<br>';
//                 fila +='<td><button type="button" class="btn btn-primary btn-sm tableButton"';
//                 fila += 'onclick="abrirModalEdicion(\'/usuarios/actualizar_usuario/'+response[i]['pk']+'/\');"> EDITAR </button>';
//                 fila += '<button type="button" class="btn btn-danger btn-sm tableButton"';
//                 fila += 'onclick="abrirModalEliminacion(\'/usuarios/eliminar_usuario/'+response[i]['pk']+'/\');"> ELIMINAR </button></td>';
//                 //fila +='</div>';
// 				fila +='</section>';
//                 $('#productos_columna').append(fila);
// 			//	listaProducto.innerHTML =`<section>
// 			// 	<div>
// 			// 		<img src="${producto.fields.imagen}">
// 			// 		<label>${producto.fields.nombre}</label><br>
// 			// 		<label>${producto.fields.descripcion}</label><br>
// 			// 		<label>${producto.fields.costo}</label>
// 			// 	</div>
// 			// </section>`
// 			// listaProducto.append(producto.fields.nombre) 
//             }
// 			console.log(response)
// 		},
// 		error:function(error){
// 			console.log(error)
// 		}
// 	})
// }

// window.addEventListener('load',cargarProductos())






// function agregarAlCarrito(){
// 	console.log('{{user.username}}')
// 	$.ajax({
// 		url:'/agregar_carrito/',
// 		method:'post'
// 	})
// }


window.addEventListener('load',carrito())
function carrito(){
	$.ajax({
		url:"/carrito/",
		method:'GET',
        dataType:'json',
		success:function(cuenta){
			document.querySelector(".contador").textContent = cuenta.length
		},
        error:function(error){
        console.log(error)
        }
	})
}

function comprar(){
	let productos = document.querySelectorAll('.carrito')
	productos.forEach(e=>{
		let producto = e.querySelector('.producto').textContent
		let cantidad = e.querySelector('.cantidad').textContent
		console.log("pruducto: "+ producto,"cantidad: " +cantidad)
		$.ajax({
			url:"/carrito/",
			method:'POST',
			data:{csrfmiddlewaretoken:$("[name = 'csrfmiddlewaretoken']").val(),'producto':producto,'cantidad':cantidad}
		})
		console.log("paso el ajax")
	})
}

function confirmacionCompra(){
	Swal.fire({
		title: '¿Deseas comprarlo?',
		text: "You won't be able to revert this!",
		icon: 'warning',
		showCancelButton: true,
		confirmButtonColor: '#3085d6',
		cancelButtonColor: '#d33',
		confirmButtonText: 'Si, comprarlo!'
	  }).then((result) => {
		if (result.isConfirmed) {
			$.ajax({
				url:"/comprar_productos/",
				success:function(){
					window.location.replace("/");
				}
			})
		  Swal.fire(
			'Confirmado!',
			'Se he comprado correctamente.',
			'success'
		  )
		}
	  })
}
