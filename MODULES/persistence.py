import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import time
import math
from sys import stdout

def calc_persistence(dictionary, savedir_1):
    print("Beginning to calculate persistence of all Tracks")
    savedir = savedir_1 + "/persistence"

    count = len(dictionary)
    curr_count = 0
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    persistances = [["key", "persistence", "corrected persistence", "whole traversed distance", "displacement"]]
    persists_corrected =[]
    for key in dictionary:
        sum_of_dists = 0
        dist_from_start = 0
        for i in range(1, len(dictionary[key])):
            x1 = dictionary[key][i-1][0]
            y1 = dictionary[key][i-1][1]
            x2 = dictionary[key][i][0]
            y2 = dictionary[key][i][1]

            sum_of_dists += ((x1-x2)**2 + (y1-y2)**2)**0.5

        x_start = dictionary[key][0][0]
        y_start = dictionary[key][0][1]
        x_end = dictionary[key][len(dictionary[key])-1][0]
        y_end = dictionary[key][len(dictionary[key])-1][1]

        dist_from_start = ((x_start-x_end)**2 + (y_start-y_end)**2)**0.5
        persistances.append([key, dist_from_start/sum_of_dists,\
                             dist_from_start/sum_of_dists*(dictionary[key][len(dictionary[key])-1][3])**0.5,\
                             dist_from_start, sum_of_dists])
        persists_corrected.append(dist_from_start/sum_of_dists*(dictionary[key][len(dictionary[key])-1][3])**0.5)

    with open(savedir_1 +"/persistence.csv", "w") as csv:
        for item in persistances:
            csv.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(item[0],item[1],item[2],item[3], item[4]))
            #print(("{0:10},{1:10},{2:10},{3:10}".format(item[0],item[1],item[2],item[3])))

    for i in range(1, 21):
        plt.hist(persists_corrected, 5*i)
        plt.xlabel("corrected Persistence")
        plt.ylabel("count")
        plt.title("Histogram of corrected Persistence with %s bins\n%s" % ((5*i), savedir_1[savedir_1.find("cs_")+3:savedir_1.find("/",savedir_1.find("cs_")+3)+1]))
        plt.savefig("%s/corrected_persistence_Histogram_%i.%s" % (savedir,(5*i),"pdf"))
        plt.close()
            


def delta_persistance(dictionary, savedir_1, datatype):
    print("Beginning to calculate persistence of all Tracks")
    savedir = savedir_1 + "/persistence"

    count = len(dictionary)
    curr_count = 0
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    persistances = [["key", "persistence", "whole traversed distance", "distance from start"]]

    max_t = 0
    for key in dictionary:
        for i in range(len(dictionary[key])):
            if dictionary[key][i][3] > max_t:
                max_t = dictionary[key][i][3]
    
    for key in dictionary:
        sum_of_dists = 0
        dist_from_start = 0
        t = [0]
        current_persistence = [1]
        corrected_persistence = [1]
        for i in range(1, len(dictionary[key])):
            x1 = dictionary[key][i-1][0]
            y1 = dictionary[key][i-1][1]
            x2 = dictionary[key][i][0]
            y2 = dictionary[key][i][1]
            x_start = dictionary[key][0][0]
            y_start = dictionary[key][0][1]

            sum_of_dists += ((x1-x2)**2 + (y1-y2)**2)**0.5
            dist_from_start = ((x_start-x2)**2 + (y_start-y2)**2)**0.5

            if(sum_of_dists == 0.0 and dist_from_start == 0.0):
                print(key, "step", i, "didn't move - persistence is still 1")
                current_persistence.append(1.0)
                corrected_persistence.append(1.0)
                t.append(dictionary[key][i-1][3])
            else:
                current_persistence.append(dist_from_start/sum_of_dists)
                corrected_persistence.append((dist_from_start/sum_of_dists)*(i**0.5))
                t.append(dictionary[key][i-1][3])

            
            

        x_start = dictionary[key][0][0]
        y_start = dictionary[key][0][1]
        x_end = dictionary[key][len(dictionary[key])-1][0]
        y_end = dictionary[key][len(dictionary[key])-1][1]

        plt.figure(figsize=(10,5))
        plt.plot(t, current_persistence, linewidth=2.0, zorder=1)
        #plt.plot(t, corrected_persistence, linewidth=2.0, zorder=1)
        plt.axis([0, max_t, 0, 1])
        plt.title("persistance by time of track %s" % key)
        plt.savefig("%s/delta_persistence_%s.%s" % (savedir, key,datatype))
        plt.close()

