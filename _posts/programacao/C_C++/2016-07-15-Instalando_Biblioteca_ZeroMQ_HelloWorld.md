---
title: "Instalando Biblioteca ZeroMQ no Hello World com Eclipse, CDT e CygWin"
tags: [C, C++, Compilador, GCC Explorer, GCC, Navegador, Tempo Real, Aprendizado, ARM, Parallella, Epiphany, ARM64, AVR, x86, PowerPC, CygWin, Pelles C, Visual Studio, Borland, Borland C++, Visual C, Visual C++, IDE, Eclipse, Compilação, Hello World, ZeroMQ, ZMQ]
category: [programacao, Cplusplus]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
ads: 
 show: true
tagcloud: true
donate:
 show: true
 coinbase:
  show: true
 flattr:
  show: true 
---

http://carlosdelfino.eti.br/programacao/cplusplus/Primeiro_Programa_em_C_com_Eclipse_CDT_CygWin/

B. Adding include libraries to a C project

If you plan to play with C, select GNU C on the Languages panel and just add these ones:

C:/soft/cygwin/lib/gcc/i686-pc-cygwin/4.5.3/include
C:/soft/cygwin/lib/gcc/i686-pc-cygwin/4.5.3/include-fixed
C:/soft/cygwin/usr/include
If you need the last one add it too:

C:/soft/cygwin/lib/include/w32api
Click Apply > OK.

C. Let's complete this tutorial

Come back to our project now.
Right click on the project name and select Build Project.

It will generate a Debug or a Release directory with several folders and files such as:

src/MyFirstProject.o
src/MyFirstProject.d
src/subdir.mk
MyFirstProject.exe
makefile
objects.mk
sources.mk
Now you can execute your project, right click on the project and select:

Run as > Local C/C++ Application.

And normally in the console, you will see:

!!!Hello World!!!

Good job! It was a bit complex, but you are a winner, and now the world is yours.