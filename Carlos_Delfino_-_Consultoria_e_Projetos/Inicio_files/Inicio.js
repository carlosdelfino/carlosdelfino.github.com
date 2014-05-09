// Created by iWeb 3.0.4 local-build-20140509

setTransparentGifURL('Media/transparent.gif');function applyEffects()
{var registry=IWCreateEffectRegistry();registry.registerEffects({stroke_0:new IWStrokeParts([{rect:new IWRect(-2,2,4,251),url:'Inicio_files/stroke.png'},{rect:new IWRect(-2,-2,4,4),url:'Inicio_files/stroke_1.png'},{rect:new IWRect(2,-2,631,4),url:'Inicio_files/stroke_2.png'},{rect:new IWRect(633,-2,5,4),url:'Inicio_files/stroke_3.png'},{rect:new IWRect(633,2,5,251),url:'Inicio_files/stroke_4.png'},{rect:new IWRect(633,253,5,4),url:'Inicio_files/stroke_5.png'},{rect:new IWRect(2,253,631,4),url:'Inicio_files/stroke_6.png'},{rect:new IWRect(-2,253,4,4),url:'Inicio_files/stroke_7.png'}],new IWSize(635,255))});registry.applyEffects();}
function hostedOnDM()
{return false;}
function onPageLoad()
{loadMozillaCSS('Inicio_files/InicioMoz.css')
adjustLineHeightIfTooBig('id1');adjustFontSizeIfTooBig('id1');adjustLineHeightIfTooBig('id2');adjustFontSizeIfTooBig('id2');adjustLineHeightIfTooBig('id3');adjustFontSizeIfTooBig('id3');detectBrowser();Widget.onload();fixupAllIEPNGBGs();fixAllIEPNGs('Media/transparent.gif');fixupIECSS3Opacity('id4');applyEffects()}
function onPageUnload()
{Widget.onunload();}
