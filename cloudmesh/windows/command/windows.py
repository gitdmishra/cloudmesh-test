from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.windows.Windows import Windows
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand

from cloudmesh.common.debug import VERBOSE

class WindowsCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_windows(self, args, arguments):
        """
        ::

          Usage:
                windows check [VENV]

          This command is intended to check if your windows set up is
          correctly done.

          Arguments:
              VENV  The location of the virtual environment. If not
                    specified it is ENV3 in your home directory

          Bugs:
              This program is supposed to be implemented. It is at this
              time just a template

          Description:

          Checks we do

             1. are you running python 3.8.1
             2. are you having the newest version of pip
             3. is cl installed
             4. is nmake installed
             5. is the username without spaces


          Checks that are missing or need implemented

             6. are you running in a vnenv
             7. is the default mongo port used
             8. do you have docker installed
             9. do you have vbox installed
            10. is hyperv switched on or off
            11. how much memory do you have
            12. do you have free diskspace
            13. are containers running
            14. .... other tyings that can help us debug your environment

        """

        w = Windows()

        venv = arguments.VENV or "~/ENV3"
        venv = path_expand(venv)

        w.check_venv(venv=venv)

        if not w.is_venv_exists(venv=venv):
            Console.error("you forgot to activate the venv")

        w.check_command("python --version", test="3.8.1")
        w.check_python()
        w.check_command("pip --version", test="20.0.2")
        w.check_command("cl")
        w.check_command("nmake")
        w.is_user_name_valid()
        return ""
