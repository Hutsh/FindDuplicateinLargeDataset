import os, subprocess
import combine_uf
import hash_separate
import find_duplicate


def check_folders():
    if not os.path.exists('text'):
        os.mkdir('text')
    if not os.path.exists('workingdata'):
        os.mkdir('workingdata')

def clean():
	if  os.listdir('./workingdata'):
		subprocess.call("rm ./workingdata/*.txt",shell=True)
	if  os.listdir('./text'):
		subprocess.call("rm ./text/*.txt",shell=True)

def start_oneid_pipline(idn):
	clean()
	check_folders()
	combine_uf.save_id_fists_to_one_text(idn) #save .gz fits file into id.txt in text folder.
	hash_separate.start_sep(idn, 512) # separate id.txt into N parts
	res = find_duplicate.get_dup_info()
	find_duplicate.save_result(res)
	clean()

if __name__ == "__main__":
	with open('idlist.txt', 'r') as idlist:
		for idn in idlist:
			idn = idn.strip()
			print("Start " + idn)
			start_oneid_pipline(idn)
			print("Finish " + idn + "\n-----------------------------")
	

