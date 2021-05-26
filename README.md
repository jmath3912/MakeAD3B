![Syntec Logo](/images/Syntec_BlackTrans_2x_PNG_(1).png)

# MakeAD3B
MakeAD3B is a text editor program to convert dialogue script into DOS 3.3 disk image containing text file with Applesoft BASIC commands.

This project is a fan creation for Project 863, an alternate-reality game created byn Matthias and the rest of the team at Spellbound Inc. (formerly known as Hi5 Studios).

### Prerequisites
Before you use this program make sure you have the latest version of Python installed (I am working on setting up application files for the major operating systems, but in the meantime we have the Python file itself). The program will not work unless you have Python installed on your machine. Along with the python installation, also be sure to install the latest version of pip if it is not automatically installed with Python.

Once python is installed, download the project files from above onto your Desktop or wherever else you choose to keep the program. Then with the folder open, open the command prompt on the folder and type in the following command:

Windows:
```
pip install -r requirements.txt
```

MacOS/Linux:
```
pip3 install -r requirements.txt
```

### **Running the program**
Now that Python and all of the dependencies have been installed, we can now run the program. Navigate to the program folder and look for the file named `MakeAD3B.py` and double-click it. If Python is installed correctly, the program should open up and look a bit similar to Notepad on Windows or some other generic text editor.

When writing your dialogue script, keep in mind that any messages that you wish for Deb to type must be written as normal, but messages that you wish to respond with must be prefixed with a `>` followed by a space. An example is shown below.



### **How to use the .dsk file**
sample text

### TO-DO
- [ ] Automatically reformat .dsk file so it works as an Applsoft BASIC file immediately
- [ ] Add checkboxes to toggle deletion of new, converted text file.
- [x] Add themes under the Options Menu
