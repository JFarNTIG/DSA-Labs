import sys
from folders import FolderManager
from windows_folders import WindowsFolderManager
from linux_folders import LinuxFolderManager

# It is common for programs to want to know the user's home directory.
# For example, a program might wish to store a settings file in a sensible place,
# or a game might need a place to store save files.

if sys.platform == "win32":
    folder_manager: FolderManager = WindowsFolderManager()
elif sys.platform == "linux":
    folder_manager: FolderManager = LinuxFolderManager()
else:
    raise NotImplementedError("No folder manager class is available for this OS")

print("Your home folder is:")
print(folder_manager.find_home_directory("jacoblewis.farnswor"))


# .....


# Somewhere else in the program, we may wish to check the drive root.
# If we don't have folder_manager variable left from earlier, this will look like:

if sys.platform == "win32":
    folder_manager: FolderManager = WindowsFolderManager()
elif sys.platform == "linux":
    folder_manager: FolderManager = LinuxFolderManager()
else:
    raise NotImplementedError("No folder manager class is available for this OS")

print("Your root folder is:")
print(folder_manager.find_system_base())