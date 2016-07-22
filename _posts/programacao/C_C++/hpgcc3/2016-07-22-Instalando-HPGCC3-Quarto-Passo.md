Chapter 4 - Installing HPGCC3 on your calculator

Details
 Published: 02 June 2011
Installing HPGCC3 on your calculator

HPGCC3 libraries are designed to be installed in ROM to release more RAM memory for the user data. Therefore, installing HPGCC3 on your calculator involves flashing a custom ROM image file on your calculator.

** WARNING: READ THIS BEFORE FLASHING **

The HPGCC3 rom image takes more space than the original rom from HP. This means that by flashing the custom HPGCC3 rom on your calculator, you might be overwriting some of your libraries and data in port 2. To prevent any data loss please read through the following sections completely before flashing the new rom. You have been warned, the HPGCC3 Team will not be responsible for data loss caused by the installation of the new rom.

Preparing your calculator

NOTE: You only need to prepare your calculator if HPGCC3 was never before installed. It is not required to upgrade to a newer version of HPGCC3.

Before flashing the new rom, you need to move your data and libraries out of the way, so they won't be overwritten by HPGCC3 lirbaries. To do that, you need to use FlashTools (you can download it from here). In that package there is a program called FMAN.BIN, that you need to download to your calculator via USB or by copying it on an SD card. Then, execute (EVAL) the program. You should see a browser style window with several numbers and letters on top.

Using your left and right cursor keys, highlight the number 8 right next to the word "FLASH". This number is the user flash bank number (internally, flash memory is divided in banks, being banks 8 through 13 available to the user as Port 2). If this bank contains any libraries or data, they will be listed on the screen and will have to be moved to another bank, because HPGCC3 will use bank 8 and 9. For each item, use the cursors up and down to highlight, then F1 to cut, use the left and right cursors to go to another bank with enough free space (use banks A through D, since 8 and 9 will be taken by HPGCC3) and paste the item. You should see the new item listed in the new bank. Now go back to bank 8, and the item that was moved will still be listed, but with a letter D shown to the left of the name (the letter D stands for "deleted", indicating the library was indeed moved, this is normal). Repeat the procedure for all items, until all items were moved to another bank.

Now go to bank 9 and do the same thing, everything must be cut and pasted to another bank (A through D). Repeat until all items have been moved.

It is important to make one final check to make sure each and every deleted item on banks 8 and 9 is properly listed in the bank where you pasted it (make sure the D mark is not present or you won't have the library or data available for use).

Once you are absolutely sure that all the information on banks 8 and 9 was safely moved, you can press On to exit the program. Since moving libraries can affect the calculator, it cannot continue and needs to be restarted by pressing On-C. The preogram will request this on the screen, just follow the instructions.

Your calculator should restart normally, and is now ready to receive HPGCC3.

Now where is the ROM?

After a successful build, your main hpgcc3 directory should contain a directory named 'rom', and inside it there will be a .bin file. This is the file you need to flash to your calculator. There is also the accompanying file update.scp just like in the official rom distribution. Follow the standard procedures (see the instructions that come with the original ROM from HP) to flash this rom image into the calculator. Once the procedure is complete your calculator will boot normally.

Go to the LIB menu (RShift-2) and you should see HPGCC listed as one of the installed libraries, with one single command inside called RLVER, which displays the installed version of the HPGCC3 library.

Congratulations, your calculator has HPGCC3 installed and ready to execute C programs.