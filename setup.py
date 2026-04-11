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


run("pkg install python -y")
run("pkg install figlet toilet git -y")
run("termux-setup-storage -y")


print(f"{Y}INSTALL LIBRARIES\n")

for lib in libs:
    print(f"{W}install {lib}...")
    subprocess.run([sys.executable, "-m", "pip", "install", lib])


print(f"\n{Y}SET ALIAS (FIX TERMUX)\n")

zshrc = os.path.expanduser("~/.zshrc")
bashrc = os.path.expanduser("~/.bashrc")

alias_line = "alias tdfps='bash ~/TD_120FPS/td'\n"

def add_alias(file):
    try:
        if os.path.exists(file):
            with open(file, "r") as f:
                data = f.read()
        else:
            data = ""

        if "alias tdfps=" not in data:
            with open(file, "a") as f:
                f.write("\n# TDx08 TOOL\n")
                f.write(alias_line)
            return True
    except:
        pass
    return False

ok1 = add_alias(zshrc)
ok2 = add_alias(bashrc)

if ok1 or ok2:
    print(f"{G}ALIAS ADDED")
else:
    print(f"{Y}ALIAS EXISTS")


run("source ~/.zshrc 2>/dev/null || source ~/.bashrc 2>/dev/null")

print(f"\n{G}SETUP DONE!")
print(f"{C}👉 Mở tool: tdfps")