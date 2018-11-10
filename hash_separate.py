import time
import threading
from collections import defaultdict
import os
import queue
from concurrent.futures import ThreadPoolExecutor  #导出线程池
from multiprocessing.pool import ThreadPool        #导出线程池
q = queue.Queue()

# 线程池
def thread_pool():
    while True:
        t, args = q.get()
        t(*args)
        q.task_done()

# 专门写文件
def task(f, lines, lock):
    # with lock:
    f.writelines(lines)

def start_sep(idn, npart):
    start = time.time()	
    if not os.path.exists('data'):
        os.mkdir('data')

    # 自建线程池
    for i in range(64):
        t = threading.Thread(target=thread_pool)
        t.daemon = True
        t.start()

    # 保存所有子文件指针
    fd = {}
    for i in range(npart):
        fd[i] = open('workingdata/sep_' + str(i) + '.txt', 'w')

    lock = threading.Lock()
    with open('text/' + str(idn) + '.txt', 'r') as f:
        fv = defaultdict(list)
        for line in f:
            line = line[2:16] +'\n'
            k = int(line) % npart # "1.16736489906023e+08 7 5"   
            fv[k].append(line)
            if len(fv[k]) >= int(npart/100)*100:      # 如果一个键值长度超过1000，则写入文件
                q.put((task, (fd[k], fv[k].copy(), lock)))
                fv[k].clear()
    q.join()
    # 所有队列完成后，还有部分字符长度少于1000的没有写入
    for k, f in fd.items():
        f.writelines(fv[k])
    for i in range(npart):
        fd[i].close()
    print(time.time() - start)



if __name__ == '__main__':
	start_sep(1010010112, 512)