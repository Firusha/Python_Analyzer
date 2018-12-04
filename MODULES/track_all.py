import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import time
import math
from sys import stdout
import logging


def plot_all_tracks(dictionary, savedir_1,datatype):
    print("Beginning to plot all Tracks")
    test=[]
    for key in dictionary:
	    test.append(key)
    print("%d plots will be created" % len(test))
    savedir=savedir_1
    
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    plt.figure(figsize=(10,20))
    
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
        
        plt.plot(x,y, linewidth=0.1, zorder=1)
        #plt.scatter(x, y, s=15, c=color, zorder=2)
    
    plt.title("all tracks")
    plt.savefig("%s/all_tracks.%s" % (savedir, datatype))
    plt.close()  
    print("All Track Plotting complete..")
