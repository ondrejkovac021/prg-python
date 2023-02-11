import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_package("") # do zavorak zadat jmeno balíčku např. NumPy
