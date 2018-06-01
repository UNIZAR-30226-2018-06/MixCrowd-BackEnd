$('.form').find('input, textarea').on('keyup blur focus', function (e) {
  
  var $this = $(this),
      label = $this.prev('label');

	  if (e.type === 'keyup') {
			if ($this.val() === '') {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
    	if( $this.val() === '' ) {
    		label.removeClass('active highlight'); 
			} else {
		    label.removeClass('highlight');   
			}   
    } else if (e.type === 'focus') {
      
      if( $this.val() === '' ) {
    		label.removeClass('highlight'); 
			} 
      else if( $this.val() !== '' ) {
		    label.addClass('highlight');
			}
    }

});

$('.tab a').on('click', function (e) {
  
  e.preventDefault();
  
  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');
  
  target = $(this).attr('href');

  $('.tab-content > div').not(target).hide();
  
  $(target).fadeIn(600);
  
});


//Mostrara u ocultara la contraseña del Login
function showPassLog() {
    var x = document.getElementById("pswdlog");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}


//Mostrara u ocultara la contraseña del Sign up
function showPassSign() {
    var x = document.getElementById("pswdsign");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}