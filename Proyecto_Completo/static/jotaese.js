function sign(idUser){
	var url=window.location.href;
	var res = url.split("/");
	if (res[res.length - 2] == "mezclador"){
		muestra = idUser;
	} else {
		muestra = res[res.length - 1];
	}
	var l=""; 
	if(idUser=='None'){
		l="<li><a href=\"http://mixcrowddb.sytes.net:5000/signpag\"><span class=\"glyphicon glyphicon-log-in\"></span> Sign</a></li>";
	}
	else{
		l="<li><a href=\"http://mixcrowddb.sytes.net:5000/mostrar_user/"+idUser+"\">"+muestra+"</a></li>";	
	}
	document.getElementById("sign").innerHTML = l;
}


function studio(idUser){
	var l="";
	if(idUser!='None'){
		l="<a href=\"http://mixcrowddb.sytes.net:5000/index2/"+idUser+"\">STUDIO</a>";
	}
	document.getElementById("kulunguele").innerHTML = l;
}

function loadCar(idUser){
	studio(idUser)
	sign(idUser)
}

function loadConf(idUser){
	studio(idUser)
	config(idUser)
}

function cargarResultados(idUser){
	debugger;
	var xmlhttp = new XMLHttpRequest();
	var x = document.getElementById("buscador");
	var search1 = x.value;
	xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var myArr=JSON.parse(this.responseText);
      myFunction2(myArr,idUser);
    }
  };
  xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/getSearch/"+search1+"/"+idUser, true);
  xmlhttp.send(search1,idUser);
}

function myFunction2(xml,idUser){

  var list_total="<h2>Search Results</h2>";
  for(i=0;i<xml.length;i++){
  	var nombre = xml[i][0]
  	var descp = xml[i][1]
  	var img = xml[i][2]
  	var user = xml[i][3]
	var list="<a href=\"http://mixcrowddb.sytes.net:5000/mezclador/"+nombre.split(" ")[0]+"_"+idUser+"\" class=\"list-group-item\">"+
	"<img src=\""+img+"\" alt=\"No hay imagen\">"+
	"<h4>"+nombre+"</h4>"+
	"<h5>"+descp+"</h5>"+
	"</a>";
	list_total=list_total+list;
   }
  document.getElementById("busquedaResul").innerHTML = list_total;
}

function cargarUser(idUser){
	debugger;
	var xmlhttp = new XMLHttpRequest();
	var x = document.getElementById("buscador_user");
	var search1 = x.value;
	xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var myArr=JSON.parse(this.responseText);
      myFunction2U(myArr,idUser);
    }
  };
  xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/getSearchUser/"+search1+"/"+idUser, true);
  xmlhttp.send(search1,idUser);
}

function myFunction2U(xml,idUser){
	debugger;
    var list_total="<h2>Search Results</h2>";
    for(i=0;i<xml.length;i++){
  	var nombre = xml[i][0]
  	var email = xml[i][1]
	var list="<a class=\"list-group-item\">"+
	"<img src=\"https://www.shareicon.net/data/128x128/2017/02/09/878597_user_512x512.png\" alt=\"No hay imagen\">"+
	"<h4>"+nombre+"</h4>"+
	"<h5>"+email+"</h5>"+
	"</a>";
	list_total=list_total+list;
   }
  document.getElementById("busquedaResul").innerHTML = list_total;
}

function cargarColl(idUser){
	debugger;
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var myArr=JSON.parse(this.responseText);
      myFunction2C(myArr,idUser);
    }
  };
  xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/getSearchUser/"+idUser, true);
  xmlhttp.send(idUser);
}

function myFunction2C(xml,idUser){
	debugger;
    var list_total="<h2>Search Results</h2>";
    for(i=0;i<xml.length;i++){
  	var nombre = xml[i][0]
  	var email = xml[i][1]
	var list="<a class=\"list-group-item\">"+
	"<img src=\"https://www.shareicon.net/data/128x128/2017/02/09/878597_user_512x512.png\" alt=\"No hay imagen\">"+
	"<h4>"+nombre+"</h4>"+
	"<h5>"+email+"</h5>"+
	"</a>";
	list_total=list_total+list;
   }
  document.getElementById("busquedaResul").innerHTML = list_total;
}

function activarMezclador(name,idUser){
	debugger;
	var checkedValue = "";
	var elements = document.getElementsByClassName("chequed");
	var formData = new FormData();
	var resultado = [];
	var instante = [];
	var panning = [];
	var indicie = 0;
	var id;
	for (var i=0; i<elements.length; i++){
		if(elements[i].checked){
			id = elements[i].id.split("_")[0];
			checkedValue = elements[i].value.split(" ")[0];
			resultado[indicie]=checkedValue;
			instante[indicie] = document.getElementById(id+"_inst").value;
			panning[indicie] = document.getElementById(id+"_pan").value;
			indicie++;
		}
	}
	//var lista = JSON.stringify(elements);

  	formData.append("lista", resultado);
  	formData.append("proyecto", name.split(" ")[0]);
  	formData.append("instante", instante);
  	formData.append("panning", panning);
	var xmlhttp = new XMLHttpRequest();
	window.alert("Wait until the player is refreshed... (It will show a confirmation message when it finished, clcik accept to continue)");
	xmlhttp.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) {
      var info=this.responseText;
      debugger;
      loadPlay(info);
      }
     };
  xmlhttp.open("POST", "http://mixcrowddb.sytes.net:5000/mezclar_todo/", true);
  xmlhttp.send(formData);
}

function loadPlay(src){
	document.getElementById("subReproductor").remove();
	debugger;
	var lista="<audio controls id=\"subReproductor\">"+
      "<source src=\"http://mixcrowddb.sytes.net:5000/"+src+"\" type=\"audio/mpeg\">"+
    "</audio>";
    document.getElementById("reproductor_bueno").innerHTML = lista;	
    window.alert("Audio processed correctly");
}




function config(idUser){
    debugger;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var myArr=JSON.parse(this.responseText);
      myFunctionC(myArr,idUser);
    }
  };
  xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/info_u/"+idUser, true);
  xmlhttp.send(idUser);
}

function configuracion(idUser){
	window.location.replace("http://mixcrowddb.sytes.net:5000/mostrar_user/"+idUser);
}

function myFunctionC(xml,idUser){
    debugger;
  var list_total="";
  for(i=0;i<xml.length;i++){
    var nombre = xml[i][0];
    var email = xml[i][1];
    var contr = xmml[i][2];
    var list="<div class=\"field-wrap\">"+
            "<label for=\"nombre\"></label>"+
            "<input type=\"text\" required autocomplete=\"on\" id=\"nombre\" placeholder=\"User name\" value=\""+nombre+"\"/>"+
          "</div>"+
          "<div class=\"field-wrap\">"+
            "<label for=\"mail\"></label>"+
            "<input type=\"email\" required autocomplete=\"on\" id=\"mail\" placeholder=\"E-mail\" value=\""+email+"\"/>"+
          "</div>"+
          "<div class=\"field-wrap\">"+
            "<label for=\"pswd\"></label>"+
            "<input type=\"password\"required autocomplete=\"off\" id=\"pswd\" placeholder=\"Password\" value=\""+contr+"\"/>"+
          "</div>";
    list_total=list_total+list;
   }
  document.getElementById("infoU").innerHTML = list_total;
}