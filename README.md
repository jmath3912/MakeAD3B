![Syntec Logo](images/GlitchSyntec.gif)
# MakeAD3B [Beta]

**TEXT EDITOR // FILE CONVERTER // EASY TO USE**

---
MakeAD3B is a text editing program to convert dialogue script into a DOS 3.3 disk image, allowing users to essentially make their own D3B.DSK. 

This project is a fan creation for Project 863, an alternate-reality game created byn Matthias (Matthew Fredrick) and the rest of the team at Spellbound Inc. (formerly known as Hi5 Studios).

### **Prerequisites**
Before you use this program make sure you have the latest version of Python installed (I am working on setting up application files for the major operating systems, but in the meantime we have the Python file itself). The program will not work unless you have Python installed on your machine. Along with the Python installation, also be sure to install the latest version of pip if it is not automatically installed with Python.

Once Python is installed, download the project files from above onto your Desktop or wherever else you choose to keep the program. To download the program, click on the green dropdown menu that says `Code` and hit `'Download as ZIP.'` It will either prompt you for where you wish to save the zip file to *or* automatically download it to your default download location.

Once it downloads, navigate to the folder where the ZIP is and unzip it and open the new folder it creates. With this folder open, open the command prompt on the folder (type in `cmd` in the bar where the filepath is located) and type in the following command:

Windows:
```
pip install -r requirements.txt
```
MacOS/Linux:
```
pip3 install -r requirements.txt
```

This command may take some time to install all of the necessary packages (depending on your device and/or Internet speed). Once they have been installed, the command prompt will display a message saying that the packages have been successfully installed and it will begin awaiting another command. You may now close out of the command prompt.

### **Running the program**
Now that Python and all of the dependencies have been installed, we can now run the program. Navigate to the program folder and look for the file named `MakeAD3B.py` and double-click it. If Python is installed correctly, the program should open up and look a bit similar to Notepad on Windows or some other generic text editor.

When writing your dialogue script, keep in mind that any messages that you wish for Deb to type must be written as normal, but messages that you wish to respond with must be prefixed with a `>` followed by a space. An example is shown below:

```txt
Prompt needed.
> Hello
Prompt needed.
> What prompt?
Any valid prompt.
> sample text
Invalid prompt.
> sample text
Answer cannot be defined at this time, please try again later.
> sample text
Searching through logs, please wait....
Nelson Syphus is a threat, avoid contact.
> sample text
Nelson Syphus is the founder of Syntec Inc.
> sample text
```

If you cannot finish your script in one sitting, you may save the script to a txt file by going to `File -> Save` or `File -> Save As...`. It can be opened up again later by going to `File -> Open` and then clicking on the txt file you created.

When you are ready to create your dsk file, begin by pressing saving the current text in the text box using `File -> Save`. Once it's saved, press the `Convert` button at the bottom of the screen. The editor will prompt you to pick or create a temporary text file which will be used in the dsk file creation process. Select a file or write in the name that you wish for your dsk file to have and then press the `Open` button at the bottom of that menu. A progress bar will momentarily pop up as the file begins to be converted. You will see a confirmation popup appear once the dsk file has been created. When that popup appears, you are free to close out of MakeAD3B.

**WARNING**: Do NOT use any double-quotation marks ("") anywhere in your script. If you wish to use quotes, use single-quotes (' ') instead. Using any double-quotes will break your dsk file and cause it to not work as intended in the emulator.

### **How to use the .dsk file**
You now have your new dsk file, but there are a few steps that must be taken before you can properly use it as used in Project 863. The steps are as follows:

1. Open up the Apple ][ emulator of your choice and load in the .dsk file into one of the drives.
2. Press the RESET button on your emulator so the .dsk can be read.
3. Type in `CATALOG` into the emulator and press Enter. You will see text that looks almost similar to the text below:
```txt
DISK VOLUME 254
 T 040 FILENAME.TXT
```
4. Go back to MakeAD3B (do NOT close the emulator) and press the blue EXEC button and then quickly open up the emulator again. You have 5 seconds to switch to the emulator of your choice before MakeAD3B types out the `EXEC` command. If done correctly, the program should type in `EXEC` and then the name of TXT file (eg. `EXEC FILENAME.TXT`). If all is working properly, you should see a series of `]` prompts (probably as many `]` prompts as there are lines in your program) scroll up the screen, as shown below:
```basic
] EXEC FILENAME.TXT
]
]
]
]
]
]
]
```
5. Once the flashing cursor returns & your disk drive stops, type `LIST` & press the ENTER key. You should see a series of `PRINT` and `INPUT` statements scroll up the screen, as well as some of the lines of your script that you typed in MakeAD3B. 
6. Now go back to MakeAD3B and press the yellow INIT button and then quickly open up the emulator again. If done correctly, it should type in `INIT` and then the name of the dsk file (eg. `INIT FILENAME.DSK`). The emulator may freeze for a bit, but then the cursor will come back and your screen should look similar to the text below:
```basic
] INIT FILENAME.DSK
]
```
7. All you need to do now is to type `RUN MYPROGRAM.DSK`, where `MYPROGRAM` is replaced the dsk name you used in the `INIT` command (eg. `RUN D3B.DSK` or `RUN FILENAME.DSK`).

### *TO-DO*
- [x] Add auto-EXEC and auto-INIT feature to eliminate need to manually type EXEC and INIT in emulator
- [ ] Add user preferences and allow ability to remember session settings on startup
- [ ] Add built-in ASCII-cam similar to the one used in Project 863 (just for fun)
- [ ] Make packaged executable files for each of the major operating systems (Windows, MacOS, Linux, etc.)
- [ ] Add visuals of some sort or make a tutorial video to show how to use MakeAD3B and the associated dsk
- [x] Add themes under the Options Menu
