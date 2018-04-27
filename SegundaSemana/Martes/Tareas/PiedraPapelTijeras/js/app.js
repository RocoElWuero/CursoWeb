//------------------Funciones------------------
function getRandomInt(min,max)
	{return Math.floor(Math.random()*(max-min))+min;}
//------------------Código------------------
var desici = prompt("Elije algo: PIEDRA, PAPEL o TIJERAS\nEn MAYUSCULAS, porfavor:");

var contrario = getRandomInt(1,4);
if(contrario==1) alert("Contrario: Piedra");
else if(contrario==2) alert("Contrario: Papel");
else if(contrario==3) alert("Contrario: Tijeras");
/*
	1==Piedra
	2==Papel
	3==Tijeras
*/

if(desici=="PIEDRA")
{
	if(contrario==1) alert("Empate :O");
	else if(contrario==2) alert("Valiste Madres :/");
	else alert("Ganaste Prroo!!!");
}
else if(desici=="PAPEL")
{
	if(contrario==1) alert("Ganaste Prroo!!!");
	else if(contrario==2) alert("Empate :O");
	else alert("Valiste Madres :/");
}
else if(desici=="TIJERAS")
{
	if(contrario==1) alert("Valiste Madres :/");
	else if(contrario==2) alert("Ganaste Prroo!!!");
	else alert("Empate :O");
}