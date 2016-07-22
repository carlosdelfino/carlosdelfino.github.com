Chapter 1 - Getting started

Details
 Published: 02 April 2011
This section will guide you step-by-step in the creation of a complete development environment.

- Installing a fresh operating system

To make it easier for everybody, this entire tutorial will be based on one operating system: Ubuntu Linux. So the first step is to install Ubuntu Desktop on either a computer or a virtual machine (preferred). To do the installation please follow the instructions on their website: www.ubuntu.com

If you need a virtual machine, there are multiple options like VMWare, VirtualBox, VirtualPC, Parallels, among others. Choose any virtual machine manager, create a new machine and perform a fresh install of Ubuntu.

Throughout this tutorial it will be assumed that the user name is 'user'. Once you have the Linux desktop installed and with all the latest updates, move to the next step.

- Installing required additional packages

Several packages are required for the development environment. These packages are not shown on the Ubuntu Software Manager. Use the Software Manager to search for and install the Synaptic Package Manager. Now using the Synaptic Package Manager, search and mark for installation the following packages:

gcc

libelf-dev

eclipse-cdt

Notice that some packages may already be installed on your system (gcc typically is). Hit Apply to get everything installed.