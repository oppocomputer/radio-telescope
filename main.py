from calculations import *
import time
import numpy as np


print("Radio telescope started!")
unixtime = time.time_ns() #Nano seconds after 00:00:00 1 January 1970



#plt.show()


#Configuration
tle_file="iss.tle"
gps = np.array([51.03594,5.72767])
gps_array = np.array(convert_gps(gps))
matplotlib = True


#Calculations
#tle = parse_tle(tle_file)
#print("Succesfully loaded " + tle_file)
#orbit = createOrbit(tle)
#print(orbit)
plot_coordinate(gps_array)




#calculations.convert_gps(gps_shd)