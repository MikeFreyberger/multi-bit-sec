import numpy as np
import itertools as it


def calculateDistortion(permutation, p):
	# Determine the number of distortions. 
	# This is correlated with the number of bits
	# of secrecy: bits = lg(numOfPermutations + 1)
	numOfPermutations = len(permutation)
	distortion = 0 #store the overall distortion
	distortionArray = []
	i = 0 #loop through the rows
	
	while (i < len(p)):
		total = p[i] #sum of probablities in the row
		j = 0 #loop through the columns
		max = p[i] #curren maximum
		decisionArray = {i: p[i]}
		
		# sum all the probablities and determine 
		# the maximum in the row
		while (j < len(permutation)):
			currentLetter = permutation[j][i] #current letter
			pPerm = p[currentLetter] #current prob
			if (currentLetter in decisionArray):
				decisionArray[currentLetter]+=pPerm
			else:
				decisionArray[currentLetter] = pPerm
			total += pPerm #sum all probablities
			if (decisionArray[currentLetter] > max ): #update max if necessary
				max  = decisionArray[currentLetter] 
			j+=1

		currentDistortion = (total - max) / (numOfPermutations + 1) #distortion of the row
		distortionArray.append(currentDistortion)
		distortion +=currentDistortion
		i+=1

	return {'array': distortionArray, 'total': distortion}

prob = [.35, .2, .14, .13, .1, .08]
standardOrder = [0, 1, 2, 3, 4, 5]
perm1 = [1, 2, 0, 4, 5, 3]
perm2 = [2, 0, 1, 5, 3, 4]
currentPermSet = [perm1, perm2]
dist = calculateDistortion(currentPermSet, prob)
report = [prob, standardOrder, perm1, perm2, dist['array']]
display = np.array(report)
print("Total Distortion is %f" % dist['total'])
print(display.T)

i = 0
j = 0


