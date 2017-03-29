# Internals

These are calls which you would normally not need to make. They give you low-level access to internal MakeHuman objects. In most cases 
you would do operations via calls in other namespaces, not directly on these. 

## getHuman()

Returns the central human object.

## getApp()

Returns the central "app" object.

## getSkeleton()

Returns the current Human's skeleton. This will return None if no skeleton is assigned.


