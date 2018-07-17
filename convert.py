#!/usr/bin/python3 -B
# -*- coding: utf-8 -*-
import os, sys, time, random
from multiprocessing import Pool
from time import sleep

global n_threads ; n_threads = 4
global l_filter ; l_filter = ""

def checkList(w_list):
    c = 0
    while c < len(w_list):
        if w_list[c].find(l_filter) == -1:
            del w_list[c]
        else:
            c += 1
    w_list.sort()
    return w_list

def doJob(item):
    start_time = time.time()
    # abspathToItem = os.path.abspath(sys.argv[1])
    # print('ffmpeg -loglevel panic -n -i "%s/%s" -vn -acodec libmp3lame -threads 3 -ac 2 -qscale:a 4 -ar 48000 "%s/mp3-out/%s.mp3"' % (abspathToItem,item,abspathToItem,item))
    # os.system('ffmpeg -loglevel panic -n -i "%s/%s" -vn -acodec libmp3lame -threads 3 -ac 2 -qscale:a 4 -ar 48000 "%s/mp3-out/%s.mp3"' % (abspathToItem,item,abspathToItem,item))
    sleep(random.randint(1,3))
    print("finished", item, "[Took us", time.time() - start_time, "seconds]")

def paralellizeJobs(w_list):
    print("List to be processed:")
    print(w_list)
    with Pool(n_threads) as p:
        p.map(doJob, w_list)
    return

if __name__ == "__main__":
    if os.path.isdir(sys.argv[1]) == True:
        paralellizeJobs(checkList(os.listdir(os.path.abspath(sys.argv[1]))))
    else:
        print("E: Path must be directory")
