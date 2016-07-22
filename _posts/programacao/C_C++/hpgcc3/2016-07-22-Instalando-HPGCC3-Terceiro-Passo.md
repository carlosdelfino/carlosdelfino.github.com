Chapter 3 - Creating a development environment

Details
 Published: 03 May 2011
Installing the HPGCC3 libraries

From the Downloads section, get the latest file.

Create a main folder for your hpgcc3 installation. The name and location is not important, but for this tutorial the folder will be created in the user's home directory, and will be named 'hpgcc3'. From this point on, all references to "the hpgcc3 folder" will mean /home/user/hpgcc3/ in this tutorial.

Extract the downloaded file inside the new hpgcc3 folder. There are two main subdirectories, one called tools_workspace and one called libs_workspace. As the name suggests, these are Eclipse workspaces, one containing tools and the other containing the hpgcc3 libraries.

Building the tools

Start Eclipse. Go to the menu File -> Switch workspace -> Other... and select the tools_workspace directory. The IDE will close and reopen automatically. Now you should see on the left of the screen, the Project Explorer showing several projects.

These projects are the tools needed to build the HPGCC3 libraries, and also your own user programs. Go to the menu Project and select Build All..., or simply hit ctrl+B on the keyboard. The IDE will start to build and install all the necessary tools. You can keep an eye on the build progress by selecting "Build on background", and then finding the tab "Console" in the lower pane. Once the build is finished, there's one important step to follow.

There's an Eclipse plugin which cannot be installed automatically, since access to the Eclipse folders requires super user permissions. The build process that just finished created a script file on your desktop, so close Eclipse. It is important that Eclipse is closed (not just minimized), since a restart is required to load the new plugin. You should see a new icon 'install_plugin.sh'. Double click on it to run it, a dialog will pop up asking you what to do. It is very important that you select "Run in Terminal", otherwise it won't give you a chance to authorize the installation.

When prompted, type your user's password. Once the script finished the installation, log out and back into the operating system. This is to allow the OS to pick up the changes in the environment variables.

To verify if the plugin was correctly installed, open Eclipse and go to the menu File -> New -> C Project. A dialog pops up, and if everything went well you should see "HPGCC3 (Linux)" listed as one of the toolchains available when you choose an Empty executable file.

Building the libraries

Once the tools are built and installed, the first step to build the libraries is to supply a calculator ROM image, where the libraries will be installed on.

Open Eclipse, go to the menu File -> Switch workspace -> Other... and select the libs_workspace directory. The IDE will close and reopen automatically. Now you should see on the left of the screen, the Project Explorer showing several projects.

In the project explorer, find the project named 'make_rom', and open the project. Inside the project there is an empty folder named 'original_rom'. Get the latest rom image from HP website, or use your favorite rom version. The rom image is typically a .bin file of about 1.2 MBytes in size. Copy this file into the 'original_rom' folder. Failure to provide a valid rom image will result in errors.

Go to the menu Project and select Build All..., or simply hit ctrl+B on the keyboard. The IDE will start to build and install all the necessary libraries. You can keep an eye on the build progress by selecting "Build on background", and then finding the tab "Console" in the lower pane. Once the build is finished, exit Eclipse.

Congratulations, HPGCC3 is now built and installed on your IDE.

Cleaning up

Once the build process finished, you can safely delete the directories 'tools_workspace' and 'libs_workspace' since they are no longer needed. It could be advantageous for the seasoned programmer to keep the 'libs_workspace' directory, in order to quickly take a peek at HPGCC3 sources when needed for reference.