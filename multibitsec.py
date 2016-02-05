#Author: Mike Freyberger

import numpy as np
import itertools as it
import sys

#general function for eavesdropper distortion
#this can handle any number of permutations.
#permutation: list of permutation arrays
#p: the original source probability distribution function
def calculateDistortion(permutation, p):
	# Determine the number of permutations. 
	# This is correlated with the number of bits
	# of secrecy: bits = lg(numOfPermutations + 1)
	numOfPermutations = len(permutation)
	distortion = 0 #store the overall distortion
	distortionArray = []
	i = 0 #loop through the bit patterns
	while (i < len(p)):
		total = p[i] #store the sum of probablities connected to bit pattern
		j = 0 #loop through the symbols connected to this bit pattern
		max = p[i] #curren max
		decisionArray = {i: p[i]}
		# sum all the probablities and determine 
		# the max input source symbol in the row
		while (j < len(permutation)): #loop through the symbols connected to this pattern
			currentLetter = permutation[j][i] #current symbol
			pPerm = p[currentLetter] #current prob
			if (currentLetter in decisionArray):
				decisionArray[currentLetter]+=pPerm #increment probability of symbol
			else:
				decisionArray[currentLetter] = pPerm #add symbol and probabilty to dict
			total += pPerm #sum all probablities
			if (decisionArray[currentLetter] > max ): #update max if necessary
				max  = decisionArray[currentLetter] 
			j+=1

		currentDistortion = (total - max)/(numOfPermutations + 1)  #distortion of the row
		distortionArray.append(currentDistortion) #save current distortion
		distortion +=currentDistortion #update total distortion
		i+=1

	return {'array': distortionArray, 'total': distortion}

	
#Main loop that takes in a comma delimited pdf
#One pdf per line of input file
#Determines the optimal encoding with lg(3) bits of secrecy
for line in sys.stdin:
	probString = line.split(',')
	prob = list(map(float, probString))

	standardOrder = range(len(prob)) #ordering with no secrecy

	perms = [p for p in it.permutations(range(len(prob)))] #find all possible permutations

	i = 0
	j = 0
	max = {'total': 0}
	while( i < len(perms)): #loop through all permutations
		
		perms1 = perms[i]
		j = i #second loop will only look at combinations we haven't analyzed
		while (j < len(perms)): #loop through all permutations combintaions
			perms2 = perms[j]
			currentPermSet = [perms1, perms2]
			dist = calculateDistortion(currentPermSet, prob)
			if (dist['total'] >= max['total']-.00001): #account for floating point errors
				max['total'] = dist['total'] #store new best permutation combination
				max['array'] = dist['array']
				max['perms1'] = perms1
				max['perms2'] = perms2
				#report = [prob, standardOrder, max['perms1'], max['perms2'], max['array']]
				#display = np.array(report)
				#print("Total Distortion is %.2f" % max['total'])
				#print(display.T)
			j+=1
		i+=1

	report = [prob, standardOrder, max['perms1'], max['perms2'], max['array']]
	display = np.array(report)
	print("Total Distortion is %f" % max['total'])
	print(display.T)


