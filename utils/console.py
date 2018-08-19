import subprocess
import os




class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def end_color(colored_text): return colored_text + bcolors.ENDC
def warning(warning):           return end_color(bcolors.WARNING    + warning)
def ok(ok):                     return end_color(bcolors.OKGREEN    + ok)
def bold(bold):                 return end_color(bcolors.BOLD       + bold)
def header(header):             return end_color(bcolors.HEADER     + header)
def identity(message):          return message # No if/elses needed when you have identity functions!


def cmd(command): return subprocess.check_output(command, shell=True)
def decorate(message, decorator):
    return decorator(message)
def message(message, decorator):
	print decorate(str(message), decorator)
def top(_message, decorator):
    print
    message(_message, decorator)
def down(_message, decorator):
    message(_message, decorator)
    print
def paragraph(_message, decorator):
    print
    message(_message, decorator)
    print
def printcmd(command, decorator):
	message(cmd(command), decorator)
