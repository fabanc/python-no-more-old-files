# python-no-more-old-files

## Description

This tool remove files that are older than a specific number of day. This tool requires Python 3.2 or above.

## Usage:

The script expect the following parameters:
 - \-f or \-\- folder: The folder in which files will be removed. This parameter is mandatory.
 - \-d or \-\-days: The number of days. Files older than this number of days will be removed. This parameter is mandatory.
 - \-r or \-\-recursive: If used, the files in sub-folders will also be removed. This parameter is optional.
 - \-s or \-\-simulation: If used, the code will list the files but will not delete them. This parameter is optional.

`no_more_old_files.py -f "D:\Temp\python-remove" -d 0 -r -s`