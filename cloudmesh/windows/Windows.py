from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import banner
from cloudmesh.common.util import path_expand
from cloudmesh.common.console import Console

class Windows:

    @staticmethod
    def check_command(command, test=None):

        banner(f"testing command: {command}")
        result = Shell.run(command)

        print(result)

        print (f"test is {result} is in the output")
        if not test in result:
            Console.error("{result} is not in output")
        else:
            Console.ok("test passed")

    @staticmethod
    def check_venv(venv="~/ENV3"):
        where = path_expand((venv))

        # check if the dir exists at where
        raise NotImplementedError

        # check if activate exists in ~\ENV3\Scripts\activate.bat

        raise NotImplementedError

    def is_venv(venv="~/ENV3"):

        # execute where python and check if venv is in the path

        raise NotImplementedError

        # chek if venv path is the in the first line

        raise NotImplementedError

        # execute where pip and check if venv is in the path

        raise NotImplementedError

        # chek if venv path is the in the first line

        raise NotImplementedError

        return True