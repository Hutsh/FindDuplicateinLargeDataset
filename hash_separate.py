import time
import threading
from collections import defaultdict
import os
import queue
from concurrent.futures import ThreadPoolExecutor  #导出线程池
from multiprocessing.pool import ThreadPool        #导出线程池
q = queue.Queue()

def thread_pool():
    while True:
        t, args = q.get()
        t(*args)
        q.task_done()

def write_file_task(f, lines, lock): # write file with lock
    f.writelines(lines)

def line_to_int(line): 
    # define a function to get hashable part of a line
    # return the unique int part 
    # "1.16736489906023e+08"  

    # MUST RETURN AN INT 
    # return int(line[2:16])
    return int(line)

def start_sep(npart):
    ########################
    output_file_path = r'workingdata2' # folder where store seprated texts
    origion_file = r'workingdata2/number.txt' # file that need to find duplicates
    ########################
    start_time = time.time()    

    if not os.path.exists('data'):
        os.mkdir('data')

    for i in range(64): # cread threads
        t = threading.Thread(target=thread_pool)
        t.daemon = True
        t.start()

    fd = {} # store output file pointers
    for i in range(npart):
        fd[i] = open(output_file_path + '/sep_' + str(i) + '.txt', 'w')

    lock = threading.Lock()
    with open(origion_file, 'r') as f:
        fv = defaultdict(list) # dictionary of lists
        for line in f:
            k = line_to_int(line) % npart # hash
            fv[k].append(line)
            if len(fv[k]) >= 1000:      # write when more than 1000 lines
                q.put((write_file_task, (fd[k], fv[k].copy(), lock)))
                fv[k].clear()
    q.join()
    
    for k, f in fd.items(): # write the rest of lines
        f.writelines(fv[k])

    for i in range(npart): # close pointers
        fd[i].close()

    end_time = time.time()  

    print("\tFinish separate in %f seconds" % (end_time - start_time) )



if __name__ == '__main__':
    start_sep(512)
    #print('start')