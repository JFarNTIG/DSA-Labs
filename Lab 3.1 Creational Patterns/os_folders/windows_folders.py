import os
from typing import Optional
from folders import FolderManager

class WindowsFolderManager(FolderManager):
    def find_system_base(self) -> Optional[str]:
        # On Windows, each drive has a different root directory.
        # The system drive is always C:\.
        # It should exist, but we check just in case.
        if os.path.isdir("C:\\"):
            return "C:\\"
        
        return None
    
    def find_home_directory(self, username: str) -> Optional[str]:
        base_path = r"C:\Users"
        if not os.path.isdir(base_path):
            return None

        # Windows paths are case-insensitive.
        # For example, "C:\Users\John" and "C:\Users\JOHN"
        # actually refers to the same folder.
        # 
        # We want to return case-insensitive matches as well,
        # so we have to enumerate all directories, and check
        # the paths as lowercase.
        username_lower = username.lower()

        try:
            for entry in os.scandir(base_path):
                if entry.is_dir() and entry.name.lower() == username_lower:
                    return entry.path
        except PermissionError:
            # On Windows, some folders may be protected (Administrator home folder, etc)
            # Checking such folders can result in an exception.
            # In this case, simply skip the protected folder.
            pass

        return None
