# Version

Information about hg and the current makehuman version.

## getBranch()

Returns the name of the current local code branch, for example 'default'. If this is not possible to deduce, None is returned.

## getRevision()

Return the full textual representation of the Hg revision, for example 'r1604 (d48f36771cc0)'. If this is not possible to deduce, None is returned.

## getRevisionId()

Returns the hash id of the current local revision as an integer, for example d48f36771cc0. If this is not possible to deduce, None is returned.

## getRevisionNumber()

Returns the number of the current local revision as an integer, for example 1604. If this is not possible to deduce, None is returned.

## getVersion()

Returns the full textual description of the current version, for example 'MakeHuman unstable 20141120' or 'MakeHuman 1.0.2'.

## getVersionNumberAsArray()

Returns the numeric representation of the version number as cells in an array, for example [1, 0, 2].

## getVersionNumberAsString()

Returns the string representation of the version number, for example '1.0.2'.


