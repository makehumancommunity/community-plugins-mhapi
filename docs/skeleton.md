# Skeleton

This namespace wraps call which work with skeleton, rig, poses and expressions.

## getSkeleton()

Get the current skeleton, or None if no skeleton is assigned

## getBaseSkeleton()

Get the internal default skeleton, which is independent on selected rig

## getPoseAsBoneDict()

Return a dict containing all bone rotations

## getPoseAsBVH()

Return a BVH object describing the current pose

## getPoseAsAnimation()

## clearPoseAndExpression()

Put skeleton back into rest pose

Set the pose from a BVH file

## setExpressionFromFile(mhposeFile)

Set the expression from a mhpose file

