// Created by iWeb 3.0.4 local-build-20140629

setTransparentGifURL('../Media/transparent.gif');function applyEffects()
{var registry=IWCreateEffectRegistry();registry.registerEffects({stroke_0:new IWStrokeParts([{rect:new IWRect(-2,2,4,262),url:'Cursos_files/stroke.png'},{rect:new IWRect(-2,-2,4,4),url:'Cursos_files/stroke_1.png'},{rect:new IWRect(2,-2,358,4),url:'Cursos_files/stroke_2.png'},{rect:new IWRect(360,-2,4,4),url:'Cursos_files/stroke_3.png'},{rect:new IWRect(360,2,4,262),url:'Cursos_files/stroke_4.png'},{rect:new IWRect(360,264,4,4),url:'Cursos_files/stroke_5.png'},{rect:new IWRect(2,264,358,4),url:'Cursos_files/stroke_6.png'},{rect:new IWRect(-2,264,4,4),url:'Cursos_files/stroke_7.png'}],new IWSize(362,266))});registry.applyEffects();}
function hostedOnDM()
{return false;}
function photocastSubscribe()
{photocastHelper("http://www.carlosdelfino.eti.br/Carlos_Delfino_-_Consultoria_e_Projetos/Cursos/rss.xml");}
function onPageLoad()
{loadMozillaCSS('Cursos_files/CursosMoz.css')
adjustLineHeightIfTooBig('id1');adjustFontSizeIfTooBig('id1');adjustLineHeightIfTooBig('id2');adjustFontSizeIfTooBig('id2');detectBrowser();adjustLineHeightIfTooBig('id3');adjustFontSizeIfTooBig('id3');adjustLineHeightIfTooBig('id5');adjustFontSizeIfTooBig('id5');Widget.onload();fixupAllIEPNGBGs();fixAllIEPNGs('../Media/transparent.gif');fixupIECSS3Opacity('id4');applyEffects()}
function onPageUnload()
{Widget.onunload();}
