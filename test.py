
from astropy.io import fits
import os
import numpy as np
import re
import collections



def save_time_in_txt(fitsFilePath):
    filename = os.path.basename(fitsFilePath)
    hdul = fits.open(fitsFilePath)
    data = hdul[1].data
    time = hdul[1].data['TIME']
    rawx = hdul[1].data['RAWX']
    rawy = hdul[1].data['RAWY']
    # print(hdul[1].data['RAWX'])
    # print(hdul[1].data['RAWY'])

    # c = np.concatenate((rawx, rawy), axis=0)
    c = np.column_stack((time.astype(np.object), rawx, rawy))
    print("shape of C:", c.shape)
    print("shape of rawx:", rawx.shape)
    print("shape of rawy:", rawy.shape)
    print(c)

    # print(time)
    del hdul

    
    # np.savetxt("text/" + filename + ".txt", time, delimiter="\n")


if __name__ == '__main__':
    path = r"/run/media/hutsh/Seagate Expansion Drive/NICER/NEW/Download/2017_09_download/FTP/nicer/data/obs/2017_09/1010010112/xti/event_uf/ni1010010112_0mpu0_uf.evt.gz"
    save_time_in_txt(path)