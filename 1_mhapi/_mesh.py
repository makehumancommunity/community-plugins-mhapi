#!/usr/bin/python

from .namespace import NameSpace

class Mesh(NameSpace):
    """This namespace wraps call which works directly on mesh vertices, edges and faces."""

    def __init__(self,api):
        self.api = api
        NameSpace.__init__(self)
        self.trace()

    def getVertexCoordinates(self):
        """Return an array with the current position of vertices"""
        self.trace()
        human = self.api.internals.getHuman()
        return human.mesh.coord

    def getAllProxies(self, includeBaseMesh=False):
        human = self.api.internals.getHuman()
        return human.getProxies(includeBaseMesh)

    def getCurrentProxy(self):
        return self.api.internals.getHuman().proxy

    def getCurrentHair(self):
        return self.api.internals.getHuman().hairProxy

    def getCurrentEyes(self):
        return self.api.internals.getHuman().eyesProxy

    def getCurrentEyebrows(self):
        return self.api.internals.getHuman().eyebrowsProxy

    def getCurrentEyelashes(self):
        return self.api.internals.getHuman().eyelashesProxy

    def getCurrentTeeth(self):
        return self.api.internals.getHuman().teethProxy

    def getCurrentTongue(self):
        return self.api.internals.getHuman().tongueProxy

    def getClothes(self):
        human = self.api.internals.getHuman()
        return list(human._clothesProxies.values())

    def getFaceGroupFaceIndexes(self):
        faceGroups = []
        faceGroups.append({"name": "body", "first": 0, "last": 13378})
        faceGroups.append({"name": "helper-genital", "first": 17793, "last": 17975})
        faceGroups.append({"name": "helper-hair", "first": 17455, "last": 17653})
        faceGroups.append({"name": "helper-l-eye", "first": 17653, "last": 17723})
        faceGroups.append({"name": "helper-l-eyelashes-1", "first": 18152, "last": 18163})
        faceGroups.append({"name": "helper-l-eyelashes-2", "first": 18140, "last": 18152})
        faceGroups.append({"name": "helper-lower-teeth", "first": 18023, "last": 18071})
        faceGroups.append({"name": "helper-r-eye", "first": 17723, "last": 17793})
        faceGroups.append({"name": "helper-r-eyelashes-1", "first": 18244, "last": 18255})
        faceGroups.append({"name": "helper-r-eyelashes-2", "first": 18232, "last": 18244})
        faceGroups.append({"name": "helper-skirt", "first": 16771, "last": 17455})
        faceGroups.append({"name": "helper-tights", "first": 18479, "last": 18480})
        faceGroups.append({"name": "helper-tongue", "first": 18255, "last": 18479})
        faceGroups.append({"name": "helper-upper-teeth", "first": 17975, "last": 18023})
        faceGroups.append({"name": "joint-ground", "first": 18480, "last": 18486})
        faceGroups.append({"name": "joint-head-2", "first": 16747, "last": 16753})
        faceGroups.append({"name": "joint-head", "first": 16375, "last": 16381})
        faceGroups.append({"name": "joint-jaw", "first": 16729, "last": 16735})
        faceGroups.append({"name": "joint-l-ankle", "first": 16195, "last": 16201})
        faceGroups.append({"name": "joint-l-clavicle", "first": 16363, "last": 16369})
        faceGroups.append({"name": "joint-l-elbow", "first": 16351, "last": 16357})
        faceGroups.append({"name": "joint-l-eye", "first": 16027, "last": 16033})
        faceGroups.append({"name": "joint-l-eye-target", "first": 16387, "last": 16393})
        faceGroups.append({"name": "joint-l-finger-1-1", "first": 16327, "last": 16333})
        faceGroups.append({"name": "joint-l-finger-1-2", "first": 16321, "last": 16327})
        faceGroups.append({"name": "joint-l-finger-1-3", "first": 16315, "last": 16321})
        faceGroups.append({"name": "joint-l-finger-1-4", "first": 16309, "last": 16315})
        faceGroups.append({"name": "joint-l-finger-2-1", "first": 16303, "last": 16309})
        faceGroups.append({"name": "joint-l-finger-2-2", "first": 16261, "last": 16267})
        faceGroups.append({"name": "joint-l-finger-2-3", "first": 16255, "last": 16261})
        faceGroups.append({"name": "joint-l-finger-2-4", "first": 16213, "last": 16219})
        faceGroups.append({"name": "joint-l-finger-3-1", "first": 16297, "last": 16303})
        faceGroups.append({"name": "joint-l-finger-3-2", "first": 16267, "last": 16273})
        faceGroups.append({"name": "joint-l-finger-3-3", "first": 16249, "last": 16255})
        faceGroups.append({"name": "joint-l-finger-3-4", "first": 16219, "last": 16225})
        faceGroups.append({"name": "joint-l-finger-4-1", "first": 16291, "last": 16297})
        faceGroups.append({"name": "joint-l-finger-4-2", "first": 16273, "last": 16279})
        faceGroups.append({"name": "joint-l-finger-4-3", "first": 16243, "last": 16249})
        faceGroups.append({"name": "joint-l-finger-4-4", "first": 16225, "last": 16231})
        faceGroups.append({"name": "joint-l-finger-5-1", "first": 16285, "last": 16291})
        faceGroups.append({"name": "joint-l-finger-5-2", "first": 16279, "last": 16285})
        faceGroups.append({"name": "joint-l-finger-5-3", "first": 16237, "last": 16243})
        faceGroups.append({"name": "joint-l-finger-5-4", "first": 16231, "last": 16237})
        faceGroups.append({"name": "joint-l-foot-1", "first": 16075, "last": 16081})
        faceGroups.append({"name": "joint-l-foot-2", "first": 16069, "last": 16075})
        faceGroups.append({"name": "joint-l-hand-2", "first": 16339, "last": 16345})
        faceGroups.append({"name": "joint-l-hand-3", "first": 16333, "last": 16339})
        faceGroups.append({"name": "joint-l-hand", "first": 16345, "last": 16351})
        faceGroups.append({"name": "joint-l-knee", "first": 16201, "last": 16207})
        faceGroups.append({"name": "joint-l-lowerlid", "first": 16381, "last": 16387})
        faceGroups.append({"name": "joint-l-scapula", "first": 16369, "last": 16375})
        faceGroups.append({"name": "joint-l-shoulder", "first": 16357, "last": 16363})
        faceGroups.append({"name": "joint-l-toe-1-1", "first": 16189, "last": 16195})
        faceGroups.append({"name": "joint-l-toe-1-2", "first": 16183, "last": 16189})
        faceGroups.append({"name": "joint-l-toe-1-3", "first": 16177, "last": 16183})
        faceGroups.append({"name": "joint-l-toe-2-1", "first": 16171, "last": 16177})
        faceGroups.append({"name": "joint-l-toe-2-2", "first": 16129, "last": 16135})
        faceGroups.append({"name": "joint-l-toe-2-3", "first": 16123, "last": 16129})
        faceGroups.append({"name": "joint-l-toe-2-4", "first": 16117, "last": 16123})
        faceGroups.append({"name": "joint-l-toe-3-1", "first": 16165, "last": 16171})
        faceGroups.append({"name": "joint-l-toe-3-2", "first": 16135, "last": 16141})
        faceGroups.append({"name": "joint-l-toe-3-3", "first": 16105, "last": 16111})
        faceGroups.append({"name": "joint-l-toe-3-4", "first": 16111, "last": 16117})
        faceGroups.append({"name": "joint-l-toe-4-1", "first": 16159, "last": 16165})
        faceGroups.append({"name": "joint-l-toe-4-2", "first": 16141, "last": 16147})
        faceGroups.append({"name": "joint-l-toe-4-3", "first": 16093, "last": 16099})
        faceGroups.append({"name": "joint-l-toe-4-4", "first": 16099, "last": 16105})
        faceGroups.append({"name": "joint-l-toe-5-1", "first": 16153, "last": 16159})
        faceGroups.append({"name": "joint-l-toe-5-2", "first": 16147, "last": 16153})
        faceGroups.append({"name": "joint-l-toe-5-3", "first": 16081, "last": 16087})
        faceGroups.append({"name": "joint-l-toe-5-4", "first": 16087, "last": 16093})
        faceGroups.append({"name": "joint-l-upper-leg", "first": 16207, "last": 16213})
        faceGroups.append({"name": "joint-l-upperlid", "first": 16393, "last": 16399})
        faceGroups.append({"name": "joint-mouth", "first": 16765, "last": 16771})
        faceGroups.append({"name": "joint-neck", "first": 16723, "last": 16729})
        faceGroups.append({"name": "joint-pelvis", "first": 16039, "last": 16045})
        faceGroups.append({"name": "joint-r-ankle", "first": 16525, "last": 16531})
        faceGroups.append({"name": "joint-r-clavicle", "first": 16693, "last": 16699})
        faceGroups.append({"name": "joint-r-elbow", "first": 16681, "last": 16687})
        faceGroups.append({"name": "joint-r-eye", "first": 16033, "last": 16039})
        faceGroups.append({"name": "joint-r-eye-target", "first": 16711, "last": 16717})
        faceGroups.append({"name": "joint-r-finger-1-1", "first": 16657, "last": 16663})
        faceGroups.append({"name": "joint-r-finger-1-2", "first": 16651, "last": 16657})
        faceGroups.append({"name": "joint-r-finger-1-3", "first": 16645, "last": 16651})
        faceGroups.append({"name": "joint-r-finger-1-4", "first": 16639, "last": 16645})
        faceGroups.append({"name": "joint-r-finger-2-1", "first": 16633, "last": 16639})
        faceGroups.append({"name": "joint-r-finger-2-2", "first": 16591, "last": 16597})
        faceGroups.append({"name": "joint-r-finger-2-3", "first": 16585, "last": 16591})
        faceGroups.append({"name": "joint-r-finger-2-4", "first": 16543, "last": 16549})
        faceGroups.append({"name": "joint-r-finger-3-1", "first": 16627, "last": 16633})
        faceGroups.append({"name": "joint-r-finger-3-2", "first": 16597, "last": 16603})
        faceGroups.append({"name": "joint-r-finger-3-3", "first": 16579, "last": 16585})
        faceGroups.append({"name": "joint-r-finger-3-4", "first": 16549, "last": 16555})
        faceGroups.append({"name": "joint-r-finger-4-1", "first": 16621, "last": 16627})
        faceGroups.append({"name": "joint-r-finger-4-2", "first": 16603, "last": 16609})
        faceGroups.append({"name": "joint-r-finger-4-3", "first": 16573, "last": 16579})
        faceGroups.append({"name": "joint-r-finger-4-4", "first": 16555, "last": 16561})
        faceGroups.append({"name": "joint-r-finger-5-1", "first": 16615, "last": 16621})
        faceGroups.append({"name": "joint-r-finger-5-2", "first": 16609, "last": 16615})
        faceGroups.append({"name": "joint-r-finger-5-3", "first": 16567, "last": 16573})
        faceGroups.append({"name": "joint-r-finger-5-4", "first": 16561, "last": 16567})
        faceGroups.append({"name": "joint-r-foot-1", "first": 16405, "last": 16411})
        faceGroups.append({"name": "joint-r-foot-2", "first": 16399, "last": 16405})
        faceGroups.append({"name": "joint-r-hand-2", "first": 16669, "last": 16675})
        faceGroups.append({"name": "joint-r-hand-3", "first": 16663, "last": 16669})
        faceGroups.append({"name": "joint-r-hand", "first": 16675, "last": 16681})
        faceGroups.append({"name": "joint-r-knee", "first": 16531, "last": 16537})
        faceGroups.append({"name": "joint-r-lowerlid", "first": 16705, "last": 16711})
        faceGroups.append({"name": "joint-r-scapula", "first": 16699, "last": 16705})
        faceGroups.append({"name": "joint-r-shoulder", "first": 16687, "last": 16693})
        faceGroups.append({"name": "joint-r-toe-1-1", "first": 16519, "last": 16525})
        faceGroups.append({"name": "joint-r-toe-1-2", "first": 16513, "last": 16519})
        faceGroups.append({"name": "joint-r-toe-1-3", "first": 16507, "last": 16513})
        faceGroups.append({"name": "joint-r-toe-2-1", "first": 16501, "last": 16507})
        faceGroups.append({"name": "joint-r-toe-2-2", "first": 16459, "last": 16465})
        faceGroups.append({"name": "joint-r-toe-2-3", "first": 16453, "last": 16459})
        faceGroups.append({"name": "joint-r-toe-2-4", "first": 16447, "last": 16453})
        faceGroups.append({"name": "joint-r-toe-3-1", "first": 16495, "last": 16501})
        faceGroups.append({"name": "joint-r-toe-3-2", "first": 16465, "last": 16471})
        faceGroups.append({"name": "joint-r-toe-3-3", "first": 16435, "last": 16441})
        faceGroups.append({"name": "joint-r-toe-3-4", "first": 16441, "last": 16447})
        faceGroups.append({"name": "joint-r-toe-4-1", "first": 16489, "last": 16495})
        faceGroups.append({"name": "joint-r-toe-4-2", "first": 16471, "last": 16477})
        faceGroups.append({"name": "joint-r-toe-4-3", "first": 16423, "last": 16429})
        faceGroups.append({"name": "joint-r-toe-4-4", "first": 16429, "last": 16435})
        faceGroups.append({"name": "joint-r-toe-5-1", "first": 16483, "last": 16489})
        faceGroups.append({"name": "joint-r-toe-5-2", "first": 16477, "last": 16483})
        faceGroups.append({"name": "joint-r-toe-5-3", "first": 16411, "last": 16417})
        faceGroups.append({"name": "joint-r-toe-5-4", "first": 16417, "last": 16423})
        faceGroups.append({"name": "joint-r-upper-leg", "first": 16537, "last": 16543})
        faceGroups.append({"name": "joint-r-upperlid", "first": 16717, "last": 16723})
        faceGroups.append({"name": "joint-spine-1", "first": 16063, "last": 16069})
        faceGroups.append({"name": "joint-spine-2", "first": 16057, "last": 16063})
        faceGroups.append({"name": "joint-spine-3", "first": 16051, "last": 16057})
        faceGroups.append({"name": "joint-spine-4", "first": 16045, "last": 16051})
        faceGroups.append({"name": "joint-tongue-1", "first": 16759, "last": 16765})
        faceGroups.append({"name": "joint-tongue-2", "first": 16753, "last": 16759})
        faceGroups.append({"name": "joint-tongue-3", "first": 16741, "last": 16747})
        faceGroups.append({"name": "joint-tongue-4", "first": 16735, "last": 16741})
        return faceGroups

