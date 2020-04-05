#!/usr/bin/python3

# On ubuntu you need "apt-get install pylint3" and the command is called
# "pylint3". On other platforms you might want to change this.
# 
# I never tested if this even works on windows. 

PYLINT="pylint3"

import os, sys, subprocess

if not "MAKEHUMAN_DIR" in os.environ or not os.environ.get("MAKEHUMAN_DIR"):
    print("You need set the environment variable MAKEHUMAN_DIR so that it points at the directory containing makehuman.py")
    sys.exit(1)

mhpath = os.path.abspath(os.environ.get("MAKEHUMAN_DIR"))
print("Makehuman directory is " + mhpath)

sys.path.append(mhpath)
sys.path.append(os.path.join(mhpath, "apps"))
sys.path.append(os.path.join(mhpath, "core"))
sys.path.append(os.path.join(mhpath, "lib"))
sys.path.append(os.path.join(mhpath, "shared"))

os.environ["PYTHONPATH"] = ":".join(sys.path)

#print(os.environ["PYTHON_PATH"])

os.system(PYLINT + " > pylint.log " + " 1_mhapi")


