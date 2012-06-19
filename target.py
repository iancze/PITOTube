'''Target Class template. The Target class is designed to hold all of the pertaining metadata (RA, DEC, name) and the corresponding Observation objects for each astronomical target that will be processed by PITOTube. Will hold all the general properties of the object'''

class Target(object):
    def __init__(self,name):
        self.name = name
        self.RA = ""#RA object
        self.DEC = ""#DEC object
        self.observations = []

    def add_observation(self,observation):
        observation.set_parent(self)
        self.observations.append(observation)
