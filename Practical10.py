def AnalyseStudents(x):
	try:
		y=8
		sum=0
		for digit in x:
			result=int(digit)*y
			sum+=result
			y-=1
		if sum%11==0:
			return 1
		else:
			return 0
	except:
			return 0
def Read(list):
	try:
		list=[]
		INFILE=open("Data.txt","r")
		count=0
		for line in INFILE:
			list.append(line.rstrip())
			count+=1
			INFILE.close()
			return count
	except:
			print("Error in reading the file")
			exit()
	
def Write(num,valid):
	VFILE=open("validNumbers.txt","a")
	IFILE=open("InvalidNumbers.txt","a")
	if valid==1:
		VFILE.write(num+"\n")
		print(num,"is a VALID student number")
	if valid==0:
		IFILE.write(num+"\n")
