#fName = "doodle"
fName = "test"
n = 5
m = 7

fin = open(fName + ".out")
fout = open(fName + ".check", "w")

k = map(int,fin.readline().strip().split())
k = k[0]


for i in range(k):
	line = fin.readline().strip().split()
	if line[0] == "PAINTSQ" :
		r = line[1]
		c = line[2]
		s = line[3]
	else :
		r = line[1]
		c = line[2]
		
	print line


		  
fin.close()
fout.close()