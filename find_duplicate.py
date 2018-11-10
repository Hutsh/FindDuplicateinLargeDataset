from collections import Counter
import time
import multiprocessing as mp
import glob 
import re
from collections import defaultdict



def get_sep_list():
    return glob.glob("./workingdata/sep*")

def find(start):
    d = []
    sepfileList = get_sep_list()
    for name in sepfileList:
        with open(name, 'r') as f:
            cnt = Counter(f.readlines())
            d.extend([(k,v) for k, v in cnt.items() if v > 1])
            # d.extend(Counter(f.readlines()).most_common(10))
    # print(d)
    return d

def start_find_dup():
    t = time.time()

    # 利用Manager传递变量
    # p = mp.Pool(16)
    # manager = mp.Manager()
    # d = manager.list()
    # for i in range(0, 2 ** 10, 2 ** 4):
    #     p.apply_async(find, args=(i,d))
    # p.close()
    # p.join()

    # 获取进程的返回值
    res = []
    d = []
    p = mp.Pool()
    for i in range(0, 2 ** 10, 2 ** 6):   # 每个进程处理64个文件
        res.append(p.apply_async(find, args=(i,)))
    p.close()
    p.join()
    for r in res:
        d.extend(r.get())
    # print(Counter(dict(d)).most_common(10))
    print(time.time() - t)
    return d

def get_dup_time_list():
    d = start_find_dup()
    uniqueTime = set([t.strip() for t,p in d])
    return uniqueTime

def get_dup_info():
    duplist = get_dup_time_list()
    textfile = glob.glob("./text/*.txt")[0]
    dupinfo = []


    with open(textfile,"r") as f:
        for ln in f:
            cut = ln[2:16]
            if cut in duplist:
                dupinfo.append(ln.strip().split())
    # dupinfo.sort(key=lambda x: x[0])

    # for dupid in
    td = defaultdict(list)
    for time,p in dupinfo:
        td[time].append(p)
        # print("t:",time, " p:",p)





    print(td)




if __name__ == '__main__':
    ut = get_dup_info()
    print(ut)


