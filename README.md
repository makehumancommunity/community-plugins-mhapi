# MHAPI

MHAPI is a set of convenience calls intented to help you get access to things which might be difficult to find in the code otherwise.
The main purpose is to serve as a base library for writing plugins for MakeHuman. 

## Installation and usage

If you place 1_mhapi in the plugins directory, it will self-register so that app.mhapi becomes available. Then (in a plugin or whatever
it is you are working with) you can make a call to one of MHAPI's functions. For example:

    from core import G
    someDir = G.app.mhapi.locations.getUserDataDir()

This would store the location of the "data" directory located amongst the user's makehuman files, i.e ~/makehuman/v1/data on a unixoid
system or MY DOCUMENTS\makehuman\v1\data on windows. 

## API reference

In the reference, "G.app.mhapi._NAMESPACE_" has been excluded. So the "getHuman()" call found on the "internals" page here is actuall called "G.app.mhapi.internals.getHuman()".

* [assets](docs/assets.md): These are calls related to reading, parsing and manipulating assets.
* [internals](docs/internals.md): These are calls which you would normally not need to make. They give you low-level access to internal MakeHuman objects. 
* [locations](docs/locations.md): Gives you information about file and directory locations. 
* [mesh](docs/mesh.md): Operations on and info about the mesh as such (ie direct access to vertices, edges and faces)
* [modifiers](docs/modifiers.md): Gives you control and information about modifiers and targets.
* [skeleton](docs/skeleton.md): Operations concerning aspects of skeleton, such as rig, pose, expression and similar.
* [ui](docs/ui.md): Operations for constructing and manipulating the UI
* [version](docs/version.md): Information about hg and the current makehuman version.
* [viewport](docs/viewport.md): Operations for manipulating the viewport and the camera

