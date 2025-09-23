from manager_holder import ManagerHolder

holder = ManagerHolder.get()
folders = holder.get_folder_manager()

print("Your home folder is:")
print(folders.find_home_directory("jacoblewis.farnswor"))


holder = ManagerHolder.get()
folders = holder.get_folder_manager()

print("Your root folder is:")
print(folders.find_system_base())