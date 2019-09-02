#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division # no more "zero" integer division bugs!:P
#import argparse,os, time, glob, sys, datetime # os: operating system | time: execution time | glob: globbing file...loading multiple files as *.pippa | sys: system...boh | datetime: daquasi-globaly and so...
import numpy as np # array


# radiants, degrees conversions etc.
pi      = 4.0*np.arctan(1.0)
dpi     = 2.0*pi
deg2rad = pi/180.0
rad2deg = 180.0/pi

# various
eps32bit  = np.finfo(np.float32(1.0)).eps
TOL_sp    = eps32bit
eps64bit  = np.finfo(np.float64(1.0)).eps
TOL_dp    = eps64bit
TOLERANCE = 1.0e-9
TOL       = TOLERANCE
d2s       = 86400.0 # seconds in a day  =  24h  =  86400 s
d2m       = 1440.0  # min in a day  =  1440. min

# Astronomical Constants USNO 2018

# body constants
GMsun_tcb = 1.32712442099e20 # Solar mass parameter: m^3/s^2 (TCB)          | +/- 1D10    |
GMsun_tdb = 1.32712440041e20 # Solar mass parameter: m^3/s^2 (TDB)          | +/- 1D10    |

# masses conversions
Msmer = 6.0236e6 # Msun to Mmer
Mmers = 1.0/Msmer # Mmer to Msun
Msven = 4.08523719e5 # Msun to Mven
Mvens = 1.0/Msven   #  Mven to Msun
Msear = 332946.0487 # Msun to Mear
Mears = 1.0/Msear  #  Mear to Msun
Msmar = 3.09870359e6 # Msun to Mmar
Mmars = 1.0/Msmar   #  Mmar to Msun
Msjup = 1.047348644e3 # Msun to Mjup
Mjups = 1.0/Msjup    #  Mjup to Msun
Mssat = 3.4979018e3 # Msun to Msat
Msats = 1.0/Mssat  #  Msat to Msun
Msura = 2.290298e4 # Msun to Mura
Muras = 1.0/Msura #  Mura to Msun
Msnep = 1.941226e4 # Msun to Mnep
Mneps = 1.0/Msnep #  Mnep to Msun

# masses of Solar System objects
Msun = 1.9884e30 # Sun mass in kg
Mmer = Msun*Mmers #  Mercury mass in kg
Mven = Msun*Mvens #  Venus mass in kg
Mear = 5.9722e24 # Earth mass in kg
Mmar = Msun*Mmars #  Mars mass in kg
Mjup = Msun*Mjups #  Jupiter mass in kg
Msat = Msun*Msats #  Saturn mass in kg
Mura = Msun*Muras #  Uranus mass in kg
Mnep = Msun*Mneps #  Neptune mass in kg

# radii of Solar System objects
Rsun = 696000.0 #  Sun radius in km
Rmer = 2439.7  #  Mercury radius in km
Rven = 6051.8  #  Venus radius in km
Rear = 6378.1366 # Earth radius in km
Rmar = 3396.19 #  Mars radius in km
Rjup = 71492.0  #  Jupiter radius in km
Rsat = 60268.0  #  Saturn radius in km
Rura = 25559.0  #  Uranus radius in km
Rnep = 24764.0  #  Neptune radius in km
Rplu = 1195.0  #  Pluto radius in km
#
Rsjup = Rsun/Rjup #  Rsun to Rjup
Rjups = Rjup/Rsun #  Rjup to Rsun
#
Rejup = Rear/Rjup # Rearth to Rjupiter
Rjear = Rjup/Rear # Rjupiter to Rearth
#
Rsear = Rsun/Rear #  Rsun to Rjup
Rears = Rear/Rsun #  Rear to Rsun

# Density of the Sun in kg/m^3
rho_sun_kgmc = Msun/(4.0*np.pi*np.power(Rsun*1000.0,3)/3.0)

# astronomical constants
AU = 149597870700.0 #Astronomical Unit in meters
kappa = 0.01720209895 # Gaussian gravitational constant
Giau = kappa*kappa # G [AU^3/Msun/d^2]
Gsi = 6.67428e-11 #Gravitational Constants in SI system [m^3/kg/s^2]
Gaumjd = Gsi*d2s*d2s*Mjup/(AU**3) # G in [AU,Mjup,day]
speed = 299792458.0 # speed of light (c) in [m/s]
speedaud = speed*d2s/AU # speed of light in [AU/d]
pc2AU = 206264.806 # parsec to au

# others
RsunAU = (Rsun*1.e3)/AU #Sun radius in AU
RjupAU = (Rjup*1.e3)/AU #Jupiter radius in AU

MJD = 2400000.5 # MJD ref time to convert to JD

sigma_sb = 5.670367e-8 # Stefan-Boltzmann constant in W⋅m^−2⋅K^−4

Teff_sun = 5772. # Effective Temperature of the Sun in K

# from http://archive.stsci.edu/kepler/manuals/Data_Characteristics.pdf
# section 1.1 Dates, Cadence Numbers, and Units
# global variables
Tkplr  = 2454833.       # Reference kepler time (days)
Tkend  = 2456424.       # end Kepler data mission (Q17)
texp_llc = 1766. /86400.    # llc exposure time in min to day
texp_slc = 58.85 / 86400.    # slc exposure time in min to day
