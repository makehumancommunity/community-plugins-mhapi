#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MakeHuman debian package build script

**Project Name:**      MakeHuman

**Product Home Page:** http://www.makehuman.org/

**Code Home Page:**    https://bitbucket.org/MakeHuman/makehuman/

**Authors:**           Joel Palmius, Jonas Hauquier

**Copyright(c):**      MakeHuman Team 2001-2017

**Licensing:**         AGPL3

    This file is part of MakeHuman (www.makehuman.org).

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Abstract
--------

Create a debian DEB package for a plugin
"""

import sys
import os
import re
import subprocess
import shutil
import glob
import time

# --- CONFIGURATION SETTINGS --- 

settings = dict()

settings["package_base_name"] = "makehuman-community-plugins-mhapi"
settings["package_sub"] = "1ppa1"
settings["tree_to_copy"] = "1_mhapi"
settings["signString"] = "Joel Palmius <joepal1976@hotmail.com>"
settings["performSign"] = True
settings["performUpload"] = False
settings["gitpath"] = "/usr/bin/git"
settings["build_root"] = os.path.join("/tmp",settings["package_base_name"] + "_ppa_work")

# --- SECONDARY CONFIGURATION

settings["location_of_script"] = os.path.dirname(os.path.abspath(__file__))
settings["source_root"] = os.path.join(settings["location_of_script"], '..')
settings["ppa_work"] = os.path.join(settings["source_root"], "..", "work")
settings["binary_final_dest"] = os.path.join(settings["ppa_work"],"dist_deb")
settings["source_final_dest"] = os.path.join(settings["ppa_work"],"dist_ppa")
settings["timestamp"] = time.strftime("%Y%m%d%H%M%S")
settings["deb_config_location"] = os.path.join(settings["location_of_script"])
settings["deb_staging_location"] = os.path.join(settings["build_root"],settings["package_base_name"]) 
settings["main_deb_def"] = os.path.join(settings["deb_staging_location"],"debian")
settings["main_changelog"] = os.path.join(settings["main_deb_def"],"changelog")

# .orig tarball to create
fn = settings["package_base_name"] + "_" + settings["timestamp"] + ".orig.tar.gz"
settings["main_tar_file"] = os.path.abspath(os.path.join(settings["build_root"], fn))

print("--- SETTINGS ---")
for key in settings:
  print(key.ljust(20) + ": " + str(settings[key]))
print(" --- ")

# --- EVERYTHING BELOW THIS POINT IS LOGIC, HANDS OFF ---

print("Source root: " + settings["source_root"])
if not os.path.isdir( os.path.join(settings["source_root"], '.git') ):
  print("Error, the git root folder %s does not contain .git folder!" % settings["source_root"])
  print("Giving up.\n\n");
  sys.exit(1)

def _sed_replace(filepath, templateToken, replaceStr):
  subprocess.check_call(['sed', '-i', '-e', 's/%s/%s/' % (templateToken, replaceStr), filepath])

def buildSourceTree():
  if os.geteuid() != 0:
    print("WARNING: You are not root. You should be running this script with root permissions!")

  if os.path.exists(settings["build_root"]):
    # Ensure dest dir is empty
    shutil.rmtree(settings["build_root"])
  os.mkdir(settings["build_root"])

  print("\nABOUT TO COPY CONTENTS\n")

  srcDir = os.path.join(settings["source_root"],settings["tree_to_copy"])
  destDir = os.path.join(settings["build_root"],settings["tree_to_copy"])

  if destDir and destDir != "" and destDir != "/" and os.path.exists(destDir):
    subprocess.check_call(["rm", "-rf", destDir])

  subprocess.check_call(["cp", "-rfv", srcDir, destDir])

  shutil.copytree(settings["deb_config_location"],settings["deb_staging_location"])

  subprocess.check_call(["rm", "-rf", os.path.join(settings["deb_staging_location"],"buildPPA.py")])

  try:
    subprocess.check_call(["chown", "-R", "0:0", settings["build_root"]])
  except:
    print("Failed to chown to root. Operation not permitted?")
  try:
    subprocess.check_call(["chmod", "-R", "644", settings["build_root"]])
    for path, dirs, files in os.walk(settings["build_root"]):
      for d in dirs:
        dpath = os.path.join(settings["build_root"], path, d)
        try:
          subprocess.check_call(["chmod", "755", dpath])
        except:
          print("Failed to chmod 755 folder %s" % dpath)
    subprocess.check_call(["chmod", "755", settings["build_root"]])
  except Exception as e:
    print("Failed to chmod " + settings["build_prepare_destination"])
    print(e)

  dummy = os.path.join(settings["build_root"],"dummy.txt")

  with open(dummy, "w") as text_file:
    text_file.write("This is only because moronic debuild cannot handle tarballs which doesn't have a non-dir entry in the root")


def createSourceTarballs():
  print("\nABOUT TO CREATE SOURCE TARBALL\n\n");

  os.chdir(settings["build_root"])

  print("Tarfile: " + settings["main_tar_file"])
  print("CWD: " + os.getcwd())

  args = ["tar","-C",settings["build_root"],"-czf", settings["main_tar_file"], settings["tree_to_copy"], "dummy.txt"]
  print(args)
  subprocess.check_call(args)

def createSourceDebs():

  print("\nWRITING CHANGELOGS\n")

  #ts = Mon, 01 Jun 2015 15:17:49 +0200

  ts = time.strftime("%a, %d %b %Y %H:%M:%S +0200")

  with open(settings["main_changelog"], "w") as text_file:
    text_file.write(settings["package_base_name"] + " (" + settings["timestamp"] + "-" + settings["package_sub"] + ") bionic; urgency=low\n\n")
    text_file.write("  * Version bump\n\n")
    text_file.write(" -- " + settings["signString"] + "  " + ts + "\n\n")

  print("\nSTARTING TO BUILD SOURCE DEB DEFINITIONS\n")
  
  print("Unpacking " + settings["main_tar_file"])
  subprocess.check_call(["tar","-C",settings["deb_staging_location"],"-xzf", settings["main_tar_file"]])

  os.chdir(settings["main_deb_def"])

  print("Debuilding in " + os.getcwd())

  if not settings["performSign"] is None and not settings["performSign"]:
    subprocess.check_call(["debuild","-S","-sa","-uc","-us"])
  else:
    subprocess.check_call(["debuild","-S","-sa"])

  print("Copying source deb output to " + settings["source_final_dest"])

  for f in glob.glob(settings["deb_staging_location"] + "/*ppa*"):
    print(f)                                                                                                                                        
    shutil.copy(f, settings["source_final_dest"])

  print("Copying source tarballs to " + settings["source_final_dest"])

  for f in glob.glob(settings["deb_staging_location"] + "/*.orig.*"):
    print(f)                                                                                                                                        
    shutil.copy(f, settings["source_final_dest"])

def createBinaryDebs():
  print("\nSTARTING TO BUILD DEB FILES\n")
  
  os.chdir(settings["main_deb_def"])

  print("Debuilding in " + os.getcwd())

  if not settings["performSign"] is None and not settings["performSign"]:
    subprocess.check_call(["debuild","-uc","-us"])
  else:
    subprocess.check_call(["debuild"])

  print("Copying deb files to " + settings["binary_final_dest"])

  for f in glob.glob(settings["deb_staging_location"] + "/*.deb"):
    print(f)                                                                                                                                        
    shutil.copy(f, settings["binary_final_dest"])

if __name__ == '__main__':
  buildSourceTree()
  createSourceTarballs()
  createSourceDebs()
  createBinaryDebs()

