# pi-file-splitter
[2017] A Python3 script which splits files into a user-defined character amount, and can find files by matching the content in the files with user-defined content. Built for functionality on a Raspberry Pi.

## Usage
If “file_splitter.py” is in “Desktop/splitting/,“ to direct to it you would type the following: cd Desktop/splitting
And to run it you would type the following: python3 fill_splitter.py

## Splitting
FileSplitter Splitting mode allows the splitting of a text file into multiple files. The files are split into a folder matching the name of the original file + “minis”
### Example:
If a file under the name of “apples.txt” is split, it will split into a file by the name of “apples.txtminis.“

## Matching
When prompted to enter the directory of the files you’d like to match with, enter the directory based on the directory you’re already in.
### Example:
If “apples.txtminis” is in “Desktop/splitting/,” you would simply enter “apples.txtminis” rather than “Desktop/splitting/apples.txtminis”.
