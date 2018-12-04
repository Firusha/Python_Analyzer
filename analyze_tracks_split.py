import os
import time
import timeit
import logging
import multiprocessing

from itertools import islice

from tkinter import Tk
from tkinter.filedialog import askopenfilename

from MODULES.tracking import *
from MODULES.track_centered import *
from MODULES.track_singular import *
from MODULES.track_slices import *
from MODULES.track_all import *
from MODULES.plot_velocity import *
from MODULES.plot_distance_from_start import *
from MODULES.persistence import *


#current_time = time.strftime("%Y_%m_%d_%H_%M", time.localtime())
####################
if not os.path.exists("LOGS"):
    os.makedirs("LOGS")

logger = logging.getLogger("analyze Tracks")
logger.setLevel(logging.DEBUG)
####################
current_time = time.strftime("%Y_%m_%d_%H_%M", time.localtime())

logfile = logging.FileHandler("LOGS/%s.log" % current_time)
logfile.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
logfile.setFormatter(formatter)
logger.addHandler(logfile)
logger.addHandler(console)



def time_stuff(other_function,arguments):
    """Times the runtime of a function and prints the runtime"""
    local_start = timeit.default_timer()
    other_function(*arguments)
    local_end = timeit.default_timer()
    m, s = divmod(local_end-local_start, 60)
    h, m = divmod(m, 60)
    logger.info("Time for execution of %s: %02i:%02i:%02i" %(other_function.__name__,h, m, s))

def split_dict(data, SIZE=10000):
    """Splits a dictionary into chunks of a predetermined SIZE"""
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k:data[k] for k in islice(it, SIZE)}

    
if __name__ == '__main__':

    if(input("loop over all files (y/n)? ") == "y"):
        for file in os.listdir("G:\\"):
            if ("Spots in tracks statistics" in file) and file.endswith(".csv"):
                filename = "G:/"+file
                
                logger.info("opening %s" %filename)
    ####################

                main_dir = os.path.dirname(filename)
                base_name = os.path.basename(filename).replace(".csv", "").replace(" ","_")

                savedir = main_dir + "/" + current_time + "_" + base_name
                track_dict = tracking(filename)
                datatype = "pdf"  
                start = timeit.default_timer()

                processlist = []
                processlist.append(multiprocessing.Process(target=time_stuff, args=(plot_slices, (track_dict, savedir, datatype),)))
                processlist.append(multiprocessing.Process(target=time_stuff, args=(plot_all_tracks, (track_dict, savedir, datatype),)))
                processlist.append(multiprocessing.Process(target=time_stuff, args=(single_plot_velocity, (track_dict, savedir, datatype),)))
                processlist.append(multiprocessing.Process(target=time_stuff, args=(plot_tracks_centered, (track_dict, savedir, "png"),)))
                processlist.append(multiprocessing.Process(target=time_stuff, args=(plot_all_tracks_centered, (track_dict, savedir, datatype),)))
                processlist.append(multiprocessing.Process(target=time_stuff, args=(plot_tracks_singular, (track_dict, savedir, "png"),)))
                processlist.append(multiprocessing.Process(target=time_stuff, args=(plot_velocity, (track_dict, savedir, "png"),)))
                processlist.append(multiprocessing.Process(target=time_stuff, args=(distance_from_start, (track_dict, savedir, datatype),)))
                processlist.append(multiprocessing.Process(target=time_stuff, args=(calc_persistence, (track_dict, savedir),)))
                processlist.append(multiprocessing.Process(target=time_stuff, args=(delta_persistance, (track_dict, savedir,"png"),)))
                processlist.append(multiprocessing.Process(target=time_stuff, args=(plot_total_velocity, (track_dict, savedir, "pdf"),)))
                processlist.append(multiprocessing.Process(target=time_stuff, args=(plot_total_velocity_single_tracks, (track_dict, savedir, "pdf"),)))
				## just added a comment
                
                print(len(processlist))

                for item in processlist:
                    item.start()
                    
                for item in processlist:
                    item.join()
                
                end = timeit.default_timer()
                m, s = divmod(end-start, 60)
                h, m = divmod(m, 60)
                logger.info("Time for whole execution: %02i:%02i:%02i" %(h, m, s))
                
    else:
        Tk().withdraw()
        filename = askopenfilename()

        logger.info("opening %s" %filename)
        ####################

        main_dir = os.path.dirname(filename)
        base_name = os.path.basename(filename).replace(".csv", "").replace(" ","_")

        savedir = main_dir + "/" + current_time + "_" + base_name
        track_dict = tracking(filename)
        datatype = "pdf"  
        start = timeit.default_timer()

        processlist = []
##        processlist.append(multiprocessing.Process(target=time_stuff, args=(plot_slices, (track_dict, savedir, datatype),)))
        processlist.append(multiprocessing.Process(target=time_stuff, args=(plot_all_tracks, (track_dict, savedir, datatype),)))
        processlist.append(multiprocessing.Process(target=time_stuff, args=(single_plot_velocity, (track_dict, savedir, datatype),)))
##        processlist.append(multiprocessing.Process(target=time_stuff, args=(plot_tracks_centered, (track_dict, savedir, "png"),)))
        processlist.append(multiprocessing.Process(target=time_stuff, args=(plot_all_tracks_centered, (track_dict, savedir, datatype),)))
##        processlist.append(multiprocessing.Process(target=time_stuff, args=(plot_tracks_singular, (track_dict, savedir, "png"),)))
        processlist.append(multiprocessing.Process(target=time_stuff, args=(plot_velocity, (track_dict, savedir, "png"),)))
##        processlist.append(multiprocessing.Process(target=time_stuff, args=(distance_from_start, (track_dict, savedir, datatype),)))
        processlist.append(multiprocessing.Process(target=time_stuff, args=(calc_persistence, (track_dict, savedir),)))
        processlist.append(multiprocessing.Process(target=time_stuff, args=(delta_persistance, (track_dict, savedir,"png"),)))
        processlist.append(multiprocessing.Process(target=time_stuff, args=(plot_total_velocity, (track_dict, savedir, "pdf"),)))
        processlist.append(multiprocessing.Process(target=time_stuff, args=(plot_total_velocity_single_tracks, (track_dict, savedir, "pdf"),)))
        
        print(len(processlist))

        for item in processlist:
            item.start()
            
        for item in processlist:
            item.join()
        
        end = timeit.default_timer()
        m, s = divmod(end-start, 60)
        h, m = divmod(m, 60)
        logger.info("Time for whole execution: %02i:%02i:%02i" %(h, m, s))

