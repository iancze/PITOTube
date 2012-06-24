#!/usr/bin/env python2
# Executes the pipeline, which subset commands are (for now) written directly in Python. May be later wrapped with a GUI.

import target

flat_field = "flat.fits"
bias = "bias.fits"
science = "science.fits"

my_target = target.Target(name="GRB1",RA="",DEC="")
my_target.add_observation(target.Observation(band="band"))

