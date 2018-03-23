# -*- coding: utf-8 -*-
"""
@author: Vartika Sharma
"""
import math

#Definie class similarity
class similarity:
	
	# Class instantiation 
	def __init__ (self, ratingP, ratingQ):
		self.ratings1 = ratingP
		self.ratings2 = ratingQ
	
	# Minkowski Distance between two vectors
	def minkowski(self, r):
		distance = sum(math.pow(abs(i-j),r) for i,j in zip(self.ratings1, self.ratings2))
		return round(math.pow(distance,(1/float(r))),4)
	
	# Pearson Correlation between two vectors
	def pearson(self):
		total_sum=0
		sum1=0 
		sum2=0
		sum1_square=0
		sum2_square=0
		length=0
    
		for key in range(len(self.ratings1)) and range(len(self.ratings2)):
			total_sum = total_sum + (self.ratings1[key] * self.ratings2[key])
			sum1 += self.ratings1[key]
			sum2 += self.ratings2[key]
			sum1_square += math.pow(self.ratings1[key], 2)
			sum2_square += math.pow(self.ratings2[key], 2)	
        
			length += 1
        
		#Calculating Pearson Coefficient covariance and standard deviation
		cov = (total_sum - (sum1*sum2)/length)
		sd_1 = math.sqrt(sum1_square - math.pow(sum1, 2)/length) 
		sd_2 = math.sqrt(sum2_square - math.pow(sum2, 2)/length)
		P_coeff = round(cov/(sd_1 * sd_2), 4) # Rounding off to four decimal places
		return P_coeff 	

# Change Input (User Ratings)
UserPRatings = {'Motorola':8, 'LG':5, 'Sony':1, 'Apple':1, 'Samsung':5, 'Nokia':7}
UserQRatings = {'Apple':7, 'Samsung':1, 'Nokia':4, 'LG':4, 'Sony':6, 'Blackberry':3}

ratingP = []
ratingQ = []
		
for key in set(sorted(UserPRatings.keys())) & set(sorted(UserQRatings.keys())):
	ratingP.append(UserPRatings[key])
	ratingQ.append(UserQRatings[key])

#Creating an object of class similarity	
FindSimilarity = similarity(ratingP, ratingQ)

#Print Output (We call the minkowski and pearson class methods to calculate the following measures.)
print ("Manhattan Distance for the given User Ratings:", FindSimilarity.minkowski(1))
print ("Euclidean Distance for the given User Ratings:", FindSimilarity.minkowski(2))
print ("Minkowski Distance for the given User Ratings:", FindSimilarity.minkowski(3))
print ("Pearson coefficient for the given User Ratings:", FindSimilarity.pearson())