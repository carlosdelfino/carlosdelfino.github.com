$(document).ready(function(){
	
	// randomize owl carrocel
	//Sort random function
	function random(owlSelector) {
		owlSelector.children().sort(function () {
			return Math.round(Math.random()) - 0.5;
		}).each(function () {
			$(this).appendTo(owlSelector);
		});
	}
	
	$("#portfolio-contant-active").mixItUp();
	$("#testimonial-slider").owlCarousel({
	    paginationSpeed : 500,      
	    singleItem: true,
	    autoPlay: 3000,
	    stopOnHover: true,
	    responsive: true,
	    itens: 5,
	    
	    //Mouse Events
	    dragBeforeAnimFinish : true,
	    mouseDrag : true,
	    touchDrag : true,
	    
		//Call beforeInit callback, elem parameter point to $(".feedback")
		beforeInit: function (elem) {
			random(elem);
		}
	});
	$("#clients-logo").owlCarousel({
		autoPlay: 3000,
		items : 5,
		itemsDesktop : [1199,5],
		itemsDesktopSmall : [979,5],
	});

	// google map
		var map;
		function initMap() {
		  map = new google.maps.Map(document.getElementById('map'), {
		    center: {lat: -34.397, lng: 150.644},
		    zoom: 8
		  });
		}
	// Counter
	$('.counter').counterUp({
        delay: 10,
        time: 1000
    });
	particlesJS("particles-js", {
	  "particles": {
	    "number": {
	      "value": 120,
	      "density": {
	        "enable": true,
	        "value_area": 800
	      }
	    },
	    "color": {
	      "value": "#ffffff"
	    },
	    "shape": {
	      "type": "circle",
	      "stroke": {
	        "width": 1,
	        "color": "#33a0ff"
	      },
	    },
	    "opacity": {
	      "value": 0.5,
	      "random": false,
	      "anim": {
	        "enable": false,
	        "speed": 1,
	        "opacity_min": 0.1,
	        "sync": false
	      }
	    },
	    "size": {
	      "value": 5,
	      "random": true,
	      "anim": {
	        "enable": false,
	        "speed": 40,
	        "size_min": 0.1,
	        "sync": false
	      }
	    },
	    "line_linked": {
	      "enable": true,
	      "distance": 150,
	      "color": "#4dacff",
	      "opacity": 0.4,
	      "width": 1
	    },
	    "move": {
	      "enable": true,
	      "speed": 6,
	      "direction": "none",
	      "random": false,
	      "straight": false,
	      "out_mode": "out",
	      "bounce": false,
	      "attract": {
	        "enable": false,
	        "rotateX": 600,
	        "rotateY": 1200
	      }
	    }
	  },
	  "interactivity": {
	    "detect_on": "canvas",
	    "events": {
	      "onhover": {
	        "enable": true,
	        "mode": "grab"
	      },
	      "onclick": {
	        "enable": true,
	        "mode": "push"
	      },
	      "resize": true
	    },
	    "modes": {
	      "grab": {
	        "distance": 140,
	        "line_linked": {
	          "opacity": 1
	        }
	      },
	      "bubble": {
	        "distance": 400,
	        "size": 40,
	        "duration": 2,
	        "opacity": 8,
	        "speed": 3
	      },
	      "repulse": {
	        "distance": 200,
	        "duration": 0.4
	      },
	      "push": {
	        "particles_nb": 4
	      },
	      "remove": {
	        "particles_nb": 2
	      }
	    }
	  },
	  "retina_detect": true
	});
	
	pageCustonFunctions();
});