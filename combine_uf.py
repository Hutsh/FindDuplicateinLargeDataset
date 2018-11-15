from astropy.io import fits
import os
import numpy as np
import re,time
import collections
from config import *

basepath = config_basepath
textpath = config_textpath

def save_id_list():
    idlist = []
    with open('uf_pkg_list.txt', 'r') as pathlist:
        for path in pathlist:
            path = path.strip()
            id = re.search(r'ni\d\d\d\d\d\d\d\d\d\d', path)[0]
            id = id[2:]
            idlist.append(id)

    idlist = list(set(idlist))
    idlist.sort()
    with open('idlist.txt', 'w') as out:
        for i in idlist:
            out.write(str(i) + '\n')

def save_time_in_txt(fitsFilePath):
    filename = os.path.basename(fitsFilePath)
    hdul = fits.open(fitsFilePath)
    time = hdul[1].data['TIME']
    rawx = hdul[1].data['RAWX']
    rawy = hdul[1].data['RAWY']

    cated = np.column_stack((time.astype(np.object), rawx, rawy))

    del hdul
    del time
    del rawx
    del rawy

    # np.savetxt("text/" + filename + ".txt", cated)
    np.savetxt("text/" + filename + ".txt", cated, fmt='%.6f %d%d') #分辨率40ns 但是数据只到小数点后6位（116736489.906023）

def one_id_find_same_time(id): ##main
    path0 = basepath + id + config_filenamePart0 + id + config_filenamePart1_0
    path1 = basepath + id + config_filenamePart0 + id + config_filenamePart1_1
    path2 = basepath + id + config_filenamePart0 + id + config_filenamePart1_2
    path3 = basepath + id + config_filenamePart0 + id + config_filenamePart1_3
    path4 = basepath + id + config_filenamePart0 + id + config_filenamePart1_4
    path5 = basepath + id + config_filenamePart0 + id + config_filenamePart1_5
    path6 = basepath + id + config_filenamePart0 + id + config_filenamePart1_6

    pathlist = [path0, path1, path2, path3, path4, path5, path6]
    for i in pathlist:
        save_time_in_txt(i)

def combine_same_id_text(id):
    command = "cat " + textpath + "*" + id + "*.txt > " + textpath + id + ".txt"
    os.system(command)
    os.system("rm " + textpath + "*" + id + "*.gz.txt")

def save_id_fists_to_one_text(id):

    start = time.time()

    path0 = basepath + id + config_filenamePart0 + id + config_filenamePart1_0
    path1 = basepath + id + config_filenamePart0 + id + config_filenamePart1_1
    path2 = basepath + id + config_filenamePart0 + id + config_filenamePart1_2
    path3 = basepath + id + config_filenamePart0 + id + config_filenamePart1_3
    path4 = basepath + id + config_filenamePart0 + id + config_filenamePart1_4
    path5 = basepath + id + config_filenamePart0 + id + config_filenamePart1_5
    path6 = basepath + id + config_filenamePart0 + id + config_filenamePart1_6

    pathlist = [path0, path1, path2, path3, path4, path5, path6]
    for i in pathlist:
        save_time_in_txt(i)

    combine_same_id_text(id)

    print("\tFinish save fits "+str(id) +" to txt in ", time.time()-start, "s")


def run():
    with open('idlist.txt', 'r') as idlist:
        for id in idlist:
            id = id.strip()
            save_id_fists_to_one_text(id)



if __name__ == '__main__':
    id = '1010010112'
    save_id_fists_to_one_text(id)
    # run()