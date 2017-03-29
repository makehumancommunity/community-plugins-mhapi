# Locations

Gives you information about file and directory locations. 

## getUnicodeAbsPath(path)

Returns the abspath version of path, and ensures that it is correctly encoded

## getInstallationPath(subpath = "")

Returns the unicode-encoded absolute path to the directory which contains the makehuman.py file. If subpath is given, assume that a subdirectory is indicated and return the combined path.

## getUserDataPath(subpath = "")

Returns the unicode-encoded absolute path to the location of the user's "data" directory (as opposed to the installation's data directory). If subpath is given, assume that a subdirectory is indicated and return the combined path.

## getUserHomePath(subpath = "")

Returns the unicode-encoded absolute path to the location of the user's makehuman directory (i.e normally ~/makehuman). If subpath is given, assume that a subdirectory is indicated and return the combined path.

## getSystemDataPath(subpath = "")

Returns the unicode-encoded absolute path to the location of the installation's "data" directory (as opposed to the user's data directory). If subpath is given, assume that a subdirectory is indicated and return the combined path.

