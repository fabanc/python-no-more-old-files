# No more old files (Python)

## Description

This tool remove files that are older than a specific number of day. This tool requires Python 3.2 or above.
This project is hosted on a public repository: https://github.com/fabanc/python-no-more-old-files

## Usage:

The script expect the following parameters:
 - \-f or \-\- folder: The folder in which files will be removed. This parameter is mandatory.
 - \-d or \-\-days: The number of days. Files older than this number of days will be removed. This parameter is mandatory.
 - \-r or \-\-recursive: If used, the files in sub-folders will also be removed. This parameter is optional.
 - \-s or \-\-simulation: If used, the code will list the files but will not delete them. This parameter is optional.

Here is an example: `python.exe no_more_old_files.py -f "D:\Temp\python-remove" -d 0 -r`
You can also modify the batch file windows_task.bat and program it in Windows Task Scheduler  to run it.