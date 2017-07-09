#!/usr/bin/env python3

#!/usr/bin/env python3

#################################################################################
#										#
# Copyright (c) 2016 Allen Majewski (altoidnerd)				#
# Permission is hereby granted, free of charge, to any person obtaining a 	#
# copy of this software and associated documentation files (the "Software"),	#
# to deal in the Software without restriction, including without limitation	#
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 	#
# and/or sell copies of the Software, and to permit persons to whom the		#	
# Software is furnished to do so, subject to the following conditions:		#
#										#
# The above copyright notice and this permission notice shall be included 	#
# in all copies or substantial portions of the Software.			#
#										#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 	#
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 	#
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 	#
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 	#
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,	#
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE	#
# THE SOFTWARE.									#                                
#										#
#################################################################################

#   python-pwscf was designed for python3; 
#   run on > 2.7 at your own risk.						

import sys
import matplotlib.pyplot as plt
import numpy as np



def filtrByComp(term, arr):
  return [ line for line in arr if term in line ]

def filtrByLambda(term, arr):
  return list(filter(lambda x: term in x, arr))

filtr=filtrByComp


class Efg(object):
  """
  Class for parsing gipaw.x output files
  for 'efg' calculation
  """
  # special paradichlorobenzene stuff

  #           [ carbons             ,      hydrogens, chlorines ]
  molecule1 = [2,  3,  5, 17, 16, 14,  4,  6, 15, 13,  1, 18]
  molecule2 = [23, 8, 10, 11, 20, 22,  7,  9, 19, 21, 24, 12]
  
  def __init__(self, efgfile):
    self.efgfile = efgfile
    self.efgfile_array = open(efgfile, 'r').readlines()
    self.file_array = self.efgfile_array
    
    # ascertain nat
    nat = len([ line for line in self.file_array if 'Q=' in line ])
    self.nat = nat

    self.WALL_TIME = float([ line.split()[4] for line in filtr('WALL',self.file_array) ][-1].replace('s',''))
    self.CPU_TIME  = float([ line.split()[2] for line in filtr('WALL',self.file_array) ][-1].replace('s',''))


  def __repr__(self):
    return "< efg object; efgfile: {}\tlength: {} lines >".format(self.efgfile, len(self.efgfile_array))

  def __str__(self):
    s = ""
    for line in self.file_array:
      s += line
    return s

  def prnt(self):
    for line in self.file_array:
      sys.stdout.write(line)

    
