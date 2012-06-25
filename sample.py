#!/usr/bin/env python2
# Executes the pipeline, which subset commands are (for now) written directly in Python. May be later wrapped with a GUI.

import pitotube as pt

flat_field = "flat.fits"
bias = "bias.fits"
science = "science.fits"

#Takes RA and DEC in either Sexagesimal format (HH:MM:SS.SSSS) and (DD:MM:SS.SSSS) or Decimal Degrees.
RA = "00:00:00.0"
DEC = "00:00:00.0"

#or alternatively
#
#RA = 120.00
#DEC = 45.0

band = "r"

my_target = pt.Target(name="GRB1",RA=RA, DEC=DEC)

print my_target
#my_target.add_observation(target.Observation(band=band))

