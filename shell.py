

import subprocess
from typing import Tuple

def run_shell(command: str, __shell="/usr/bin/zsh"):
    """
        this is going to run 'sh' on your linux system
        not bash, not zsh, just sh
    """
    if not __shell:
        __shell = "/usr/bin/zsh"
    subprocess.call(command, shell=True, executable=__shell)


# this is now deprecated from subprocess.getoutput(cmd=...)
def get_process_output(command: str, __shell="/usr/bin/zsh"):

    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        executable=__shell)
    out, _ = process.communicate()
    out = out.decode("utf-8")
    return out


# TODO
# rename this to get_process_output
# after fixing the winit.py script
def get_output(command: str) -> str:
    return subprocess.getoutput(cmd=command)

def get_status_of_process_output(command: str) -> Tuple:
    return subprocess.getstatusoutput(cmd=command)

def get_exit_code(command: str) -> int:
    return subprocess.getstatusoutput(cmd=command)[0]











