import numpy as np

def check_data(data):
	if data.sum() != 1.0:
		print("input doesn't meet sum=1")
		return -1
	elif len(set(data)) != len(data):
		print("duplicate input element")
		return -1
	else:
		print("input successfully")
		return data

def execute(data, alpha):
	accumalate = 0
	table = []
	for (i, num) in enumerate(data):
		accumalate += num
		if accumalate >= alpha:
			print("index is: ", i)
			break
				
	

if __name__ == '__main__':
	data = np.array([0.1,0.4,0.3,0.2])
	data = check_data(data)
	alpha = 0.5
	execute(data, 0.4)
	pass
