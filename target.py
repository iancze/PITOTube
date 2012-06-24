'''Target Class template. The Target class is designed to hold all of the pertaining metadata (RA, DEC, name) and the corresponding Observation objects for each astronomical target that will be processed by PITOTube. Will hold all the general properties of the object'''

class Target(object):
    '''Target holds all of the information and objects pertaining to an observation of a single target, possibly with multiple filters.'''
    def __init__(self,name):
        self.name = name
        self.RA = ""#RA object
        self.DEC = ""#DEC object
        self.observations = []

    def add_observation(self,observation):
        observation.set_parent(self)
        self.observations.append(observation)


class Observation(Target):
    '''The Observation class contains all of the objects to fully reduce an observation taken with a single filter, such as science image, flat field(s), bias image, and exposure corrections.'''
    def __init__(self,band):
        self.exptime = exptime
        self.band = band
        self.science = Science_Image()
        self.flat = Flatfield()
        self.flat_raw_list = [Flatfield(),Flatfield()]
        self.bias = Bias()
        pass
        #self.super().__init__() or whatever

    def stack_flats(self):
        #use self.flat_raw_list to create a new Flatfield()
        pass

    def do_reduce(self):
        '''This method calls the pipeline to begin reducing the data to a science format.'''
        #Do flats need stacking? If so, stack them
        if len(self.flat_raw_list) > 1:
            self.flat = self.stack_flats()
        #Trim all of the objects, while subtracting overscan

        pass

    def do_astrometry(self):
        pass



class Image(Observation):
    '''The image class is the base class for dealing with all FITS files, including science, flat, and bias images'''
    def __init__(self,exptime):
        pass

class Science_Image(Image):
    def __init__(self):
        self.reduced = False

    def set_reduced(value):
        #TODO: Check to make sure boolean
        self.reduced = value
    

class Flatfield(Image):
    pass

class Bias(Image):
    pass




