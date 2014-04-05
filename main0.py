### Google HashCode Paris 2014
import numpy as np
import scipy.sparse
import random

fName = "test"
fName = "paris_54000"
fin = open(fName + ".txt")

N, M, T, C, S = map(int,fin.readline().strip().split())
cost = [[0 for x in xrange(N)] for x in xrange(N)] #[[0]*N]*N
reward = [[0 for x in xrange(N)] for x in xrange(N)]#[[0]*N]*N
for i in range(N):
	drop = fin.readline()
for i in range(M):
	a,b,d,c,l =  map(int,fin.readline().strip().split())
	if d == 2 :
		cost[a][b] = c
		reward[a][b] = l
		cost[b][a] = c
		reward[b][a] = l
	else :
		cost[a][b] = c
		reward[a][b] = l    

#print cost[N-1][N-1]
#print cost[4516][2666]
#print cost[2666][4516]

class Car(object):
	def __init__(self,start):
		self.paths = [start]
		self.time = 0
		self.rew = 0
		global T
        
	def get_best_next_pos(self):
		pos = self.paths[-1]        
		# descending sorted list of lengths from cur to other destinqtions
		dest = reward[pos][:]		
		# indexes of the sorted list
		destSortedIdx = sorted(range(len(dest)), key=lambda k: dest[k]) #[dest.index(x) for x in destSorted]
		destSortedIdx = destSortedIdx[::-1]
		#print "destSortedIdx"
		#print destSortedIdx
		#Filtering destSortedIdx for possible destinations, not exceding time T and existing paths (cost[pos][newpos] != 0
		destIdx = [i for i in destSortedIdx if cost[pos][i] != 0 and cost[pos][i] + car.time <= T]
		#print destIdx
		if not destIdx:
			return -1
		elif (reward[pos][destIdx[0]] > 0):
			return destIdx[0]
		else:
			x = random.randint(0,len(destIdx)-1)
			return destIdx[x]
		
cars = []
for i in range(C):
	cars.append(Car(S))
for i in range(len(cars)):
	car = cars[i]
	#print "Car" + str(i+1)
	pos = S
	#print pos
	while pos != -1 :
		newpos = car.get_best_next_pos()		
		if newpos == -1:
			break
		#print "Car" + str(i+1)
		#print newpos
		car.time += cost[pos][newpos]
		car.rew += reward[pos][newpos]
		car.paths.append(newpos)
		reward[pos][newpos] = 0
		reward[newpos][pos] = 0
		pos = newpos

print len(cars)
for i in range(len(cars)):
	car = cars[i]
	l = len(car.paths)
	print l
	for j in range(l):
		print car.paths[j]

        
        
           
            