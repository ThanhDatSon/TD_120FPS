import os
import subprocess
import sys
from colorama import Fore, init

init(autoreset=True)

G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.WHITE

libs = [
    "colorama",
    "requests",
    "rich",
    "zstandard",
    "pycryptodome"
]


def run(cmd):
    print(f"{C}{cmd}")
    subprocess.run(cmd, shell=True)


print(f"{G}ĐANG SETUP TOOL...\n")


run("pkg update -y")
run("pkg install python -y")
run("pkg install figlet toilet git -y")


print(f"{Y}INSTALL LIBRARIES\n")

for lib in libs:
    print(f"{W}install {lib}...")
    result = subprocess.run([sys.executable, "-m", "pip", "install", lib])

    if result.returncode == 0:
        print(f"{G}OK {lib}")
    else:
        print(f"{R}FAIL {lib}")


print(f"\n{Y}SET ALIAS\n")

bashrc = os.path.expanduser("~/.bashrc")
alias_line = "alias tdfps=/data/data/com.termux/files/home/TD_120FPS/td"
\n"

try:
    with open(bashrc, "r") as f:
        data = f.read()
except:
    data = ""

if "alias tdfps=" not in data:
    with open(bashrc, "a") as f:
        f.write("\n# TDx08 TOOL\n")
        f.write(alias_line)
    print(f"{G}ALIAS ADDED")
else:
    print(f"{Y}ALIAS EXISTS")


print(f"\n{G}SETUP DONE!")
print(f"{C}Nhập tdfps để mở tool\n")