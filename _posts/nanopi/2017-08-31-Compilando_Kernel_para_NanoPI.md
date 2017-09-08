---
title: Compilando o Kernel para NanoPi e uso com 3G da Claro
---

Inicie instalando o GCC para ARM especialmente preparado para compilar para Linux para ARM, é preciso usar a versão 4.9.3 portanto veja os comandos abaixo para obte-los corretamente para o NanoPi M3.

```
sudo mkdir -p /opt/FriendlyARM/toolchain
sudo tar xf prebuilts/gcc-x64/arm-cortexa9-linux-gnueabihf-4.9.3.tar.xz -C /opt/FriendlyARM/toolchain/
```

atualize path de acesso ao GCC atualizando o arquivo `"~/.bashrc"` incluindo :
`export PATH=/opt/FriendlyARM/toolchain/4.9.3/bin:$PATH`
execute `"~/.bashrc"` para surtir efeito as novas alterações:

```
. ~/.bashrc
```

As instruções acima consideram que esteja em um sistema 32bits, caso esteja em um sistema 64bits digite também os comandos abaixo para instalar as versões 32bits das ferramentas necessárias.

```
dpkg --add-architecture i386
apt-get update
apt-get install libncurses-dev bison flex build-essential gcc-multilib rpm libstdc++6:i386 libgcc1:i386 zlib1g:i386 libncurses5:i386
```

`libncurses-dev` é necessário para ter acesso ao menu de configuração do Kernel, e bison e flex para uso com a geração do uImage do kernel, os demais pacotes são para compilar o kernel.

## Compilando o kernel

## Clone do projeto do kernel

https://github.com/friendlyarm/linux-3.4.y

então execute os comandos:

```
make distclean
touch .scmversion
```

### Opções relacioandas ao PPP

Marque as seguintes opções para preparar o Kernel para uso com PPP
```
Device Drivers  --->
Network device support  --->
<M>   PPP (point-to-point protocol) support│  
[ ]     PPP multilink support (EXPERIMENTAL)
[ ]     PPP filtering
<M>     PPP support for async serial ports
<M>     PPP support for sync tty ports
<M>     PPP Deflate compression
<M>     PPP BSD-Compress compression
<M>     PPP MPPE compression (encryption) (EXPERIMENTAL)
< >     PPP over Ethernet (EXPERIMENTAL)
<M>     PPP over L2TP (EXPERIMENTAL)
```

## Compile o Kernel
```
make  CROSS_COMPILE=arm-linux- nanopi3_linux_defconfig
```

```
make  CROSS_COMPILE=arm-linux- menuconfig
```

```
make  CROSS_COMPILE=arm-linux- uImage
```

## Compile os Módulos

Compile os módulos e instale em um diretório temporário para gerar o arquivo compatado para transporta-lo.

```
make INSTALL_MOD_PATH=/tmp/nanopi-modules CROSS_COMPILE=arm-linux- modules
make INSTALL_MOD_PATH=/tmp/nanopi-modules CROSS_COMPILE=arm-linux- modules_install
```

Then strip the Linux kernel module, creat the compress lib
cd /tmp/nanopi-modules/lib/
find . -name \*.ko | xargs arm-linux-strip --strip-unneeded
tar czvf kernel-modules.tgz modules/




vboxmanage internalcommands listpartitions -r awdisk \\.\PhysicalDrive1



## Fontes

* http://wiki.friendlyarm.com/wiki/index.php/NanoPi
* http://nanopi.org/nanopi_development.html
* http://wiki.friendlyarm.com/wiki/index.php/NanoPi_M3
