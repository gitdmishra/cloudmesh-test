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

        """

        w = Windows()

        venv = arguments.VENV or "~/ENV3"
        venv = path_expand(venv)

        w.check_venv(venv=venv)

        if not w.is_venv(venv=venv):
            Console.error("you forgot to cativate the venv")

        w.check_command("python --version", test="3.8.1")
        w.check_command("python --version", test="20.0.2")
        w.check_command("cl")
        w.check_command("nmake")

        return ""
