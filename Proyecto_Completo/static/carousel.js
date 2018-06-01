function loadCarousel(idUser){
	sign(idUser);
	studio(idUser);
	loadCarPrincipal(idUser);
	if (idUser != "None"){
		loadCarUserRec(idUser);
	}
	loadCarUser1(idUser);
	loadCarUser2(idUser);
	
}

function loadCarPrincipal(idUser){
	var xmlhttp = new XMLHttpRequest();
     xmlhttp.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) {
      var info=JSON.parse(this.responseText);
      myCarPrincipal(info,idUser);
      }
     };
     xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/get_carousel_principal/"+idUser, true);
     xmlhttp.send(idUser);	
}

function myCarPrincipal(xml,idUser){
	var lista="";
	for (i=0; i<xml.length; i++){
	  var img = xml[i][4];
	  var title = xml[i][0];
	  var autor = xml[i][8];
	  var descr = xml[i][7];
	  var valoracion = xml[i][6];
	  var genero = "genero";
	  var list = "";
	  if (i==0){
	  	list = list + "<div class=\"item active\">";
	  }
	  else{
	  	list = list + "<div class=\"item\">";
	  }
	  list=  list + "<img src=\""+img+"\" alt=\"Slide"+i+"\">"+
                "<a href=\"http://mixcrowddb.sytes.net:5000/mezclador/"+title.split(" ")[0]+"_"+idUser+"\">"+
                "<div class=\"carousel-caption\">"+
                    "<h3>"+title+"</h3> <p>"+descr+"</p>"+
                "</div> </a>"+
            	"</div>";
       lista = lista + list;
	}
	 document.getElementById("carPrin").innerHTML = lista;
}

function loadCarUser1(idUser){
	var xmlhttp = new XMLHttpRequest();
     xmlhttp.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) {
      var info=JSON.parse(this.responseText);
      myCarUser1(info,idUser);
      }
     };
     xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/get_carousel_user1/"+idUser, true);
     xmlhttp.send(idUser);	
}

function myCarUser1(xml,idUser){
	var lista="<h2>Projects best rated</h2>";
	for (i=0; i<xml.length; i++){
	  var img = xml[i][4];
	  var title = xml[i][0];
	  var autor = xml[i][8];
	  var descr = xml[i][7];
	  var valoracion = xml[i][6];
	  var genero = "genero";
	  var list="<a href=\"http://mixcrowddb.sytes.net:5000/mezclador/"+title.split(" ")[0]+"_"+idUser+"\" class=\"list-group-item\">"+
        "<img src=\""+img+"\" alt=\"Second Slide\">"+
        "<h4>"+title+"</h4>"+
        "<h5>"+descr+"</h5>"+
    "</a>";
       lista = lista + list;
	}
	document.getElementById("carUser1").innerHTML = lista;
}

function loadCarUser2(idUser){
	var xmlhttp = new XMLHttpRequest();
     xmlhttp.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) {
      var info=JSON.parse(this.responseText);
      myCarUser2(info,idUser);
      }
     };
     xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/get_carousel_user2/"+idUser, true);
     xmlhttp.send(idUser);	
}

function myCarUser2(xml,idUser){
	var lista="<h2>Projects most commented</h2>";
	for (i=0; i<xml.length; i++){
	  var img = xml[i][4];
	  var title = xml[i][0];
	  var autor = xml[i][8];
	  var descr = xml[i][7];
	  var valoracion = xml[i][6];
	  var genero = "genero";
	  var list = "";
	  list=  "<a href=\"http://mixcrowddb.sytes.net:5000/mezclador/"+title.split(" ")[0]+"_"+idUser+"\" class=\"list-group-item\">"+
        "<img src=\""+img+"\" alt=\"Second Slide\">"+
        "<h4>"+title+"</h4>"+
        "<h5>"+descr+"</h5>"+
    "</a>";
       lista = lista + list;
	}
	document.getElementById("carUser2").innerHTML = lista;
}

function loadCarUserRec(idUser){
	var xmlhttp = new XMLHttpRequest();
     xmlhttp.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) {
      var info=JSON.parse(this.responseText);
      myCarUserRec(info,idUser);
      }
     };
     xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/get_carousel_user_recomend/"+idUser, true);
     xmlhttp.send(idUser);	
}

function myCarUserRec(xml,idUser){
	var lista="<h2>Recomended for you</h2>";
	for (i=0; i<xml.length; i++){
	  var img = xml[i][4];
	  var title = xml[i][0];
	  var autor = xml[i][8];
	  var descr = xml[i][7];
	  var valoracion = xml[i][6];
	  var genero = "genero";
	  var list = "";
	  list=  "<a href=\"http://mixcrowddb.sytes.net:5000/mezclador/"+title.split(" ")[0]+"_"+idUser+"\" class=\"list-group-item\">"+
        "<img src=\""+img+"\" alt=\"Second Slide\">"+
        "<h4>"+title+"</h4>"+
        "<h5>"+descr+"</h5>"+
    "</a>";
       lista = lista + list;
	}
	document.getElementById("carUserRec").innerHTML = lista;
}