// Created by iWeb 3.0.4 local-build-20140601

setTransparentGifURL('Media/transparent.gif');function applyEffects()
{var registry=IWCreateEffectRegistry();registry.registerEffects({stroke_0:new IWStrokeParts([{rect:new IWRect(-2,2,4,289),url:'Sobre_Mim_files/stroke.png'},{rect:new IWRect(-2,-2,4,4),url:'Sobre_Mim_files/stroke_1.png'},{rect:new IWRect(2,-2,276,4),url:'Sobre_Mim_files/stroke_2.png'},{rect:new IWRect(278,-2,5,4),url:'Sobre_Mim_files/stroke_3.png'},{rect:new IWRect(278,2,5,289),url:'Sobre_Mim_files/stroke_4.png'},{rect:new IWRect(278,291,5,4),url:'Sobre_Mim_files/stroke_5.png'},{rect:new IWRect(2,291,276,4),url:'Sobre_Mim_files/stroke_6.png'},{rect:new IWRect(-2,291,4,4),url:'Sobre_Mim_files/stroke_7.png'}],new IWSize(280,293))});registry.applyEffects();}
function hostedOnDM()
{return false;}
function onPageLoad()
{loadMozillaCSS('Sobre_Mim_files/Sobre_MimMoz.css')
adjustLineHeightIfTooBig('id1');adjustFontSizeIfTooBig('id1');adjustLineHeightIfTooBig('id2');adjustFontSizeIfTooBig('id2');adjustLineHeightIfTooBig('id3');adjustFontSizeIfTooBig('id3');adjustLineHeightIfTooBig('id4');adjustFontSizeIfTooBig('id4');detectBrowser();Widget.onload();fixupAllIEPNGBGs();fixAllIEPNGs('Media/transparent.gif');fixupIECSS3Opacity('id5');applyEffects()}
function onPageUnload()
{Widget.onunload();}
