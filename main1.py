### Google HashCode Paris 2014
import numpy as np
import scipy.sparse
import random
import math

#fName = "test"
fName = "paris_54000"
fin = open(fName + ".txt")

N, M, T, C, S = map(int,fin.readline().strip().split())
coord = [[0 for x in xrange(N)] for x in xrange(2)] #[[0]*N]*N
zone = [0 for x in xrange(N)] #[[0]*N]*N
cost = [[0 for x in xrange(N)] for x in xrange(N)] #[[0]*N]*N
reward = [[0 for x in xrange(N)] for x in xrange(N)]#[[0]*N]*N
max_lon =0
min_lon =1000
max_lat = 0
min_lat = 1000
#print coord
for i in range(N):
	lat,lon = fin.readline().strip().split()
	lat = float(lat)
	lon = float(lon)
	#print i,N
	coord[0][i] = lat
	coord[1][i] = lon
	if lat < min_lat:
		min_lat = lat
	elif lat > max_lat:
		max_lat = lat
	if lon < min_lon:
		min_lon = lon
	elif lon > max_lon:
		max_lon = lon
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

#Normalizing
for i in range(N):
	coord[0][i] = 2*(coord[0][i]-min_lat)/(max_lat -min_lat)-1
	coord[1][i] = 2*(coord[1][i]-min_lon)/(max_lon -min_lon)-1
	
#print coord

#Defining zones
for i in range(N):
	if coord[0][i] > 0:
		if coord[1][i] > 0:
			if coord[1][i] >coord[0][i]:
				zone[i]=0
			else:
				zone[i] = 1
		else :
			if abs(coord[1][i])>abs(coord[0][i]):
				zone[i] = 2
			else :
				zone[i] = 3
	else:
		if coord[1][i] > 0:
			if abs(coord[1][i]) >abs(coord[0][i]):
				zone[i]=4
			else:
				zone[i] = 5
		else :
			if abs(coord[1][i])>abs(coord[0][i]):
				zone[i] = 6
			else :
				zone[i] = 7

class Car(object):
	def __init__(self,start):
		self.paths = [start]
		self.time = 0
		self.rew = 0
		global T
        
	def get_best_next_pos(self,z):
		pos = self.paths[-1]        
		# descending sorted list of lengths from cur to other destinqtions
		dest = reward[pos][:]		
		# indexes of the sorted list
		destSortedIdx = sorted(range(len(dest)), key=lambda k: dest[k]) #[dest.index(x) for x in destSorted]
		destSortedIdx = destSortedIdx[::-1]
		#print "destSortedIdx"
		#print destSortedIdx
		#Filtering destSortedIdx for possible destinations, not exceding time T and existing paths (cost[pos][newpos] != 0
		destIdx0 = [i for i in destSortedIdx if cost[pos][i] != 0 and cost[pos][i] + car.time <= T]
		destIdx = [i for i in destIdx0 if zone[i]==z]
		#print destIdx
		if not destIdx0:
			return -1
		if not destIdx:
			x = random.randint(0,len(destIdx0)-1)
			return destIdx0[x]
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
	z = i
	#print "Car" + str(i+1)
	pos = S
	#print pos
	while pos != -1 :
		newpos = car.get_best_next_pos(z)		
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

        
        
           
            