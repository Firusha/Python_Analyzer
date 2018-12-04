import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import time
import math
from sys import stdout

def plot_velocity(dictionary, savedir_1, datatype):
    print("Beginning to plot velocities of all Tracks")
    print("%d plots will be created" % len(dictionary))
    savedir = savedir_1 + "/velocity_plots"

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
            x1 = dictionary[key][i-1][0]
            y1 = dictionary[key][i-1][1]
            x2 = dictionary[key][i][0]
            y2 = dictionary[key][i][1]

            v = ((x1-x2)**2 + (y1-y2)**2)**0.5

            velocity.append(v)
            t.append(dictionary[key][i][3])
        plt.figure(figsize=(10,5))
        plt.plot(t, velocity, linewidth=2.0, zorder=1)
        plt.axis([0, 144, 0, 0.065])
        plt.title("Velocity per Frame of Track %s" % key)
        plt.savefig("%s/velocity_of_track_%s.%s" % (savedir, key, datatype))
        plt.close()

        curr_count += 1
        if(curr_count%round(count/10)==0):
            percentage=round(curr_count/count*100,0)
            print(percentage, "% of Velocity plotting complete")
    print("Velocity Plotting complete..")


def single_plot_velocity(dictionary, savedir_1, datatype):
    print("Beginning to plot velocities of all Tracks into single file")
    print("%d plots will be created" % len(dictionary))
    savedir = savedir_1# + "/velocity_plots"
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    plt.figure(figsize=(10,5))
    plt.axis([0, 144, 0, 0.065])
    for key in dictionary:
        x = []
        y = []
        t = [0]
        velocity = [0]
        for i in range(1, len(dictionary[key])):
            x1 = dictionary[key][i-1][0]
            y1 = dictionary[key][i-1][1]
            x2 = dictionary[key][i][0]
            y2 = dictionary[key][i][1]

            v = ((x1-x2)**2 + (y1-y2)**2)**0.5

            velocity.append(v)
            t.append(dictionary[key][i][3])
        
        plt.plot(t, velocity, linewidth=2.0, zorder=1)
    
    plt.title("Velocity per Frame of Track %s" % key)
    plt.savefig("%s/all_velocities.%s" % (savedir, datatype))
    plt.close()  
    print("Velocity Plotting complete..")


def plot_total_velocity(dictionary, savedir_1, datatype):
    print("Beginning to plot total velocities of all Tracks")
    print("%d plots will be created" % len(dictionary))
    savedir = savedir_1 + "/velocity_plots"

    count = len(dictionary)
    curr_count = 0
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    with open("%s/velocities.csv" % savedir_1, "w") as csv:
        v = []
        keys = []
        for key in dictionary:
            x = []
            y = []
            t = [0]
            sum_of_dists = 0
            for i in range(1, len(dictionary[key])):
                x1 = dictionary[key][i-1][0]
                y1 = dictionary[key][i-1][1]
                x2 = dictionary[key][i][0]
                y2 = dictionary[key][i][1]

                d = ((x1-x2)**2 + (y1-y2)**2)**0.5
                sum_of_dists += d
                
                t.append(dictionary[key][i][3])

            v.append(sum_of_dists/len(t))
##            v.append(len(t))
            keys.append(key)

            csv.write("%s\t%f\n" % (key, (sum_of_dists/len(t))))

        #print(len(keys), len(v))
        plt.figure(figsize=(10,5))
        plt.scatter(keys, v)
        plt.axis([0,len(keys),0,max(v)*1.1])
        plt.title("Scatterplot of all velocities\n%s" % savedir_1[savedir_1.find("cs_")+3:])
        plt.xlabel("Tracknumber")
##        plt.ylabel("Frames in Track")
        plt.ylabel("cm/frame")
        plt.savefig("%s/total_velocity_of_all_tracks.%s" % (savedir_1, datatype))
        plt.close()


def plot_total_velocity_single_tracks(dictionary, savedir_1, datatype):
    print("Beginning to plot total velocities of all Tracks")
    print("%d plots will be created" % len(dictionary))
    savedir = savedir_1 + "/velocity_plots"

    count = len(dictionary)
    curr_count = 0
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    v = []
    keys = []
    all_dict = {}
    for key in dictionary:
        x = []
        y = []
        t = []
        sum_of_dists = 0
        current_v = []
        for i in range(1, len(dictionary[key])):
            t = dictionary[key][i-1][3]
            if t not in all_dict:
                x1 = dictionary[key][i-1][0]
                y1 = dictionary[key][i-1][1]
                x2 = dictionary[key][i][0]
                y2 = dictionary[key][i][1]

                d = ((x1-x2)**2 + (y1-y2)**2)**0.5
                all_dict[t] = [d]
            else:
                x1 = dictionary[key][i-1][0]
                y1 = dictionary[key][i-1][1]
                x2 = dictionary[key][i][0]
                y2 = dictionary[key][i][1]

                d = ((x1-x2)**2 + (y1-y2)**2)**0.5
                all_dict[t].append(d)

    avg_dict = {}
    sum_dist = 0
    frame = []
    for key in all_dict:
        sum_dist += sum(all_dict[key])/float(len(all_dict[key]))
        frame.append(key)
        v.append(sum_dist/(key+1))

    plt.plot(frame, v)
    plt.axis([0,max(frame),0,max(v)*1.1])
    plt.title("Average Velocity per Frame\n%s" % (savedir_1[savedir_1.find("cs_")+3:]))
    plt.xlabel("Frame")
    plt.ylabel("cm/frame")
    plt.savefig("%s/average_velocity_per_frame.%s" % (savedir_1, datatype))
    plt.close()

    print("Velocity Plotting complete..")
