#! /usr/bin/env python
"""
Estimate phase synchronization periods between ENSO and AIMRI
=============================================================

"""
# Created: Wed Oct 11, 2017  03:18PM
# Last modified: Fri Nov 17, 2017  08:40AM
# Copyright: Bedartha Goswami <goswami@pik-potsdam.de>

import numpy as np
import datetime as dt
from scipy import signal
from scipy.stats import percentileofscore, norm
import csv
import netCDF4

def load_data():
		"""Returns Nino3 and ISMR time series after laoding data from CSV files.
		"""
		fsikkim = "sikkim_jastemp_1870_2008.txt"
		dsikkimjastemp = np.genfromtxt(fsikkim, delimiter=",", dtype=float).flatten()
		return dsikkimjastemp
