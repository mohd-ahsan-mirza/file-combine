# Description
Command line tool to combine all files in the current directory by passing in the file extension
# Currently Supported Formats
All formats that `fopen` of python can handle
# Setup
After pulling the repo, add the following line in your ~/.bash_profile. Replace the path to the path where this project is pulled
```
alias combine='python3 {Absolute path of file-combine folder}/run.py'
```
To load the changes
```
source ~/.bash_profile
#How To Use
CD into the directory where all the files are
###Example usage
```
combine DAT
```
