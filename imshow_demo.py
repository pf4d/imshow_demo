# ImShowDemo.py
# Evan Cummings
# CSCS 444 - Data Structures
# 9.29.11

#    Copyright (C) <2011>  <cummings.evan@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Purpose:
#   Program for displaying a variey of three dimensional data 
#   highlighting the features of imPlot, ogrid, and the scipy 
#   math module.

# Usage:
#   Type "run ImShowDemo [3d object type] [a] [b] [c]" where 
#   a, b, and c are scalar values to modify the x, y, and z 
#   calculations, respectively.  The imaginary parts of the 
#   equations were eliminated for this test with the ".real" 
#   modifier.

import matplotlib.pyplot as plt
import sys
from scipy import *

class ImShowDemo:
    
    # Constructor method
    def __init__(self, type, a, b, c):
        
        self.type = type
        a = float(a)
        b = float(b)
        c = float(c)
        
        # Creating the grid of coordinates x,y 
        # changing the last digit (.01) to a higher or lower 
        # value results in an increase of decrease in resolution
        # due to more points plotted.
        x, y = ogrid[-1:1:.01, -1:1:.01]
        
        # Equation for a sphere radius 1 centered at the origin.
        if type == 'sphere':
            self.z =  c * sqrt(1 - (x**2 / a**2) - 
                (y**2 / b**2)).real
        
        # Equation for a hyperboloid of one sheet.
        elif type == 'hyperOne':
            self.z = c * sqrt(-1 + (x**2 / a**2) + 
                (y**2 / b**2)).real
        
        # Equation for a hyperboloid of two sheets.
        elif type == 'hyperTwo':
            self.z = c * sqrt(-1 + (x**2 / a**2)- 
                (y**2 / b**2)).real
        
        # Equation for a two-side cone:
        elif type == 'cone':
            self.z = c * sqrt(-(x**2 / a**2) + 
                (y**2 / b**2)).real
        
        # Equation for an elliptic paraboloid:
        elif type == 'ellPara':
            self.z = (x**2 / a**2) + (y**2 / b**2)
        
        # Equation for a hyperbolic paraboloid:
        elif type == 'saddle':
            self.z = (x**2 / a**2) - (y**2 / b**2)
    
    # method for graphing the chosen equation.
    def draw_stuff(self):
        
        z = self.z
        
        # Creating image
        # Extent gives [xMin, xMax, yMin, yMax] values to plot.
        # change the colormap with the cmap= tag.
        plt.imshow(z, cmap=plt.cm.cool, origin='lower', extent=[-2,2,-2,2])
        
        # labels
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('False color image for a %s' %type)
        plt.colorbar()
        
        # Save the figure as a .png file.
        plt.savefig(type)


# Executable section: Put keyword in args.
if __name__ == '__main__':
    
    type = (len(sys.argv) > 1 and sys.argv[1]) or 'sphere'
    a = (len(sys.argv) > 2 and sys.argv[2]) or '1'
    b = (len(sys.argv) > 3 and sys.argv[3]) or '1'
    c = (len(sys.argv) > 4 and sys.argv[4]) or '1'
    
    demo = ImShowDemo(type, a, b, c)
    
    demo.draw_stuff()
    
    plt.show()

