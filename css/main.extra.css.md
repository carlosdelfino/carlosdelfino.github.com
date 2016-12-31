---
permalink: /css/main.extra.css
layout: css
---

/\*---------------------------------------------
					Index Start
-----------------------------------------------\*/
/\*--
	Slider Start
--\*/
#slider {
  padding: 70px 0 70px 0;
  position: relative;
  background: url(../images/{{ site.cover }}) no-repeat;
  background-size: 100% 80%;
  background-attachment: fixed;
  background-position: 10% 0%;
  background-color: rgba(255,255,255,0.3)
  -khtml-opacity:.50; 
  -moz-opacity:.50; 
  -ms-filter:"alpha(opacity=50)";
  filter:alpha(opacity=50);
  filter:progid:DXImageTransform.Microsoft.Alpha(opacity=0.5);
  /* Fallback for web browsers that doesn't support RGBa */
  filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#99000000, endColorstr=#99000000);
  -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorstr=#99000000, endColorstr=#99000000)";
}


/\*---------------------------------------------
					Work Start
-----------------------------------------------\*/
/\*--
	Slider-work Start
--\*/
#global-header {
  background: url(../images/{{ site.cover }}) no-repeat;
  background-size: cover;
  padding-top: 150px;
  padding-bottom: 107px;
  position: relative;
  background-attachment: fixed;
}

/\*---------------------------------------------
					 Contact Start
-----------------------------------------------\*/
/\*--
	slider-contact Start
--\*/
#slider-contact {
  background: url(../images/{{ site.cover }}) no-repeat;
  background-size: cover;
  padding-top: 150px;
  padding-bottom: 107px;
  position: relative;
}
