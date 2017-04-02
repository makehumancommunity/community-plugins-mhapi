# Locations

This namespace wraps all calls that are related to file and directory locations.

## getUnicodeAbsPath(path)

Returns the abspath version of path, and ensures that it is correctly encoded

## getInstallationPath(subpath = "")

Returns the unicode-encoded absolut path to the directory which contains the makehuman.py file

## getSystemDataPath(subpath = "")

Returns the unicode-encoded absolute path to the location of the user's "data" directory (as opposed to the installation's data directory). If subpath is given, assume that a subdirectory is indicated and return the combined path.

## getUserHomePath(subpath = "")

Returns unicode-encoded absolute path to the location of the user's makehuman directory (i.e normally ~/makehuman).

## getUserDataPath(subpath = "")

Returns unicode-encoded absolute path to the location of the user's "data" directory (as opposed to the installation's data directory)

