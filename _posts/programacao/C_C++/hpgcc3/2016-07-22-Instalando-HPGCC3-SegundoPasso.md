Chapter 2 - Toolchain

Details
 Published: 14 April 2011
Chapter 2 - Installing a toolchain

In order to compile both the libraries and your own programs, we need a cross-compiling toolchain.

Getting the right toolchain

The preferred toolchain for HPGCC3 is the one provided with Ubuntu.

Open the Synaptic Package Manager, search for and install the following packages:

gcc-arm-none-eabi

gdb-arm-none-eabi

Note: For people using distributions other than Ubuntu, the correct compiler must support the armv4t platform. Some newer compilers that support only armv6 and up will not work for HPGCC3. Also, all Makefiles on HPGCC3 are meant for GNU Make, on platforms not using gnu make it has to be installed as the default 'make'.