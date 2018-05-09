"""JUST FOR GRAPH."""
import matplotlib.pyplot as plt

if __name__ == '__main__':
	leg = ['3D-Random Walk', '2D-Random Walk']
	prob3 = [1, 0.998, 0.9668, 0.6978, 0.4032, 0.1953, 0.0816, 0.0314, 0.0124, 0.0039]
	prob2 = [1, 0.9994, 0.9976, 0.9896, 0.9562, 0.887, 0.7845, 0.6611, 0.5158, 0.3794, 0.2616, 0.1707, 0.1044, 0.0597, 0.0364, 0.0201, 0.0121, 0.0049, 0.0032, 0.0016]
	plt.plot(prob3, 'ro-')
	plt.plot(prob2, 'bo-')
	plt.title('Probability of Repeated States in Different Dimensions')
	plt.ylabel('Probability')
	plt.xlabel('Length of Walk')
	plt.legend(leg)
	plt.show()