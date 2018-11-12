from collections import Counter
import multiprocessing as mp
import glob, re, os, time
from collections import defaultdict
from queue import Queue

def find_task(filelist): 
    res = [] # store result of this part
    for path in filelist:
        with open(path, 'r') as f:
            count = Counter(f.readlines())
            res.extend([(k,v) for k, v in count.items() if v > 1]) # choice item appears more than once
    return res

def start_find_dup():
    #########################
    total_files = 512
    file_each_process = 64
    file_list = glob.glob("./workingdata2/sep*") # (total_files) file path
    #########################

    start_time = time.time()

    pool = mp.Pool()
    results = []
    
    for i in range(0, total_files, file_each_process): # i is the start of each process
        f_list = file_list[i:i + file_each_process]
        results.append(pool.apply_async(find_task,(f_list,))) # calculate and put in pool
        #
    pool.close()    
    pool.join() # wait finish

    all_results = []
    for res in results:
        part_res = res.get()
        if len(part_res) > 0:
            all_results.extend(part_res)

    end_time = time.time()
    print("\tFinish finding in %f seconds" % (end_time - start_time) )

    print(all_results)
    return all_results

def save_result(dictionary):
    if not os.path.exists('result'):
        os.mkdir('result')


    idn = os.path.basename(glob.glob("./text/*.txt")[0]).strip('.txt')

    with open("./result/"+idn+"_result.txt", 'w') as out:
        for k,v in dictionary.items():
            line = str(k) + "\t" + str(v) + '\n'
            out.write(line)



if __name__ == '__main__':

    start_find_dup()


