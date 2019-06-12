# Automatic Repository Creation

These script files help you to create an repository on github and do the initial commit of all the files present in the working directory.

You will need [PAT (Personal Access token)](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line) for these scripts.

Place the respective file accordingly in the directory where your files are present that are to be pushed.

## How to use
### create.bat
This file is made exclusively for windows. You can either direcly open the file or run it via command prompt.

``` batch
> create.bat <Repository Name> <Github Username> <PAT>
```

If you want to enter each field individually then you can run it:
``` batch
> create.bat
```

### create.sh
This file is made for linux distros. You can open the file directly or run it via terminal.

``` bash
$ bash create.sh <Repository Name> <PAT> 
```

If you want to enter each field individually then you can run it:

``` bash
$ bash create.sh
```

### create.py
This file can be run using python 3.xx.

``` python
python create.py <Repository Name> <PAT> 
```

If you want to enter each field individually then you can run it:

``` python
python create.py
```