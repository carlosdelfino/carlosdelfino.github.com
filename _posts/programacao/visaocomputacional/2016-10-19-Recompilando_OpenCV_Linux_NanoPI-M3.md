---
title: "Recompilando o OpenCV no Linux Ubuntu e Similares para Cortex-A53" 
tags: [Cortex-A, Cortex-53, RaspberryPI, Cortex-A53, NanoPI, FrendlyARM, ARM, Visão Computacional, OpenCV, Linux, Câmera, Contador, Bicicleta]
categories: [Visão Computacional]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
image:
 feature: embarcados/nanopi-m3-03-1024x445.png
 teaser: embarcados/nanopi-m3-03-300x174.png
ads: 
 show: true
tagcloud: true
coinbase:
 show: true
---
Nos últimos 5 anos temos tido um grande avanço na visão computacional, carros que detectam pedestres a frente, contadores de bicicleta, sem falar no seu uso na medicina na analise de planetas e imagens telescópicas, onde antes se levavam dias para detectar nos padrões em milhões de imagens, hoje se levam horas.

<!--more-->

O OpenCV está sendo usado no projeto {Contador de Ciclistas](/ContadorDeCiclistas] é uma ferramenta fenomenal capaz de poupar muito trabalho.

Para instala-la é muito simples basta usar o comando:

```bash
sudo apt-get libopencv-dev
```

Porém podemos vir a precisar de outras configurações, como no caso de otimizá-lo para uso no Cortex-A53, no qual somente instalando pacotes pelo Apt-Get não seja suficiente. 

Abaixo estão os comando que usei para compilar e instalar os pacotes importantes para os testes no Cortex-A53, veja que instalo de qualquer forma o pacote `libopencv-dev` e muitas dependências, faço isso para ter através das dependências tudo que preciso para recompila-lo sem surpresas, futuramente farei outro tutorial mais limpo com apenas o que é 100% necessário.


```bash
sudo apt-get update
sudo apt-get install -y build-essential
sudo apt-get install -y cmake
sudo apt-get install -y pkg-config
sudo apt-get install -y checkinstall  yasm 
sudo apt-get install -y python-numpy python-dev
sudo apt-get install -y x264 v4l-utils
sudo apt-get install -y libgtk2.0-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install -y libjpeg-dev libpng-dev libtiff-dev libjasper-dev 
sudo apt-get install -y libopencv-dev 
sudo apt-get install -y libjpeg-dev libjasper-dev libavcodec-dev libavformat-dev
sudo apt-get install -y libswscale-dev libdc1394-22-dev 
sudo apt-get install -y libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev 
sudo apt-get install -y libv4l-dev 
sudo apt-get install -y libtbb-dev 
sudo apt-get install -y libqt4-dev libgtk2.0-dev 
sudo apt-get install -y libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev 
sudo apt-get install -y libtheora-dev libvorbis-dev libxvidcore-dev 
sudo apt-get install -y libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
sudo apt-get install -y libavformat-dev libcv-dev libcvaux-dev libhighgui-dev 
sudo apt-get install -y libopencv-contrib-dev libopencv-dev libopencv-highgui-dev 
sudo apt-get install -y libopencv-legacy-dev libopencv-objdetect-dev libopencv-ocl-dev 
sudo apt-get install -y libopencv-superres-dev libopencv-videostab-dev
sudo apt-get install -y libopencv-highgui-dev libopencv-legacy-dev 
sudo apt-get install -y libopencv-objdetect-dev
```
Para instalar todas as dependências de uma só vez você também pode usar o comando:

```bash
sudo apt-get build-dep opencv
```

```bash
sudo apt-get install libv4l-dev
cd /usr/include/linux
sudo ln -s ../libv4l1-videodev.h videodev.h
```


Para baixar o fonte do OpenCV há duas opções, você pode fazer download do pacote zip ou todo o fonte do GitHub, o importante é usar a versão 2.4 do código.

Considerando baixar o fonte em um pacote, use os seguintes comandos:

```bash
wget http://downloads.sourceforge.net/project/opencvlibrary/opencv-unix/2.4.11/opencv-2.4.11.zip
unzip opencv-2.4.11.zip
cd opencv-2.4.11
```
Crie um diretório para trabalhar com a compilaçãod o pcaote, não faça a compilação no diretório onde está o fonte, você pode criar algo como demonstrado abaixo:

```bash
mkdir release
cd release
```

agora precisamos criar o arquivo Makefile, para isso o OpenCV já nos dá um pré script baseado no cmake, bastando por tanto executar o comando abaixo, veja que estou apenas compilando o core sem os módulos, exemplos e docs, que serão feitos depois.

```bash
cmake -G "Unix Makefiles" \
 -D CMAKE_CXX_COMPILER=/usr/bin/arm-linux-gnueabihf-g++ \
 -D CMAKE_C_COMPILER=/usr/bin/arm-linux-gnueabihf-gcc \
 -D CMAKE_CXX_FLAGS="-mtune=cortex-a53 -mcpu=cortex-a53 -mfloat-abi=hard -march=armv8-a+crc"
 -d CMAKE_C_FLAGS="-mtune=cortex-a53 -mcpu=cortex-a53 -mfloat-abi=hard -march=armv8-a+crc"
 -D CMAKE_BUILD_TYPE=RELEASE-NANOPI-M3 \
 -D CMAKE_INSTALL_PREFIX=/usr/local \
 -D WITH_TBB=ON \
 -D WITH_V4L=ON \
 -D WITH_QT=ON \
 -D WITH_OPENGL=ON \
 -D WITH_IMAGEIO=ON \
 -D WITH_GSTREAMER=ON \
 -D ENABLE_NEON=ON \
 -D ENABLE_FAST_MATH=ON \
 -D BUILD_SHARED_LIBS=OFF \
 -D BUILD_NEW_PYTHON_SUPPORT=OFF \
 -D BUILD_EXAMPLES=OFF \
 -D BUILD_FAT_JAVA_LIB=OFF -DBUILD_opencv_java=OFF \
 -D BUILD_TBB=ON \
 -D BUILD_opencv_apps=OFF -D BUILD_opencv_nofree=OFF  \
 -D BUILD_opencv_objdetect=ON -D BUILD_opencv_core=ON -D BUILD_opencv_imgproc=ON -D BUILD_opencv_ml=ON -D BUILD_opencv_flann=OFF \
 -D BUILD_opencv_highgui=ON \
 -D BUILD_OPTIONAL=Off  \
 -D BUILD_DOCS=OFF \
 -D INSTALL_C_EXAMPLES=OF \
 -D INSTALL_PYTHON_EXAMPLES=OFF \
 -D INSTALL_TO_MANGLED_PATHS=ON \
 -D INSTALL_CREATE_DISTRIB=ON \
 -D INSTALL_TESTS=OFF \
 -D CMAKE_VERBOSE=ON \
 -D CPACK_BINARY_STGZ=OFF \
 -D CPACK_BINARY_TZ=OFF \
 -D CPACK_PACKAGE_NAME="NanoPI-M3"
 ..
```

Podemos criar diversas opções de configuração, criando um diretório para cada uma delas, ou reexecutando o comando acima com ajustes, podemos também passar parametros especiais quando usando as compilações para Release ou Debug com a varíavel "CMAKE_BUILD_TYPE=RELEASE"

O comando acima está otimizado para uso apenas em Detecção e para uso no Cortex-A53, sem java e sem python.

```bash
make all -j4 # 4 cores
sudo make install
 
# ignore libdc1394 error http://stackoverflow.com/questions/12689304/ctypes-error-libdc1394-error-failed-to-initialize-libdc1394
 
#python
#> import cv2
#> cv2.SIFT
#<built-in function SIFT>