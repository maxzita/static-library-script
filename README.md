# static-library-script
A script written in Python that facilitate the creation of a static library for C programs in Terminal.

## Requirements
Python3 version is required to use this script. Furthermore, this script is intend to use in GNU/Linux operating system.

## Preparation
It's recommended to clone this repository to your Download folder.

```
git clone https://github.com/andrewunifei/static-library-script ~/Downloads/staticLib
```
It's also recommended that you add the script's folder absolute path to your $PATH variable.

## Usage
As mentioned before, in order to use this script everywhere in your system, you need to add the script's folder absolute path to your $PATH variable (if you don't add this path, when you use the script, it'll be necessary to maintain a copy of the "staticLib" file in the same folder you're keeping your C files). Then you need to run ```staticLib``` command in the directory where your C files are.

##### While running
While the script is running, you have to enter the C file's name that will compose your static library. This script allows various files, but you need to enter one after another, you cannot enter all files in one line. After entering all C files, you just need to press RETURN KEY to go to the next step. In the next step you'll be asked to enter the executable file's name that will be outputted. After that, the script will delete all object files that it creates and everything will be ready to be used!
