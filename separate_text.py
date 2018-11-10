import os
import subprocess


def count_lines(path):
	with open(path) as f:
		size=sum(1 for _ in f)
	print(size)
	return size


def sep_into_n(n, textPath):
	numberOfLines = count_lines(textPath)
	linesInEach = int(numberOfLines / n) + 1
	idn = os.path.basename(textPath).strip(".txt")
	print(idn)

	cdcmd = "cd " + os.path.dirname(textPath)
	cmd = "split -a 4 -d -l " + str(linesInEach) + " " + os.path.basename(textPath) +" sep_"
	print(cmd)

	with open("./workingdata/temp.sh", 'w') as tempsep:
		tempsep.write("mv " + textPath + " ./workingdata" + '\n')
		tempsep.write("cd ./workingdata\n")
		tempsep.write(cmd)

	os.system("sh ./workingdata/temp.sh")
	os.system("rm ./workingdata/temp.sh")
	os.system("mv ./workingdata/" + os.path.basename(textPath) + " ./text")


def sep_text_given_id(id):
	pass


if __name__ == '__main__':
	path = "./text/1010010112.txt"
	sep_into_n(200, path)