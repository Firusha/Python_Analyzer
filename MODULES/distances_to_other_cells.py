import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import time
import math
import logging
from sys import stdout

logger = logging.getLogger("analyze_Tracks.distances_to_other_cells")
logger.setLevel(logging.DEBUG)

def plot_distances_centered(dictionary, savedir_1,datatype):
    print("Beginning to plot Spots around a centered Spot")
    print("%d plots will be created" % len(dictionary))
    savedir = savedir_1 + "/centered_around_spots"
    count = len(dictionary)
    curr_count = 0
    if not os.path.exists(savedir):
        os.makedirs(savedir)
	
    for key in dictionary:
        startX = dictionary[key][0][0]
        startY = dictionary[key][0][1]
        x = []
        y = []
        max_t = dictionary[key][len(dictionary[key])-1][3]
        t = 0
        for key_2 in dictionary:
            if dictionary[key][t][3] == dictionary[key_2][t][3]:
                if (((dictionary[key_2][t][0] - startX)**2+(dictionary[key_2][t][1] - startY)**2)**0.5) <= 0.02:
                    x.append((dictionary[key_2][t][0] - startX)*10000)
                    y.append((dictionary[key_2][t][1] - startY)*10000)
            else:
                pass
        # print("plotting track %s" % key)
##        plt.scatter(x,y, linewidth=2.0, zorder=1)
        plt.axis('equal')
        max_x = max(x)
        max_y = max(y)
        plt.axis([-1.1*max(max_x, max_y),1.1*max(max_x, max_y), -1.1*max(max_x, max_y), 1.1*max(max_x, max_y)]) 
        plt.scatter(x, y, s=9, zorder=2)
        plt.xlabel("µm")
        plt.ylabel("µm")
        curr_count += 1
        if(curr_count%round(count/10)==0):
            percentage=round(curr_count/count*100,0)
            print(percentage, "% of all centered Plotting complete")
        plt.title("plotting all Tracks centered\n%s" % key)
        
##        plt.show()
        plt.savefig("%s/centered_around_%s.%s" % (savedir,key,datatype))
        plt.close()
    print("Centered Plotting (%s) complete.." % datatype)
