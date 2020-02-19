from subprocess import CalledProcessError

from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import banner
from cloudmesh.common.util import path_expand
from cloudmesh.common.console import Console
import os
import getpass

class Windows:

    def check_command(self,command, test=None):

        banner(f"testing command: {command}")
        try:
            result = Shell.run(command)

            print(f"{test} is {result} is in the output")
            if not test in result:
                Console.error("{result} is not in output")
            else:
                Console.ok("test passed")

        except CalledProcessError:
            Console.error(f"command '{command}' not successful")
        #print(result)



    def check_venv(self, venv="~/ENV3"):

        banner(f"checking python environment setup")

        where = path_expand((venv))
        activate_path = where + "\\Scripts\\activate.bat"
        # check if the dir exists at where
        if os.path.isdir(where):
            Console.ok("ENV3 directory exists")
        else:
            raise NotImplementedError

        # check if activate exists in ~\ENV3\Scripts\activate.bat
        if os.path.isfile(activate_path):
            Console.ok("Activate exists")
        else:
            raise NotImplementedError

    def is_venv_exists(self, venv="~/ENV3"):
        venv_path = path_expand((venv))

        # execute where python and check if venv is in the path

        command = "where python"
        result = Shell.run(command)
        flag_venv,line = self.is_venv_in_path(result, venv_path)

        if flag_venv:
            Console.ok(f"'{command}' : venv is in path")
        else:
            raise NotImplementedError

        # chek if venv path is the in the first line
        if line == 1:
            Console.ok(f"'{command}' : venv is in first line")
        else:
            raise NotImplementedError

        # execute where pip and check if venv is in the path

        command = "where pip"
        result = Shell.run(command)
        flag_venv, line = self.is_venv_in_path(result, venv_path)

        if flag_venv:
            Console.ok(f"'{command}' : venv is in path")
        else:
            raise NotImplementedError

        # chek if venv path is the in the first line
        if line == 1:
            Console.ok(f"'{command}' : venv is in first line")
        else:
            raise NotImplementedError


        # raise NotImplementedError

        # chek if venv path is the in the first line

        # raise NotImplementedError

        return True

    def is_venv_in_path(self,result,venv_path):

        result_list = result.split("\r\n")
        line = 0
        flag_venv = False

        for item in result_list:
            line = line + 1
            if venv_path in item:
                flag_venv = True
                break

        return flag_venv,line

    def is_user_name_valid(self):
        banner("Check For User Name")
        username = getpass.getuser()

        if " " not in username:
            Console.ok("No spaces in user name")
        else:
            Console.error("User name has spaces")

if __name__=="__main__":
    w = Windows()
    # w.check_command("python --version", test="3.8.1")
    # w.check_command("cl")
    # w.check_venv()
    # w.is_venv_exists()
    w.is_user_name_valid()