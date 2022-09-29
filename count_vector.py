import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import pickle

def count_vector(input_file_1, input_file_2, input_file_3):
	
	text_train = np.load(input_file_1, allow_pickle=True)
	text_test = np.load(input_file_2, allow_pickle=True)
	test_data = np.load(input_file_3, allow_pickle=True)

	vectorizer = CountVectorizer()

	X_train = vectorizer.fit_transform(text_train)

	X_test = vectorizer.transform(text_test)

	A_test = vectorizer.transform(test_data)

	return X_train, X_test, A_test


if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('input_file_1', help='Training numpy array (npy)')
	parser.add_argument('input_file_2', help='Testing numpy array (npy)')
	parser.add_argument('input_file_3', help='Actual testing numpy array (npy)')
	parser.add_argument('output_file_1', help='CountVector for the training data (pkl)')
	parser.add_argument('output_file_2', help='CountVector for the testing data (pkl)')
	parser.add_argument('output_file_3', help='TfidfVector for the actual testing data (pkl)')
	args = parser.parse_args()

	X_train, X_test, A_test = count_vector(args.input_file_1, args.input_file_2, args.input_file_3)
	pickle.dump(X_train, open(args.output_file_1, "wb"))
	pickle.dump(X_test, open(args.output_file_2, "wb"))
	pickle.dump(A_test, open(args.output_file_3, "wb"))