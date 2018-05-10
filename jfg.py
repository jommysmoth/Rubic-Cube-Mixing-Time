"""JUST FOR GRAPH."""
import matplotlib.pyplot as plt

if __name__ == '__main__':
	leg = ['3D-Random Walk', '2D-Random Walk', '3D-Random Walk Translation-Restricted: 2', '3D-Random Walk Translation-Restricted: 1',
		   '3D-Random Walk Rotation-Restricted: 2', '2D-Random Walk Translation-Restricted: 2', '2D-Random Walk Rotation-Restricted: 2', '2D-Random Walk Translation-Restricted: 1']
	prob3 = [1, 0.998, 0.9668, 0.6978, 0.4032, 0.1953, 0.0816, 0.0314, 0.0124, 0.0039]
	prob2 = [1, 0.9986, 0.9868, 0.8829, 0.6709, 0.4512, 0.2736, 0.1533, 0.0852, 0.0398, 0.0201, 0.0112, 0.0047]
	prob1 = [1, 0.9986, 0.9849, 0.8466, 0.5809, 0.3517, 0.1739, 0.0876, 0.0371, 0.0149, 0.0069]
	prob4 = [1, 0.9992, 0.9953, 0.9669, 0.7943, 0.4787, 0.2283, 0.107, 0.0478, 0.0225, 0.0096]
	prob5 = [1, 0.9989, 0.9889, 0.8922, 0.7182, 0.5158, 0.3216, 0.1848, 0.0926, 0.0416, 0.0189, 0.0078]
	prob6 = [1, 0.999, 0.9939, 0.9614, 0.8408, 0.6842, 0.5176, 0.372, 0.2611, 0.1624, 0.1095, 0.0653, 0.0389, 0.0227, 0.0129, 0.0076]
	prob7 = [1, 0.9992, 0.9953, 0.9699, 0.8816, 0.7553, 0.5993, 0.434, 0.2888, 0.178, 0.0996, 0.0553, 0.028, 0.0149, 0.0066]
	prob8 = [1, 0.9994, 0.998, 0.9926, 0.972, 0.9041, 0.767, 0.6059, 0.4517, 0.3423, 0.2512, 0.1802, 0.1247, 0.0835, 0.0537, 0.0396, 0.0236, 0.0136, 0.0074]




	plt.plot(prob3, 'o-')
	plt.plot(prob2, 'o-')
	plt.plot(prob1, 'o-')
	plt.plot(prob4, 'o-')
	plt.plot(prob5, 'o-')
	plt.plot(prob6, 'o-')
	plt.plot(prob7, 'o-')
	plt.plot(prob8, 'o-')

	plt.title('Probability of Repeated States in Different Dimensions')
	plt.ylabel('Probability')
	plt.xlabel('Length of Walk')
	plt.legend(leg)
	plt.show()