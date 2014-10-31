"""
add a docstring later
"""

def calcLogLikelihood(modelLambda,modelOmega):
# Omega => observations
# Lamba => expectations

	#init our variables
	if len(modelLamba == len(modelOmega):
		logLikelihood = [0]*len(modelLamba)
	joint_log_likelihood = long(0)
	discardModel = False

	#iterate i times, to a total as the length of our Model
	for i in range(len(modelLamba)):
		if modelLamba[i] == 0:
			modelLamba[i] += 1
		if (modelOmega[i] == 0 and modelLamba[i] == 0):
			log_likelihood[i] += 1
		elif (modelOmega[i] != 0 and modelLamba[i] == 0):
			log_likelihood[i] = Decimal('-Infinity')
			discardModel = True
		#this part had to do with the factorial issue we had last time, i dont think we will need this any longer once we are going to use the log property Claus told about.
		if(modelOmega[i] > 100):
			cast = 99
		else:
			cast = modelOmega[i]
		#end of it

		#had to change this is order to use the log property
		log_likelihood[i] = -modelLamba[i] + (modelOmega[i]*math.log10(modelLamba[i])) - (math.log10(float(fatorial[cast])))

	#calcula o joint_log_likelihood
	joint_log_likelihood = sum(log_likelihood)

	return log_likelihood, joint_log_likelihood, discardModel


