import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from tletools import TLE
from astropy import units as u
from poliastro.bodies import Earth, Moon
from poliastro.earth import Orbit

#rEarth = 6371 #km
rEarth = 1


def convert_gps(gps):
    x = rEarth * math.cos(gps[1]) * math.cos(gps[0])
    y = rEarth * math.sin(gps[1]) #Switched y and z because of preference
    z = rEarth * math.cos(gps[1]) * math.sin(gps[0])
    return x,y,z

def createOrbit(tle):
    return tle.to_orbit()

def parse_tle(file):
    data = open(file, "r")
    data = data.read().strip().splitlines()
    data = TLE.from_lines(*data)
    return data



def plot_coordinate(gps_array):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.axes.set_xlim3d(left=-2, right=2) 
    ax.axes.set_ylim3d(bottom=-2, top=2) 
    ax.axes.set_zlim3d(bottom=-2, top=2) 

    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')

    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = rEarth * np.cos(u)*np.sin(v)
    y = rEarth * np.sin(u)*np.sin(v)
    z = rEarth * np.cos(v)

    ax.plot_surface(x, y, z,  rstride=1, cstride=1, color='b', alpha=1, linewidth=0)
    ax.scatter(gps_array[0], gps_array[1], gps_array[2], color='r', alpha=1, s=10)

    plt.show()


def inclination_angle(location, orbit, time):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.axes.set_xlim3d(left=-2, right=2) 
    ax.axes.set_ylim3d(bottom=-2, top=2) 
    ax.axes.set_zlim3d(bottom=-2, top=2) 

    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')

    

    x0 = np.array([0,])
    y0 = np.array([0,])
    z0 = np.array([0,])

    u,v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x1 = rEarth * np.cos(u)*np.sin(v)
    y1 = rEarth * np.sin(u)*np.sin(v)
    z1 = rEarth * np.cos(v)

    
    ax.plot()
    ax.plot_surface(x1, y1, z1,  rstride=1, cstride=1, color='b', alpha=1, linewidth=0)

    


    plt.show()
