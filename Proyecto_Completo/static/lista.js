function carga(idUser){
	loadPro(idUser);
	sign(idUser);
	studio(idUser)
}

function loadPro(idUser) {
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var myArr=JSON.parse(this.responseText);
      myFunction(myArr,idUser);
    }
  };
  xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/getProjectsUser/"+idUser, true);
  xmlhttp.send(idUser);
}

function traerEstilos(id_proyecto) {
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var estilos=JSON.parse(this.responseText);
      mostrarEstilos(estilos);
    }
  };
  xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/getStyles/"+id_proyecto, true);
  xmlhttp.send(id_proyecto);
}

function mostrarEstilos(xml){
	var list_total="";
	list_total = "<div class=\"modal-body\">"+"<p>";
  	for(i=0;i<xml.length;i++){
  		list_total = list_total + xml[i] + ",";
  	}
  	list_total = list_total + "</p>"+"</div>";
  	document.getElementById("listaEstilos").innerHTML = list_total;
}

function myFunction(xml,idUser) {
  var list_total="";
  for(i=0;i<xml.length;i++){
	  var y=xml[i];
	  var id = i ;
	  var ya = y[0];
	  var list="<div class=\"container\" id=\"" +i + "\">"+ 
	  "<h1 style=\"color: #ffff\">"+y[0]+"</h1>"+
	  "<div class=\"dropdown\">"+
		"<button class=\"dropbtn\">Info</button>"+
		"<div class=\"dropdown-content\">"+
		  "<a href=\"#myModal1\" data-toggle=\"modal\">Users</a>"+
		  "<a href=\"#myModal2\" data-toggle=\"modal\">Description</a>"+
		  "<a onclick=\"traerEstilos(\'" + ya + "\')\" href=\"#myModal3\" data-toggle=\"modal\">Style</a>"+
		"</div>"+
	  "</div>"+
	  "<div class=\"modal fade\" id=\"myModal1\" role=\"dialog\">"+
		"<div class=\"modal-dialog\">"+
		"<div class=\"modal-content\">"+
		    "<div class=\"modal-header\">"+
		      "<button type=\"button\" class=\"close\" data-dismiss=\"modal\">&times;</button>"+
		      "<h4 class=\"modal-title\">Users</h4>"+
		    "</div>"+
		    "<div class=\"modal-body\">"+
		      "<p>"+y[3]+"</p>"+
		    "</div>"+
		    "<div class=\"modal-footer\">"+
		      "<button type=\"button\" class=\"btn btn-default\" data-dismiss=\"modal\">Close</button>"+
		    "</div>"+
		  "</div>"+

		"</div>"+
	  "</div>"+
	  "<div class=\"modal fade\" id=\"myModal2\" role=\"dialog\">"+
		"<div class=\"modal-dialog\">"+
		"<div class=\"modal-content\">"+
		    "<div class=\"modal-header\">"+
		      "<button type=\"button\" class=\"close\" data-dismiss=\"modal\">&times;</button>"+
		      "<h4 class=\"modal-title\">Description</h4>"+
		    "</div>"+
		    "<div class=\"modal-body\">"+
		      "<p>"+y[7]+"</p>"+
		    "</div>"+
		    "<div class=\"modal-footer\">"+
		      "<button type=\"button\" class=\"btn btn-default\" data-dismiss=\"modal\">Close</button>"+
		    "</div>"+
		  "</div>"+

		"</div>"+
	  "</div>"+
	  "<div class=\"modal fade\" id=\"myModal3\" role=\"dialog\">"+
		"<div class=\"modal-dialog\">"+
		"<div class=\"modal-content\">"+
		    "<div class=\"modal-header\">"+
		      "<button type=\"button\" class=\"close\" data-dismiss=\"modal\">&times;</button>"+
		      "<h4 class=\"modal-title\">Style</h4>"+
		    "</div>"+
		    "<div id=\"listaEstilos\"> </div>"+
		    "<div class=\"modal-footer\">"+
		      "<button type=\"button\" class=\"btn btn-default\" data-dismiss=\"modal\">Close</button>"+
		    "</div>"+
		  "</div>"+

		"</div>"+
	  "</div>"+
	  "<img src="+y[4]+" style=\"width:100%\" style=\"border-radius:50%;\">"+
	  "<button class=\"btn1\" onclick= \"mostrar_proyecto(\'" + ya + "\',\'" +  idUser + "\')\" >Entrar</button>"+
	  "<button class=\"btn\" onclick= \"eliminar(" + id + ",\'" + ya + "\')\">Eliminar</button>"+
	"</div>";
  	list_total=list_total+list;
  }
  document.getElementById("listaProyectos").innerHTML = list_total;
}


function mostrar_proyecto(nombre, idUser){
	//window.location="http://mixcrowddb.sytes.net:5000:5000/mezclador";
	var xmlhttp = new XMLHttpRequest();
  	xmlhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
		var myArr=JSON.parse(this.responseText);
      	pag_proyecto(myArr,idUser); 
	}
  };
  	xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/mostrar_proyecto/"+nombre+"/"+idUser, true);
  	xmlhttp.send(nombre,idUser);
}

function pag_proyecto(name,idUser){
	namereal=name[0][0];
	img=name[0][4];
	descripcion=name[0][7];
	administrador=name[0][8];
	namereal = namereal.split(" ");
	aux = namereal[0];
	var total=aux;
	var i=1;
	while(namereal[i] != "" && i<namereal.length){
		total=total+" "+namereal[i];
		i=i+1;
	}
	// var formData = new FormData();
	// formData.append("id_proyecto", namereal);
	// formData.append("img",img);
	// formData.append("descripcion",descripcion);
	// formData.append("administrador",administrador);
	// debugger;
	// var request = new XMLHttpRequest();
	// request.open("POST", "http://mixcrowddb.sytes.net:5000:5000/mezclador", true);
	// request.send(formData);
	window.location.replace("http://mixcrowddb.sytes.net:5000/mezclador/"+total+"_"+idUser);
}

function pag_proyecto1(name){
	window.location.replace("http://mixcrowddb.sytes.net:5000/mezclador/"+name);
}

function eliminar(id,nombre){
	document.getElementById(id).remove();
	var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
	  
	}
  };
  xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/borrar_proyecto/"+nombre, true);
  xmlhttp.send(nombre);
}

