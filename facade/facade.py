#fName = "doodle"
fName = "test"

fin = open(fName + ".txt")
fout = open(fName + ".out", "w")

n,m = map(int, fin.readline().strip().split())



		  
fin.close()
fout.close()