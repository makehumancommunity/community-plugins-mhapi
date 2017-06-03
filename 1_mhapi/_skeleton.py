#!/usr/bin/python

from .namespace import NameSpace

class Skeleton(NameSpace):
    """This namespace wraps call which work with skeleton, rig, poses and expressions."""

    def __init__(self,api):
        self.api = api
        NameSpace.__init__(self)
        self.trace()
        self.human = self.api.internals.getHuman()

    def getSkeleton(self):
        """Get the current skeleton, or None if no skeleton is assigned"""
        return self.human.getSkeleton()

    def getBaseSkeleton(self):
        """Get the internal default skeleton, which is independent on selected rig"""
        return self.human.getBaseSkeleton()

    def getPoseAsBoneDict(self):
        """Return a dict containing all bone rotations"""
        skeleton = self.getSkeleton()
        if skeleton is None:
            # No rig is set
            return None
        return None

    def getPoseAsBVH(self):
        """Return a BVH object describing the current pose"""
        skeleton = self.getSkeleton()
        if skeleton is None:
            # No rig is set
            return None
        b = BVH()
        b.fromSkeleton(skeleton)

        return b
 
    def clearPoseAndExpression(self):
        """Put skeleton back into rest pose"""
        human.resetToRestPose()
        human.removeAnimations()

    def setPoseFromFile(self, bvh_file_name):
        """Set the pose from a BVH file"""
        skeleton = self.getSkeleton()
        pass

    def setExpressionFromFile(self, mhposeFile):
        """Set the expression from a mhpose file"""
        skeleton = self.getSkeleton()
        pass

    def _loadBvh(self, bvh_file_name):
        pass

    def _createAnimationTrack(self, skeleton):
        pass

    def _calculateBVHBoneLength(self):
        pass

