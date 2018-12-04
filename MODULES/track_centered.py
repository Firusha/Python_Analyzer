import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import time
import math
from sys import stdout


def plot_tracks_centered(dictionary, savedir_1,datatype):
    print("Beginning to plot all Tracks centered to (0, 0)")
    print("%d plots will be created" % len(dictionary))
    savedir = savedir_1 + "/centered_tracks"
    count = len(dictionary)
    curr_count = 0
    if not os.path.exists(savedir):
        os.makedirs(savedir)
	
    for key in dictionary:
        startX = dictionary[key][0][0]
        startY = dictionary[key][0][1]
        x = []
        y = []
        t = []
        for i in range(len(dictionary[key])):
            x.append(dictionary[key][i][0] - startX)
            y.append(dictionary[key][i][1] - startY)
            t.append(dictionary[key][i][3])

        # print("plotting track %s" % key)
        color = [str(i/255) for i in t]
        plt.plot(x,y, color="gray", linewidth=2.0, zorder=1)
        plt.scatter(x, y, s=9, c=color, zorder=2)
        plt.title("scatterplot of track %s" % key)
        plt.savefig("%s/centered_track_%s.%s" % (savedir, key,datatype))
        plt.close()
        curr_count += 1
        if(curr_count%round(count/10)==0):
            percentage=round(curr_count/count*100,0)
            print(percentage, "% of centered Plotting complete")
    print("Centered Plotting (%s) complete.." % datatype)


def plot_all_tracks_centered(dictionary, savedir_1,datatype):
    print("Beginning to plot all Tracks centered to (0, 0)")
    print("%d plots will be created" % len(dictionary))
    savedir = savedir_1
    count = len(dictionary)
    curr_count = 0
    if not os.path.exists(savedir):
        os.makedirs(savedir)
	
    for key in dictionary:
        startX = dictionary[key][0][0]
        startY = dictionary[key][0][1]
        x = []
        y = []
        t = []
        for i in range(len(dictionary[key])):
            x.append(dictionary[key][i][0] - startX)
            y.append(dictionary[key][i][1] - startY)
            t.append(dictionary[key][i][3])

        # print("plotting track %s" % key)
        plt.plot(x,y, linewidth=2.0, zorder=1)
        plt.axis('equal')
        #plt.scatter(x, y, s=9, c=color, zorder=2)
        curr_count += 1
        if(curr_count%round(count/10)==0):
            percentage=round(curr_count/count*100,0)
            print(percentage, "% of all centered Plotting complete")
    plt.title("plotting all Tracks centered\n%s" % savedir_1[savedir_1.find("cs_")+3:])
    plt.savefig("%s/%sall_tracks_centered.%s" % (savedir,savedir_1[savedir_1.find("cs_")+3:savedir_1.find("/", savedir_1.find("cs_")+3)+1],datatype))
    plt.close()
    print("Centered Plotting (%s) complete.." % datatype)
