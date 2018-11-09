from astropy.io import fits
import os
import numpy as np
import re
import collections


def run():
    #
    # with open('uf_pkg_list.txt') as filelist:
    #     idlist = []
    #     for line in filelist:
    #         c = 0
    #         path = line.strip()
    #         filename = os.path.basename(path)
    #         id = re.search(r'ni\d\d\d\d\d\d\d\d\d\d', filename)[0]
    #         id = id[2:]
    #         idlist.append(id)
    # print(set(idlist))
    #
    # pathlist = []
    # for idnum in idlist:
    #     path0 = r"/run/media/hutsh/Seagate Expansion Drive/NICER/NEW/Download/2017_09_download/FTP/nicer/data/obs/2017_09/" + idnum + r"/xti/event_uf/ni" + idnum + r"_0mpu0_uf.evt.gz"
    #     path1 = r"/run/media/hutsh/Seagate Expansion Drive/NICER/NEW/Download/2017_09_download/FTP/nicer/data/obs/2017_09/" + idnum + r"/xti/event_uf/ni" + idnum + r"_0mpu1_uf.evt.gz"
    #     path2 = r"/run/media/hutsh/Seagate Expansion Drive/NICER/NEW/Download/2017_09_download/FTP/nicer/data/obs/2017_09/" + idnum + r"/xti/event_uf/ni" + idnum + r"_0mpu2_uf.evt.gz"
    #     path3 = r"/run/media/hutsh/Seagate Expansion Drive/NICER/NEW/Download/2017_09_download/FTP/nicer/data/obs/2017_09/" + idnum + r"/xti/event_uf/ni" + idnum + r"_0mpu3_uf.evt.gz"
    #     path4 = r"/run/media/hutsh/Seagate Expansion Drive/NICER/NEW/Download/2017_09_download/FTP/nicer/data/obs/2017_09/" + idnum + r"/xti/event_uf/ni" + idnum + r"_0mpu4_uf.evt.gz"
    #     path5 = r"/run/media/hutsh/Seagate Expansion Drive/NICER/NEW/Download/2017_09_download/FTP/nicer/data/obs/2017_09/" + idnum + r"/xti/event_uf/ni" + idnum + r"_0mpu5_uf.evt.gz"
    #     path6 = r"/run/media/hutsh/Seagate Expansion Drive/NICER/NEW/Download/2017_09_download/FTP/nicer/data/obs/2017_09/" + idnum + r"/xti/event_uf/ni" + idnum + r"_0mpu6_uf.evt.gz"
    #     oneIdallfilelist = [path0, path1, path2, path3, path4, path5, path6]
    #     pathlist.append(oneIdallfilelist)
    #
    #
    # for l in pathlist:
    #     print(l)



    path0 =r'/run/media/hutsh/Seagate Expansion Drive/NICER/NEW/Download/2017_09_download/FTP/nicer/data/obs/2017_09/1010010112/xti/event_uf/ni1010010112_0mpu0_uf.evt.gz'

    path1 = r'/run/media/hutsh/Seagate Expansion Drive/NICER/NEW/Download/2017_09_download/FTP/nicer/data/obs/2017_09/1010010112/xti/event_uf/ni1010010112_0mpu1_uf.evt.gz'

    hdul0 = fits.open(path0)
    time0 = hdul0[1].data['TIME']
    del hdul0

    hdul1 = fits.open(path1)
    time1 = hdul1[1].data['TIME']
    time1 = time1
    del hdul1



    comb = np.concatenate((time0,time1))
    s = comb
    #
    print(s)
    print(comb.shape)
    print(type(comb))

    for i in range(len(comb)-2):
        if comb[i] == comb[i+1]:
            print(i)




#############3
    # a = np.array([1, 3, 5])
    # b = np.array([2, 4, 6])
    # c = np.array([3, 7, 8])
    #
    # d = np.concatenate((a,b,c))
    # d.sort(kind='mergesort')
    # print(d)



if __name__ == '__main__':
    run()
