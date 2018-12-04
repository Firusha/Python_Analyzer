import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import time
import math
from sys import stdout

def plot_tracks_singular(dictionary, savedir_1,datatype):
    print("Beginning to plot all Tracks at their Position")
    print("%d plots will be created" % len(dictionary))
    savedir = savedir_1 + "/single_tracks"

    count = len(dictionary)
    curr_count=0
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    for key in dictionary:
        startX = dictionary[key][0][0]
        startY = dictionary[key][0][1]
        x = []
        absx = []
        y = []
        absy = []
        t = []
        for i in range(len(dictionary[key])):
            x.append(dictionary[key][i][0])
            y.append(dictionary[key][i][1])
            t.append(dictionary[key][i][3])

        # print("plotting track %s" % key)
        color = [str(i/255) for i in t]
        plt.figure(figsize=(6,12))
        plt.axis([0, 0.1, 0, 0.15])
        plt.plot(x,y, color="gray", linewidth=2.0, zorder=1)
        plt.scatter(x, y, s=15, c=color, zorder=2)
        plt.title("scatterplot of track %s" % key)
        plt.savefig("%s/abs_position_track_%s.%s" % (savedir, key, datatype))
        plt.close()

        curr_count += 1
        if(curr_count%round(count/10)==0):
            percentage=round(curr_count/count*100,0)
            print(percentage, "% of absolute Position plotting complete")
    print("Absolut Plotting complete..")
