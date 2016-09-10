import numpy as np

def normalize(input):
	mean_input = np.mean(input)
	std_input = np.std(input)
	norm_input = (input-mean_input)/std_input
	return norm_input
