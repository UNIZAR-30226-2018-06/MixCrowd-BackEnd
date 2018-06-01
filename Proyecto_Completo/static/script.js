

function calculateTotalValue(length) {
    var minutes = Math.floor(length / 60),
        seconds_int = length - minutes * 60,
        seconds_str = seconds_int.toString(),
        seconds = seconds_str.substr(0, 2),
        time = minutes + ':' + seconds

    return time;
}

function calculateCurrentValue(currentTime) {
    var current_hour = parseInt(currentTime / 3600) % 24,
        current_minute = parseInt(currentTime / 60) % 60,
        current_seconds_long = currentTime % 60,
        current_seconds = current_seconds_long.toFixed(),
        current_time = (current_minute < 10 ? "0" + current_minute : current_minute) + ":" + (current_seconds < 10 ? "0" + current_seconds : current_seconds);

    return current_time;
}

function initProgressBar() {
    var player = document.getElementById('player');
    var length = player.duration
    var current_time = player.currentTime;

    // calculate total length of value
    var totalLength = calculateTotalValue(length)
    jQuery(".end-time").html(totalLength);

    // calculate current value time
    var currentTime = calculateCurrentValue(current_time);
    jQuery(".start-time").html(currentTime);

    var progressbar = document.getElementById('seekObj');
    progressbar.value = (player.currentTime / player.duration);
    progressbar.addEventListener("click", seek);

    if (player.currentTime == player.duration) {
        $('#play-btn').removeClass('pause');
    }

    function seek(evt) {
        var percent = evt.offsetX / this.offsetWidth;
        player.currentTime = percent * player.duration;
        progressbar.value = percent / 100;
    }
};

function initPlayers(num) {
    // pass num in if there are multiple audio players e.g 'player' + i

    for (var i = 0; i < num; i++) {
        (function() {

            // Variables
            // ----------------------------------------------------------
            // audio embed object
            var playerContainer = document.getElementById('player-container'),
                player = document.getElementById('player'),
                isPlaying = false,
                playBtn = document.getElementById('play-btn');

            // Controls Listeners
            // ----------------------------------------------------------
            if (playBtn != null) {
                playBtn.addEventListener('click', function() {
                    togglePlay()
                });
            }

            // Controls & Sounds Methods
            // ----------------------------------------------------------
            function togglePlay() {
                if (player.paused === false) {
                    player.pause();
                    isPlaying = false;
                    $('#play-btn').removeClass('pause');

                } else {
                    player.play();
                    $('#play-btn').addClass('pause');
                    isPlaying = true;
                }
            }
        }());
    }
}

initPlayers(jQuery('#player-container').length);




/*
function removeName(itemid){
    var item = document.getElementById(itemid);
    item.parentNode.removeChild(item);
}*/
function removeName(itemid,nombre,id_proyecto){
  var item = document.getElementById(itemid);
  //document.getElementById(itemid).outerHTML='';
  if (item.parentNode){
      item.parentNode.removeChild(item);
  }
  var xmlhttp = new XMLHttpRequest();
  var nom = nombre.split(" ")[0];
  xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/delete_pista/"+id_proyecto+"/"+nom, true);
  xmlhttp.send(nombre);
}


/* choose button */////////////////////////////////////////////////

document.querySelector("#selectFile").addEventListener('change', function (ev) {

    // TO SEE THE NAME OF THE FILE IN THE CONSOLE BUT IS TRASH CODE BECAUSE A NORMAL USER DON'T HAVE THE CONSOLE OPEN.
    // console.log(ev.target.files[0].name);

    document.querySelector("[for='selectFile']").innerHTML = ev.target.files[0].name;

});

/////////////////////////////////////////////////////////////////////////////////// hasta ui button choose
function existeID(num)
{
    var el = document.getElementById("lista").getElementsByTagName("LI");
    for (var i=0; i<el.length; i++)
    {
        if(el[i].firstElementChild.id==num)
            return true;
    }
    return false;
}
//// Añadir a la lista ///////////////////////////////////////////////////////////////
function add_li(id_proyecto)
{
    // var file = document.forms['formName']['inputName'].files[0];
    var nuevoLi = document.getElementById('selectFile').files[0].name;
    //var nuevoLi=document.getElementById("selectFile").value;
    var el = document.getElementById("lista").getElementsByTagName("li");
    //var id = el.length + 1;
    var id=Math.floor(Math.random()*65535+1);
    while (existeID(id)===true){
        id = Math.floor(Math.random()*65535+1);
    }
    var nom_proyecto = id_proyecto.split("_")[0];
    var aux= "";
    var final = "";
    /*var audio = document.createElement('audio');
    audio.src = "nuevoLi";
    var duracion = audio.duration;*/
    /*var audio = new Audio("cosa.mp3");
    audio.src=document
    duracion = audio.duration;*/
    /*var sound = document.createElement("audio");
    debugger;
    sound.src=window.URL.createObjectURL(document.getElementById('selectFile').files[0]);
    sound.load();
    debugger;
    var duracion = sound.duration;
    debugger;
    window.URL.revokeObjectURL(sound.src);+/
    /*var reader =new FileReader();
    var file = document.getElementById('selectFile').files[0];
    reader.readAsDataURL(file);
    var duracion=reader.duration;*/
    //var duracion=document.getElementById('selectFile').files[0].id3.TLEN;
    var duracion = document.getElementById('selectFile').files[0].duration;
    for (i=0; i<nuevoLi.length; i++){
        if (nuevoLi[i] == '\\'){
            aux = "";
        } else if (nuevoLi[i] == '.'){
            final = aux;
        } else {
            aux = aux + nuevoLi[i];
        }
    }
    nuevoLi = final;
    if(nuevoLi.length>0)
    {
        if(find_li(nuevoLi))
        {
            var li=document.createElement('li');
            li.id=id;
            li.innerHTML="<span>"+nuevoLi+"</span> <span>Instant<input class=\"instanteC\" type=\"time\" id=\"" +id+"_inst"+  "\" min=\"00:00:00\" max=\"08:00:00\" step=\"1\" value=\"00:00:00\"><label for=\"" +id+"_inst"+  "\"></label></span><span>Panning <input type=\"range\" class=\"panningC\" id=\"" +id+"_pan"+  "\" min=\"0\" max=\"100\" step=\"1\"/><label for=\"" +id+"_pan"+  "\"></label></span>&nbsp;&nbsp;<input class=\"chequed\" value=\""+nuevoLi+"\" type=\"checkbox\" id=\"" +id+"_l"+  "\"/> <label for=\"" +id+"_l"+ "\">Play</label> <button class=\"erasebutton\" onclick= \"removeName(" +id+ ",\'"+ nuevoLi +"\',\'"+ nom_proyecto +"\')\"> ❌ </button>";
            document.getElementById("lista").appendChild(li);
        } else {
            // error de archivo ya existe
        }
    }


  var formData = new FormData();
  var instante = document.getElementById(id+"_inst").value;
  var panning = document.getElementById(id+"_pan").value;
  debugger;

  formData.append("id_proyecto", nom_proyecto);
  formData.append("nombre_pista", nuevoLi);
  formData.append("pista_nueva", document.getElementById('selectFile').files[0]);
  formData.append("instante", 0);
  formData.append("panning", 50);
  debugger;
  var request = new XMLHttpRequest();
  request.open("POST", "http://mixcrowddb.sytes.net:5000/add_pista", true);
  request.send(formData);

    return false;
}


function find_li(contenido)
{
    var el = document.getElementById("lista").getElementsByTagName("LI");
    for (var i=0; i<el.length; i++)
    {
        if(el[i].firstElementChild.innerHTML==contenido)
            return false;
    }
    return true;
}

 
//////////////////////////////////////////////////////////////////////////////////

 function loadMix(name, idUser) {
    var aux = name.split("_");
    var nombre = aux[0];
    var usuario = aux[1];
    sign(usuario);
    loadInfo(nombre);
    loadPistas(nombre);
    loadComentario(name);
    studio(usuario);
    seleccion(nombre);
    load_val(nombre,usuario);
 }

function seleccion(user) {
     document.getElementById("seleccion").innerHTML = "<input id=\"selectFile\" type=\"file\" accept=\"audio/*\" onchange=add_li(\'"+ user +"\') onclick=\"document.getElementById('selectFile').value = ''\" value=\"anadir\">";
  }



  function loadInfo(name) {
     var xmlhttp = new XMLHttpRequest();
     xmlhttp.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) {
      var info=JSON.parse(this.responseText);
      myInfo(info);
      }
     };
     xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/mostrar_proyecto/"+name, true);
     xmlhttp.send(name);
  }

  function myInfo(xml) {
      var len = xml.length; 
      var img = xml[0][4];
      var title = xml[0][0];
      var autor = xml[0][8];
      var descr = xml[0][7];
      var valoracion = xml[0][6];
      var genero = "";
      for(i=1; i<xml.length; i++){
        genero = genero + xml[i][0] + ",";
      }
      var list=" <div class=\"flotalo\"><div class=\"album-art\"><img src=\""+img+
      "\"/> <div class=\"actions\">  </div> </div><div class=\"album-details\"> <h2> <img src=\"" +
      img + "\"/>" + title + "</h2> <h1>" + title + "</h1><span class=\"spaneitor\"> <p class=\"parrafo\"> AUTOR: " + autor + "<br> GENERO: " + genero + "<br>" +  
      descr + "</p> <p class=\"parrafo2\">&nbsp;</p> </div></div>";

     document.getElementById("albumDescription").innerHTML = list;

     var listaa="<h2>Valoracion media</h2>";
     for(i=0; i<(5-valoracion); i++){
        listaa+= "<span class=\"fa fa-star \"></span>";
     }
     for(i=0; i<valoracion; i++){
        listaa+= "<span class=\"fa fa-star checked\"></span>";
     }
     document.getElementById("val_media").innerHTML = listaa;
  }





  function loadPistas(name) {
     var xmlhttp = new XMLHttpRequest();
     xmlhttp.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) {
      var info=JSON.parse(this.responseText);
      myPistas(info,name);
      }
     };
     xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/get_todas_pistas/"+name, true);
     xmlhttp.send(name);
  }

   function myPistas(xml,id_proyecto) {
     var list=" ";
     var listaAux ="";
     var vp=[]; var vp2=[];
     var vi=[]; var vi2=[];
     for (i = 0; i <xml.length; i++) {
      var name = xml[i][0];
      var instante = xml[i][1];
      var duracion = 100;//xml[i][2];
      var panning = xml[i][3];
      var hour = duracion / 3600;
      var min = (duracion / 60) % 60;
      var seg = duracion % 3600;
      var instanteFinal = hour.toString() + ":" + min + ":" + seg;

      var id=Math.floor(Math.random()*65535+1);
        while (existeID(id)===true){
          id = Math.floor(Math.random()*65535+1);
        }

      listaAux = "<li id=\"" + id + "\"><span>"+name+"</span> <span>Instant<input  class=\"instanteC\" type=\"time\" id=\"" +id+"_inst"+  "\" min=\"00:00:00\" max=\"08:00:00\" step=\"1\" value=\"00:00:00\"><label for=\"" +id+"_inst"+  "\"></label></span><span>Panning <input class=\"panningC\" type=\"range\" id=\"" +id+"_pan"+  "\" min=\"0\" max=\"100\" step=\"1\"/><label for=\"" +id+"_pan"+  "\"></label></span>  &nbsp;&nbsp;<input type=\"checkbox\" class=\"chequed\" value=\""+name+"\" id=\"" +id+"_l"+  "\"/> <label for=\"" +id+"_l"+ "\">Play</label> <button class=\"erasebutton\" onclick= \"removeName(" +id+ ",\'"+ name +"\',\'"+ id_proyecto +"\')\"> ❌ </button></li>";
      
      vp.push(id+"_pan");
      vp2.push(panning);
      vi.push(id+"_inst");
      vi2.push(instanteFinal);
      list = list + listaAux;
     }
     document.getElementById("lista").innerHTML = list;
     for (i = 0; i <vp.length; i++) {
        document.getElementById(vi[i]).value = vi2[i];
        document.getElementById(vp[i]).value = vp2[i];
     }
  }



  function loadComentario(name) {
     var xmlhttp = new XMLHttpRequest();
     xmlhttp.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) {
      var info=JSON.parse(this.responseText);
      myComentario(info);
      }
     };
     xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/get_comentario/"+name, true);
     xmlhttp.send(name);
  }

  function myComentario(xml) {
      var listaTotal="";
      for (i = 0; i <xml.length; i++) {
        var fecha = xml[i][0];
        var comentador = xml[i][1];
        var texto = xml[i][2];
        listaTotal=listaTotal+"<br><h4>"+comentador+" </h4><p>"+texto+"</p>";
      }
      
      document.getElementById("comments").innerHTML = listaTotal;
  }

  function load_val(id_proyecto,user){
    var xmlhttp = new XMLHttpRequest();
     xmlhttp.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) {
      var info=JSON.parse(this.responseText);
      my_valor(info);
     }
     };
     xmlhttp.open("GET", "http://mixcrowddb.sytes.net:5000/get_valoracion_usuario/"+id_proyecto+"/"+user, true);
     xmlhttp.send(name);
  }

  

  function my_valor(xml) {
    debugger;
      list_inicio="<h2>Valora este proyecto</h2> <fieldset>";
      list_final="</fieldset>";    
      list_dentro="";
      if (xml=='0'){
        for (i = 5; i >=1; i--) {
          list_dentro+="<input type=\"radio\" id=\"star"+i+"\""+"name=\"rating\" value=\"" +i +"\" onclick=\"mandar_valoracion("+i+")\"/><label for=\"star"+i+"\" title=\"Outstanding\">"+i+ " stars</label>";  
        } 
      }
      else{
        for (i = 5; i >=1; i--) {
          if (i==xml){
             list_dentro+="<input type=\"radio\" id=\"star"+i+"\""+"name=\"rating\" value=\"" +i +"\" checked=\"checked\" onclick=\"mandar_valoracion("+i+")\" /><label for=\"star"+i+"\" title=\"Outstanding\">"+i+ " stars</label>";
          }
          else{
             list_dentro+="<input type=\"radio\" id=\"star"+i+"\""+"name=\"rating\" value=\"" +i +"\" onclick=\"mandar_valoracion("+i+")\"/><label for=\"star"+i+"\" title=\"Outstanding\">"+i+ " stars</label>";  
          }
        }
      }  
      listaTotal=list_inicio+list_dentro+list_final;
      document.getElementById("val_user").innerHTML = listaTotal;
  }

  function mandar_valoracion(valoracion){
    debugger;
    var formData = new FormData();
    var url = window.location.href;
    list=url.split("/");
    idProyecto=list[4].split("_")[0];
    idUser=list[4].split("_")[1];  
    formData.append("val", valoracion);
    var request = new XMLHttpRequest();
    request.open("POST", "http://mixcrowddb.sytes.net:5000/set_valoracion_usuario/"+idProyecto+"/"+idUser , true);
    request.send(formData);
  }

////////////////////////////////////////////////////generar lista pistas////////////////////////////////////////////////


/*
 function loadPro() {
 var xmlhttp = new XMLHttpRequest();
 xmlhttp.onreadystatechange = function() {
 if (this.readyState == 4 && this.status == 200) {
 myFunction(this);
 }
 };
 xmlhttp.open("POST", "http://mixcrowddb.sytes.net:5000/getProjectsUser", true);
 xmlhttp.send();
 }

 function myFunction(xml) {
 var i;
 var xmlDoc = xml.responseXML;

 /*
 var list="<div class=\"container\">"+
 "<h1 style=\"color: rgba(177,79,7,0.69)\">Project1</h1>"+
 "<div class=\"dropdown\">"+
 "<button class=\"dropbtn\">Info</button>"+
 "<div class=\"dropdown-content\">"+
 "<a href=\"#myModal1\" data-toggle=\"modal\">Users</a>"+
 "<a href=\"#myModal1\" data-toggle=\"modal\">Description</a>"+
 "<a href=\"#myModal1\" data-toggle=\"modal\">Style</a>"+
 "</div>"+
 "</div>"+
 "<div class=\"modal fade\" id=\"myModal1\" role=\"dialog\">"+
 "<div class=\"modal-dialog\">
 "<div class=\"modal-content\">"+
 "<div class=\"modal-header\">"+
 "<button type=\"button\" class=\"close\" data-dismiss=\"modal\">&times;</button>"+
 "<h4 class=\"modal-title\">Modal Header</h4>"+
 "</div>"+
 "<div class=\"modal-body\">"
 <p>Some text in the modal.</p>
 </div>
 <div class="modal-footer">
 <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
 </div>
 </div>

 </div>
 </div>
 <img src="https://image.freepik.com/free-vector/circle-made-of-music-instruments_23-2147509304.jpg" style="width:100%" style="border-radius:50%;">
 <button class="btn1">Entrar</button>
 <button class="btn">Eliminar</button>
 </div>";*/
/*
 var list = "<span>"+nuevoLi+"</span> <span>"+duracion+"  &nbsp;&nbsp;<input type=\"checkbox\" id=\"" +id+"l"+
 "\"/> <label for=\"" +id+"l"+ "\">Play</label> <button class=\"erasebutton\" onclick= \"removeName(" +id+
 ")\"> ❌ </button> </span>";
 var x = xmlDoc.getElementsByTagName("CD");
 for (i = 0; i <x.length; i++) {
 table += "<tr><td>" +
 x[i].getElementsByTagName("ARTIST")[0].childNodes[0].nodeValue +
 "</td><td>" +
 x[i].getElementsByTagName("TITLE")[0].childNodes[0].nodeValue +
 "</td></tr>";
 }
 document.getElementById("listaProyectos").innerHTML = list;
 }
 */











