import os
from typing import Optional
from folders import FolderManager

class LinuxFolderManager(FolderManager):
    def find_system_base(self) -> Optional[str]:
        # On Linux, the root directory is always /.
        # It should always exist, but we check just in case.
        if os.path.isdir("/"):
            return "/"
        
        return None

    def find_home_directory(self, username: str) -> Optional[str]:
        # On Linux, home directories are of the form:
        # /home/jacob
        # /home/developer
        
        # However, for the root user, the home directory
        # is /root. We need to consider this as an exception.
        if username == "root" and os.path.isdir("/root"):
            return "/root"

        # On Linux, paths are case-sensitive.
        # So /home/jacob and /home/JACOB refer to *different*
        # directories.
        # We need to return exact, case-sensitive matches.

        # Simply check if a folder /home/<username> exists.
        # If so, return the path.
        candidate = os.path.join("/home", username)
        if os.path.isdir(candidate):
            return candidate

        return None