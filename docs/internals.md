# Internals

The *internals* namespace hierarcy consists of a number of namespaces collecting calls for gaining low-level access to internal MakeHuman functionality.

In the vast majority of cases, you would benefit from first trying to find a relevant call elsewhere in the API, and as a last resort look here.

## getHuman()

Get the central human object.

## getApp()

Get the central app object.

## getSkeleton()

Get the human's skeleton, if any.

## numpyTypecodeToPythonTypeCode(numpyTypeCode)

Get the python array type code that is closest to the given numpy type code.

