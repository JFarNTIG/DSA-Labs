from manager_factory import ManagerFactory

# It is common for programs to want to know the user's home directory.
# For example, a program might wish to store a settings file in a sensible place,
# or a game might need a place to store save files.

os_factory = ManagerFactory.get()
folders = os_factory.get_folder_manager()

print("Your home folder is:")
print(folders.find_home_directory("jacoblewis.farnswor"))


# .....


# Somewhere else in the program, we may wish to check the drive root.
# If we don't have os_factory variable left from earlier, this will look like:

os_factory = ManagerFactory.get()
folders = os_factory.get_folder_manager()

print("Your root folder is:")
print(folders.find_system_base())