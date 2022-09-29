import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

def logistic_reg(input_file_1, input_file_2, input_file_3, input_file_4, input_file_5):

	X_train = pickle.load(open(input_file_1, "rb"))
	X_test = pickle.load(open(input_file_2, "rb"))
	A_test = pickle.load(open(input_file_5, "rb"))

	# X_train = pickle.load(input_file_1)
	# X_test = pickle.load(input_file_2)
	y_train = np.load(input_file_3)
	y_test = np.load(input_file_4)
	# A_test = pickle.load(input_file_5)

	random_seed = 42
	
	clf = LogisticRegression(random_state=random_seed)
	clf.fit(X_train, y_train)

	y_pred = clf.predict(X_test)

	score = f1_score(y_test, y_pred, average='macro')

	print(score)

	real_pred = clf.predict(A_test)

	df = pd.DataFrame(real_pred).reset_index().rename(columns={'index': 'id', 0: 'label'})

	return df


if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('input_file_1', help='X training pickle (pickle)')
	parser.add_argument('input_file_2', help='X testing pickle (pickle)')
	parser.add_argument('input_file_3', help='Y training numpy array (npy)')
	parser.add_argument('input_file_4', help='Y testing numpy array (npy)')
	parser.add_argument('input_file_5', help='Actual Testing numpy array (npy)')
	parser.add_argument('output_file', help='The predictions for the test file')
	args = parser.parse_args()

	predictions = logistic_reg(args.input_file_1, args.input_file_2, args.input_file_3, args.input_file_4, args.input_file_5)
	predictions.to_csv(args.output_file, index=False)