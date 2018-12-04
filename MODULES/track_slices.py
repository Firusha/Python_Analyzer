import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import time
import math
from sys import stdout

def plot_slices(dictionary, savedir_1, datatype):
    print("Beginning to plot the Time Slices")
    savedir = savedir_1 + "/time_slice_plots"
    if not os.path.exists(savedir):
        os.makedirs(savedir)
    minx = -0.01
    miny = -0.01
    maxx = 0
    maxy = 0
    
    
    for key in dictionary:
        absx = []
        absy = []
        for i in range(len(dictionary[key])):
            absx.append(dictionary[key][i][0])
            absy.append(dictionary[key][i][1])

        if min(absx) < minx:
            minx = min(absx)
        if min(absy) < miny:
            miny = min(absy)
        if max(absx) > maxx:
            maxx = max(absx)
        if max(absy) > maxy:
            maxy = max(absy)

    minx, maxx = math.floor(minx * 100) / 100.0, math.ceil(maxx * 100) / 100.0
    miny, maxy = math.floor(miny * 100) / 100.0, math.ceil(maxy * 100) / 100.0

    # print(minx, maxx, miny, maxy)

    max_t = 0
    for key in dictionary:
        for i in range(len(dictionary[key])):
            # print(dictionary[key][i][3])
            if dictionary[key][i][3] > max_t:
                max_t = dictionary[key][i][3]

    slice_dir = {}
    for i in range(max_t):
        for key in dictionary:
            for j in range(len(dictionary[key])):
                if dictionary[key][j][3] == i:
                    if not i in slice_dir:
                        slice_dir[i] = [[dictionary[key][j][0]], [dictionary[key][j][1]], [key]]
                    else:
                        slice_dir[i][0].append(dictionary[key][j][0])
                        slice_dir[i][1].append(dictionary[key][j][1])
                        slice_dir[i][2].append(key)

    for i in slice_dir:
        plt.figure(figsize=(6,12))
        # print(i, len(slice_dir[i][0]), len(slice_dir[i][1]))
        plt.scatter(slice_dir[i][0], slice_dir[i][1], s=15, c=str(i/255))
        plt.axis([minx, maxx, miny, maxy])
        plt.title("position of the cells at time %i" % i)
        plt.savefig("%s/slice_%i.%s" % (savedir, i,datatype))
        plt.close()
    print("Time slice plotting complete")
