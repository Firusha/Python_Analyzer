import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import time
import math
from sys import stdout

def distance_from_start(dictionary, savedir_1, datatype):
    print("Beginning to plot distance from Start")
    print("%d plots will be created" % len(dictionary))
    savedir = savedir_1 + "/distance_from_start"
    count = len(dictionary)
    curr_count = 0
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    
    for key in dictionary:
        x = []
        y = []
        t = [0]
        velocity = [0]
        for i in range(1, len(dictionary[key])):
            x1 = dictionary[key][0][0]
            y1 = dictionary[key][0][1]
            x2 = dictionary[key][i][0]
            y2 = dictionary[key][i][1]

            v = ((x1-x2)**2 + (y1-y2)**2)**0.5

            velocity.append(v)
            t.append(dictionary[key][i][3])
        plt.figure(figsize=(10,5))
        plt.plot(t, velocity, linewidth=2.0, zorder=1)
        plt.axis([0, 144, 0, 0.1])
        plt.title("Distance from Start after each frame of Track %s" % key)
        plt.savefig("%s/distance_from_start_%s.%s" % (savedir, key,datatype))
        plt.close()

        curr_count += 1
        if(curr_count%round(count/10)==0):
            percentage=round(curr_count/count*100,0)
            print(percentage, "% of Distance from Start plotting complete")
    print("Distance from Start Plotting complete..")
