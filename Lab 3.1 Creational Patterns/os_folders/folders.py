from abc import ABC, abstractmethod
from typing import Optional

class FolderManager(ABC):
    """Abstract class that represents a class that provides helper functions
    for finding special folders.
    """
    @abstractmethod
    def find_home_directory(self, username: str) -> Optional[str]:
        """Get the home directory of the specified user.

        Parameters:
        -- 
            - username: The user to get the home directory for.
        
        Returns:
        -- 
            - The path to the user's home directory, or None if no directory was found.
        """
        pass

    @abstractmethod
    def find_system_base(self) -> Optional[str]:
        """Get the system base directory, or (on Windows) the drive root.
        
        Returns:
        -- 
            - The path to the system base, or None if no system base was found.
        """
        pass