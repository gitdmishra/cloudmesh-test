from subprocess import CalledProcessError

from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import banner
from cloudmesh.common.util import path_expand
from cloudmesh.common.console import Console
import os
import getpass
import platform
import socket
import sys
import psutil

"""
are you running in a vnenv
are you running python 3.8.1
are you running the 64 bit version of python
are you having the newest version of pip
is the default mongo port used
is cl installed

do you have docker installed
do you have vbox installed
is hyperv switched on or off
how much memory do you have
do you have free diskspace
are containers running
.... other tyings that can help us debug your environment 
"""

"""
find equifalent for windows

if os == "darwin":
    
    
Shell.run("df -h")

or maybe this works for all, e.g. use path, maybe we use pathlib and Path

from os import path
from shutil import disk_usage

print([i / 1000000 for i in disk_usage(path.realpath('/'))])
"""

"""
venvetest either one will work, i think

pip -V starts with user home dir

import sys

if hasattr(sys, 'real_prefix'):
   i am in vdir
   


test for os.environ['VIRTUAL_ENV']

"""


class Windows:

    def __init__(self):
        check = []

    def usage(self):
        hdd = psutil.disk_usage('/')
        print("Disk Space")
        print("Total: {total:.0f} GiB".format(total=hdd.total / (2 ** 30)))
        print("Used: {used:.0f} GiB".format(used=hdd.used / (2 ** 30)))
        print("Free: {free:.0f} GiB".format(free=hdd.free / (2 ** 30)))

        mem = psutil.virtual_memory()
        total = mem.total >> 30
        available = mem.available >> 30
        print (f"Memory: {available}GB free from {total}GB")

    def is_port_used(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0

    def is_venv(self):
        return (hasattr(sys, 'real_prefix') or
                (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

    def check_mongo(self):
        if platform.system() == "Windows":
            result = Shell.run("sc.exe query MongoDB")
            if "The specified service does not exist" in result \
                and "FAILED" in result:
                Console.ok("The MongoDB service is not running")
            else:
                Console.error("The MOngo DB service is running")
                Console.error(result)

            self.check_command("mongod.exe")  # find a good test

        if self.is_port_used(27017):
            Console.error("OK. he mongo port 27017 is already used")
        else:
            Console.ok("The mongo port 27017 is free")

    def check_python(self):
        length = platform.architecture()[0]
        if length == "32bit":
            Console.error("You run Python 32 bit")
        elif length == "64bit":
            Console.ok("OK. You run Python 64 bit")
        else:
            Console.error(f"Pythin is not 32 or 64 bit: {length}")

    def check_command(self, command, test=None, show=True):

        # banner(f"testing command: {command}")
        try:
            result = Shell.run(command).strip()

            if not test in result:
                if show:
                    Console.error(f"{test} not found in {result}")
                else:
                    Console.error("{command} not found")
            else:
                if show:
                    Console.ok(f"OK. {test} found in {result}")
                else:
                    Console.ok(f"OK. {command} found")

        except CalledProcessError:
            Console.error(f"command '{command}' not successful")

    #
    # TODO:  this should also work if you do return not name is ENV3
    #        use where python to find where ot is
    #        the username shoudl be in the path of the first python that shows
    #
    def check_venv(self, venv="~/ENV3"):

        # banner(f"checking python venv")

        if self.is_venv():
            Console.ok("OK. you are running in a venv")
            print("    VIRTUAL_ENV=", os.environ.get("VIRTUAL_ENV"), sep="")

        else:
            Console.error("You are not running in a venv")
        if "EVN3" not in os.environ.get("VIRTUAL_ENV"):
            Console.warning("your venv is not called ENV3. That may be ok")


        if platform.system() == "Windows":
            where = path_expand((venv))
            activate_path = where + "\\Scripts\\activate.bat"
            # check if the dir exists at where
            if os.path.isdir(where):
                Console.ok("OK. ENV3 directory exists")
            else:
                Console.error("ENV3 directory does not exists")

            # check if activate exists in ~\ENV3\Scripts\activate.bat
            if os.path.isfile(activate_path):
                Console.ok("OK. Activate exists in {activate_path}")
            else:
                Console.error("Could not find {activate_path}")

        # execute where pip and check if venv is in the path

        if platform.system() == "Windows":
            command = "where pip"
        else:
            command = "which pip"

    def is_venv_in_path(self, result, venv_path):

        result_list = result.split("\r\n")
        line = 0
        flag_venv = False

        for item in result_list:
            line = line + 1
            if venv_path in item:
                flag_venv = True
                break

        return flag_venv, line

    def is_user_name_valid(self):
        # banner("Check For User Name")
        username = getpass.getuser()

        if " " in username:
            Console.error("User name has spaces")
        else:
            Console.ok("OK. No spaces in user name")


if __name__ == "__main__":
    w = Windows()
    # w.check_command("python --version", test="3.8.1")
    # w.check_command("cl")
    # w.check_venv()
    # w.is_venv_exists()
    w.is_user_name_valid()
