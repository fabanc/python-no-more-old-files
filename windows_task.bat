SET PYTHON_EXE="D:\arcgis-pro-envs\deep-learning\python.exe"
SET SCRIPT="D:\git\python-no-more-old-files\nomoreoldfiles\no_more_old_files.py"
SET FOLDER_TO_CLEAN="D:\Temp\python-remove"

echo Calling script
%PYTHON_EXE% %SCRIPT% -f %FOLDER_TO_CLEAN% -d 20 -s

echo Using robocopy to remove empty subfolders
robocopy %FOLDER_TO_CLEAN% %FOLDER_TO_CLEAN% /S /move
