var cameraPos = {x:0,y:0,z:100};	
var linaccel=new THREE.Vector3(0.0,0.0,0.0);
var rotaccel = new THREE.Vector3(0.0,0.0,0.0);
var rotations = [null, null, null,null,null,null];
var n = [null, null, null,null,null,null];

  

const CALIBRATED = 0;
const RAW = 1;
var accel_units_set = false;

var SCREEN_WIDTH = 250;
var SCREEN_HEIGHT = 200;

var container;

var particle;

var camera;
var scene;
var renderer;

var mouseX = 0;
var mouseY = 0;

var particles = []; 
var particleImage = new Image();//THREE.ImageUtils.loadTexture( "img/ParticleSmoke.png" );
particleImage.src = 'img/ParticleSmoke.png'; 


function updateAccel(accelid, accelx, accely, accelz){
	      var sensor_display_mode = $("input[name='sensor_data_type']:checked").attr('MODE');
	   if (sensor_display_mode == CALIBRATED){
		  accelx = (Math.round(accelx*100.0))/100.0;
     	  accely = (Math.round(accely*100.0))/100.0;
     	  accelz = (Math.round(accelz*100.0))/100.0;
  	      if (!accel_units_set){
     	    if ( Math.sqrt(accelx*accelx + accely*accely + accelz*accelz) < 2.0){
            $('.accelunits').html('<i>g</i>');
            accel_units_set = true;
          } else {
            $('.accelunits').html('<i>m/s<sup>2</sup></i>');
            accel_units_set = true;
          }
    	 }
         var x=document.getElementById("accelX");
     	 x.innerHTML = "" + accelx;
     	 var y=document.getElementById("accelY");
   	     y.innerHTML = "" + accely;
     	 var z=document.getElementById("accelZ");
     	 z.innerHTML = "" + accelz;
   	   }
}
   
function updateRawAccel(accelid, accelx, accely, accelz){
	var sensor_display_mode = $("input[name='sensor_data_type']:checked").attr('MODE');
	if (sensor_display_mode == RAW){
		accelx = (Math.round(accelx*100.0))/100.0;
		accely = (Math.round(accely*100.0))/100.0;
		accelz = (Math.round(accelz*100.0))/100.0;
		if (!accel_units_set){
			if ( Math.sqrt(accelx*accelx + accely*accely + accelz*accelz) < 2.0){
            $('.accelunits').html('<i>g</i>');
          } else {
            $('.accelunits').html('<i>m/s<sup>2</sup></i>');
          }
    	 }
         var x=document.getElementById("accelX");
     	 x.innerHTML = "" + accelx;
     	 var y=document.getElementById("accelY");
   	     y.innerHTML = "" + accely;
     	 var z=document.getElementById("accelZ");
     	 z.innerHTML = "" + accelz;
	}
}
   
var linaccelActive = false;
function updateLinearAccel( linaccelx, linaccely, linaccelz){
	if (!linaccelActive){ setInterval( snow_loop, 2000 / 60 ); linaccelActive = true;}
	linaccel.x = linaccelx;
	linaccel.y = linaccely;	
	linaccel.z = linaccelz;
}

function updateGyro(gyroid, gyrox, gyroy, gyroz){

	var sensor_display_mode = $("input[name='sensor_data_type']:checked").attr('MODE');

	if (sensor_display_mode == CALIBRATED){
		gyrox = (Math.round(gyrox*100.0))/100.0;
		gyroy = (Math.round(gyroy*100.0))/100.0;
		gyroz = (Math.round(gyroz*100.0))/100.0;
		var x=document.getElementById("gyroX");
		x.innerHTML = "" + gyrox;
		var y=document.getElementById("gyroY");
		y.innerHTML = "" + gyroy;
		var z=document.getElementById("gyroZ");
		z.innerHTML = "" + gyroz;
		var scale = 1.0/2000.0;
		rotaccel.x = scale*(-gyroy*cameraPos.z + gyroz*cameraPos.y);
		rotaccel.y = scale*( gyrox*cameraPos.z - gyroz*cameraPos.x);
		rotaccel.z = scale*( gyrox*cameraPos.y - gyroy*cameraPos.x);
	}
}
   
function updateRawGyro(gyroid, gyrox, gyroy, gyroz){

	var sensor_display_mode = parseInt($("input[name='sensor_data_type']:checked").attr('MODE'));
	if (sensor_display_mode == RAW){
		gyrox = (Math.round(gyrox*100.0))/100.0;
		gyroy = (Math.round(gyroy*100.0))/100.0;
		gyroz = (Math.round(gyroz*100.0))/100.0;
		var x=document.getElementById("gyroX");
		x.innerHTML = "" + gyrox;
		var y=document.getElementById("gyroY");
		y.innerHTML = "" + gyroy;
		var z=document.getElementById("gyroZ");
		z.innerHTML = "" + gyroz;
		var scale = 1.0/2000.0;
		rotaccel.x = scale*(-gyroy*cameraPos.z + gyroz*cameraPos.y);
		rotaccel.y = scale*( gyrox*cameraPos.z - gyroz*cameraPos.x);
		rotaccel.z = scale*( gyrox*cameraPos.y - gyroy*cameraPos.x);
	   	}
}	

var accel_cal_count = 0;
function updateAccelCal(){
	++accel_cal_count;
	$('.accel_cal_counter').html('Cal#: ' + accel_cal_count);
}


var mag_cal_count = 0;	
function updateMagCal(){
	++mag_cal_count;
	$('.mag_cal_counter').html('Cal#: '+mag_cal_count);
}

var gyro_cal_count = 0;
function updateGyroCal(){
	++gyro_cal_count;
	if( gyro_cal_count < 9){
		$('.gyro_cal_counter').html('Cal#: '+gyro_cal_count);
	} else {
		$('.gyro_cal_counter').html('Cal#: 9+');
	}
}
		
function updateMagAnomaly( inAnomaly ){
	if( inAnomaly){
		$(container).css('background-color', 'darkred');
		$('.mag_influenced').css('background-color', '#FFE0E0');
	} else {	
		$(container).css('background-color', 'black');
		$('.mag_influenced').css('background-color', '#FFFFFF');
	}
}

        
function updateYPR( yaw, pitch, roll ){
 
	yaw = (Math.round(yaw*100.0))/100.0;
	pitch = (Math.round(pitch*100.0))/100.0;
	roll = (Math.round(roll*100.0))/100.0;
	//yaw = yaw+90;
	pitch=-pitch;
	
//    cameraPos.y = Math.sin(TO_RADIANS*(pitch-90));
//     cameraPos.z = 1000.0;//*(1.0 - Math.cos(TO_RADIANS*(pitch-90)));
//     cameraPos.x = Math.sin(TO_RADIANS*(roll));
     //cameraPos.z = cameraPos.z*(1.0 - Math.cos(roll));
     
	$('.cubie').each( function(index){
		// alert(index);
		if (rotations[index]==null){
            
			rotations[index] = $(this).css('-webkit-transform')  ;
            if (!rotations[index]){
              rotations[index] = $(this).css('-moz-transform');
            }
            if (!rotations[index]){
              rotations[index] = $(this).css('-ms-transform');
            }
            n[index] = eval($(this).attr('n'));
		}
          
		// CSS3: CSS3-y is our z (yaw), CSS3-x is our x(roll), 
		// and CSS3-z is our -y (-pitch)
          
		var newndoty = -Math.cos(TO_RADIANS*pitch)*Math.cos(TO_RADIANS*yaw)*n[index][1] //VERIFIED PR
		- ( Math.sin(TO_RADIANS*roll)*Math.sin(TO_RADIANS*yaw)  + Math.cos(TO_RADIANS*roll)*Math.sin(TO_RADIANS*pitch)*Math.cos(TO_RADIANS*yaw))*n[index][2]//VERIFIED PR
		- ( Math.cos(TO_RADIANS*roll)*Math.sin(TO_RADIANS*yaw) - Math.sin(TO_RADIANS*roll)*Math.sin(TO_RADIANS*pitch)*Math.cos(TO_RADIANS*yaw))*n[index][0]
          ;
      
     
          //csstext = 'rotateZ(' + roll +'deg) rotateX(' + (pitch) +'deg) rotateY('+yaw+'deg) '+ rotations[index];
		csstext = 'rotateY('+yaw+'deg) rotateX(' + (pitch) +'deg) rotateZ(' + roll +'deg) '+ rotations[index];
		if (newndoty<=0){
			$(this).css( 'display','none');
        } else {
        	$(this).css('display','block');
        } 
         
		$(this).css( '-webkit-transform',csstext);
		$(this).css( '-moz-transform',csstext);
		$(this).css( '-ms-transform',csstext);
	});
     
}


function updateOrient(orientid, orientw,  orientx, orienty, orientz){
	
     orientx = (Math.round(orientx*1000.0))/1000.0;
     orienty = (Math.round(orienty*1000.0))/1000.0;
     orientz = (Math.round(orientz*1000.0))/1000.0;
     orientw = (Math.round(orientw*1000.0))/1000.0;
     var x=document.getElementById("orientX");
     x.innerHTML = "" + orientx;
     var y=document.getElementById("orientY");
     y.innerHTML = "" + orienty;
     var z=document.getElementById("orientZ");
     z.innerHTML = "" + orientz;
     var w=document.getElementById("orientW");
     w.innerHTML = "" + orientw;
}

  
   
 function updateMag(magid, magx, magy, magz){
	 var sensor_display_mode = parseInt($("input[name='sensor_data_type']:checked").attr('MODE'));
	 if (sensor_display_mode == CALIBRATED){
		 magx = (Math.round(magx*1000.0))/1000.0;
		 magy = (Math.round(magy*1000.0))/1000.0;
		 magz = (Math.round(magz*1000.0))/1000.0;
		 var x=document.getElementById("magX");
		 x.innerHTML = "" + magx;
		 var y=document.getElementById("magY");
		 y.innerHTML = "" + magy;
		 var z=document.getElementById("magZ");
		 z.innerHTML = "" + magz;
	 }
 }
  

function updateRawMag(magid, magx, magy, magz){
	
	var sensor_display_mode = parseInt($("input[name='sensor_data_type']:checked").attr('MODE'));
	if (sensor_display_mode == RAW){
		magx = (Math.round(magx*1000.0))/1000.0;
		magy = (Math.round(magy*1000.0))/1000.0;
     	magz = (Math.round(magz*1000.0))/1000.0;
        var x=document.getElementById("magX");
	 	x.innerHTML = "" + magx;
      	var y=document.getElementById("magY");
	 	y.innerHTML = "" + magy;
      	var z=document.getElementById("magZ");
	  	z.innerHTML = "" + magz;
	}
}


var windowHalfX ;
var windowHalfY;
	
  
$(document).ready(function(){

	windowHalfX = $('#canvas')[0].innerWidth / 2;
    windowHalfY = $('#canvas')[0].innerHeight / 2;
		         
	$('#startlogbtn').click( function(){
		if ($(this).html()=='<span class="ui-button-text">Start Logging</span>' ||
				$(this).html()=='Start Logging'){
			$(this).html('<span class="ui-button-text">Stop Logging</span>');
			document.title="logging-start";
		} else {
			$(this).html('<span class="ui-button-text">Start Logging</span>');
			document.title="logging-stop";
		}
	});
		
	$('.button').button();
});


function freemotion_init() {
	container = document.createElement('div');
	$('#canvas')[0].appendChild(container);
	$(container).width(SCREEN_WIDTH);
    $(container).height(SCREEN_HEIGHT);
    $(container).css('background-color','black');
	camera = new THREE.PerspectiveCamera( 75, 1, 1, 10000);
	camera.position.z = 1000;

	scene = new THREE.Scene();
	scene.add(camera);
		
	renderer = new THREE.CanvasRenderer();
	renderer.setSize(SCREEN_WIDTH,SCREEN_HEIGHT);
	var material = new THREE.ParticleBasicMaterial( { map: new THREE.Texture(particleImage) } );
		
	for (var i = 0; i < 500; i++) {

		particle = new Particle3D( material);
		particle.position.x = Math.random() * 2000 - 1000;
		particle.position.y = Math.random() * 2000 - 1000;
		particle.position.z = Math.random() * 2000 - 1000;
		particle.scale.x = particle.scale.y =  1;
		scene.add( particle );
		
		particles.push(particle); 
	}

	container.appendChild( renderer.domElement );


	
	//setInterval( loop, 1000 / 60 );
	/* USE THE FOLLOWING TO UNCOMMENT AND ACTIVE TEST PROGREAM*/
	//enable_unit_test();
	
	//initial view:
	updateYPR(-45, 45, 45);

    $('textarea').css('font-weight','bold');
}

function enable_unit_test(){
	setInterval( test_loop, 1000 / 60 );
}

function onDocumentMouseMove( event ) {

	mouseX = event.clientX - windowHalfX;
	mouseY = event.clientY - windowHalfY;
}

function onDocumentTouchStart( event ) {

	if ( event.touches.length == 1 ) {

		event.preventDefault();

		mouseX = event.touches[ 0 ].pageX - windowHalfX;
		mouseY = event.touches[ 0 ].pageY - windowHalfY;
	}
}

function onDocumentTouchMove( event ) {

	if ( event.touches.length == 1 ) {

		event.preventDefault();

		mouseX = event.touches[ 0 ].pageX - windowHalfX;
		mouseY = event.touches[ 0 ].pageY - windowHalfY;
	}
}

//
var YPR = [45,45,-45];
var simtime = 0.0;
var sign=1;

function test_loop() {
	
	YPR[0] += 0.3;
	YPR[1] += sign*0.5;
	YPR[2] += 0.7;
	if(YPR[2]> 90 ) {
		sign=-sign;
	 
		YPR[2] -= 180;
		YPR[0] -= 180;
		YPR[1] = 180-YPR[1];
	} 

	if(YPR[0]>=360) {
		YPR[0] -=360;
	} else if ( YPR[0] < 0){
		YPR[0] += 360;
	}
	if(YPR[1]>=180) {
		YPR[1] -= 360;
	} else if (YPR[1] < -180){
		YPR[1] += 360;
	}
	if (simtime < 100.0){
		setConnectionStatus( false, "Faking it out " + simtime);
	} else {
		setConnectionStatus( true, "Faked connection");
	}
	linaccel.x = 0.06*Math.sin(TO_RADIANS*YPR[0]);
    linaccel.y = 0.06*Math.cos(TO_RADIANS*YPR[0]);
    updateGyro( 0, 1.0*Math.sin(TO_RADIANS*YPR[0]),-1.0*Math.sin(TO_RADIANS*YPR[0]), 1.0);
    updateYPR(YPR[0], YPR[1], YPR[2]);
    updateAccel( 0, linaccel.x, linaccel.y, linaccel.y);
    updateLinearAccel( 0, linaccel.x, linaccel.y, linaccel.y);
       updateMagAnomaly( simtime < 500.0 );
    updateAccelCal();
    updateGyroCal();
    updateMagCal();
    simtime += 1.0;
}

function snow_loop(){

	for(var i = 0; i<particles.length; i++)
	{

		var particle = particles[i]; 
		particle.updatePhysics(); 

		with(particle.position)
		{
            factor=7.5;
            while(y<-factor*SCREEN_WIDTH/2) y+=factor*SCREEN_WIDTH; 
            while(y>factor*SCREEN_WIDTH/2) y -= factor*SCREEN_WIDTH;
			while(x>factor*SCREEN_WIDTH/2) x-=factor*SCREEN_WIDTH; 
			while(x<-factor*SCREEN_WIDTH/2) x+=factor*SCREEN_WIDTH; 
			if(z>100) z-=2000; 
			else if(z<-100) z+=2000;
           // x=50.0; y = 750.0; z= 0.0;
           // if(y > 750.0){ alert([x,y,z]);}
		}				
	}

	camera.position.x = cameraPos.x;//( mouseX - camera.position.x ) * 0.05;
    camera.position.y = cameraPos.y;//( - mouseY - camera.position.y ) * 0.05;
    camera.position.z = cameraPos.z;
    camera.lookAt(scene.position); 
	renderer.render( scene, camera );

	
}
