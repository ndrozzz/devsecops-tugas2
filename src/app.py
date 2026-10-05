import shlex
import subprocess


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b


def run_command(cmd):
    # shell=False (default) + argumen berbentuk list -> tidak ada interpretasi shell
    args = shlex.split(cmd)
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
