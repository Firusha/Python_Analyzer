import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import time
import math
import logging
import numpy as np
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

    heatmap_high = []
    for i in range(402):
        heatmap_high.append([])
        for j in range(402):
            heatmap_high[i].append(0)

    heatmap_low = []
    for i in range(102):
        heatmap_low.append([])
        for j in range(102):
            heatmap_low[i].append(0)

    #print(heatmap)
    
    for key in dictionary:
        startX = dictionary[key][0][0]
        startY = dictionary[key][0][1]
        x = []
        y = []
        max_x = []
        max_y = []
        max_t = dictionary[key][len(dictionary[key])-1][3]
        t = 0
        for key_2 in dictionary:
            if dictionary[key][t][3] == dictionary[key_2][t][3]:
##                if (((dictionary[key_2][t][0] - startX)**2+(dictionary[key_2][t][1] - startY)**2)**0.5)*10000 <= 50:
##                    x.append((dictionary[key_2][t][0] - startX)*10000)
##                    y.append((dictionary[key_2][t][1] - startY)*10000)

                if abs((dictionary[key_2][t][0] - startX)*10000) <= 50 and abs((dictionary[key_2][t][1] - startY)*10000) <= 50:
                    xpos = int((dictionary[key_2][t][0] - startX)*10000*4)
                    ypos = int((dictionary[key_2][t][1] - startY)*10000*4)
                    x.append(xpos)
                    y.append(ypos)
##                    print(xpos, ypos)
                    heatmap_high[xpos+201][ypos+201] += 1
                    
                    xpos = int((dictionary[key_2][t][0] - startX)*10000)
                    ypos = int((dictionary[key_2][t][1] - startY)*10000)
                    heatmap_low[xpos+50][ypos+50] += 1
            else:
                pass
        # print("plotting track %s" % key)
##        plt.scatter(x,y, linewidth=2.0, zorder=1)
        plt.axis('equal')        
        plt.scatter(x, y, s=4, zorder=2)
        plt.xlabel("µm")
        plt.ylabel("µm")
        curr_count += 1
        if(curr_count%round(count/10)==0):
            percentage=round(curr_count/count*100,0)
            print(percentage, "% of all centered Plotting complete")
    plt.axis([-210, 210, -210, 210]) 
    plt.title("plotting all Tracks centered\n%s" % key)
        
##        plt.show()
    plt.savefig("%s/centered_around_%s.%s" % (savedir,key,datatype))
    plt.close()
    print("Centered Plotting (%s) complete.." % datatype)

##    with open(savedir+"heatmap.csv","w") as csv:
##        for i in range(len(heatmap)):
##            csv.write(str(heatmap[i]).replace("[","").replace(",","\t").replace("]","")+"\n")
    
        

    #print(heatmap)

    heatmap_high[201][201] = -1
    heatmap_low[50][50] = -1
            
    fig, ax = plt.subplots()
    im = ax.imshow(np.array(heatmap_high), cmap="inferno", origin="lower", extent=[-50,50,-50,50])
    cbar = ax.figure.colorbar(im, ax=ax)
    ax.set_title("heatmap with high resolution")
    cbar.ax.set_ylabel("number of cells at position", rotation=-90, va="bottom")
    fig.tight_layout()
    plt.xlabel("µm")
    plt.ylabel("µm")
    plt.savefig("%s/heatmap_highres.%s" % (savedir,datatype))
    plt.close()
    
    fig, ax = plt.subplots()
    im = ax.imshow(np.array(heatmap_low), cmap="inferno", origin="lower", extent=[-50,50,-50,50])
    cbar = ax.figure.colorbar(im, ax=ax)
    ax.set_title("heatmap with low resolution")
    cbar.ax.set_ylabel("number of cells at position", rotation=-90, va="bottom")
    fig.tight_layout()
    plt.xlabel("µm")
    plt.ylabel("µm")
    plt.savefig("%s/heatmap_lowres.%s" % (savedir,datatype))
    plt.close()
