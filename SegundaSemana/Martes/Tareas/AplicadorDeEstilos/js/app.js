function color()
{
	var estilo = document.getElementById("cambio");
	var texto = console.log(estilo.innerHTML);
	alert(texto);
/*
La siguiente cadena (string) se muestra en la ventana de la consola:
<p>primer parrafo hijo de div id="txt"</p> 
<p>segundo parrafo hijo de id="txt" txt</p>
*/


	stripHtmlTags (estilo);
	document.getElementById('id').style.backgroundColor=estilo;

//	<a href="javascript:void(document.getElementById('id').style.backgroundColor='yellow')">Cambia el color del fondo de esta sección</a>

//	document.getElementById("id").style.backgroundColor = document.getElementById("id");
//	alert(estilo);

//	javascript:void(document.getElementById("id").style.backgroundColor=estilo);

//	var x = document.getElementById("cambio");
//	document.body.style.fontSize=estilo+"px"
//	document.getElementById("id").style.property="value"

//	x.value = x.value.toUpperCase(); //Convierte a Mayusculas
}