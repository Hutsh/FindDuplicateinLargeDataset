
if __name__ == '__main__':
	with open('workingdata2/number.txt', 'w') as out:
		for i in range(2**16):
			out.write(str(i) + '\n')
			print(i)
