import sys
from folders import FolderManager
from linux_folders import LinuxFolderManager
from windows_folders import WindowsFolderManager

_created = None

class ManagerFactory:
    def __init__(self):
        """Create a new ManagerFactory.

        Raises:
        --
            - NotImplementedError if the user's platform is not supported.
        """
        if sys.platform == "win32":
            self.folder_manager: FolderManager = WindowsFolderManager()
        elif sys.platform == "linux":
            self.folder_manager: FolderManager = LinuxFolderManager()
        else:
            raise NotImplementedError("No folder manager class is available for this OS")

    @staticmethod
    def get() -> "ManagerFactory":
        """Get the singleton instance of ManagerFactory."""
        global _created
        if _created is None:
            _created = ManagerFactory()
        return _created

    def get_folder_manager(self) -> FolderManager:
        """Get a folder manager specific to the current platform (Windows or Linux).
        """
        return self.folder_manager
        
        