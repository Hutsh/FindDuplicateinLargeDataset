from astropy.io import fits
import numpy as np
import re,time,os,collections,glob
import fileinput
import config as cfg

def trans2txts_of_one_data(id, savefolder='text'):
    # transform all data files in one data pack into corresponding txts
    filelist = cfg.get_fits_list(id)
    for fi in filelist:
        cfg.trans_fits_to_txt(fi, savefolder)

    txt_list = glob.glob(os.path.join(savefolder,'*.txt')) 

    with open(os.path.join(savefolder, str(id) + '.txt'), 'w') as fout:
        for txtfi in txt_list:
            with fileinput.input(txtfi) as fin:
                for line in fin:
                    fout.write(line)
            os.remove(txtfi)




if __name__ == '__main__':
    trans2txts_of_one_data(1010010112,'text')
