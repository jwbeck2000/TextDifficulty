import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

def train_test(input_file):
	df = pd.read_csv(
	    input_file
	)

	random_seed = 42

	x = df['text_processed'].values #KB changed 'original_text' tp 'text_processed' with change of data_clean.py to KB's attempt
	y = df['label'].values

	text_train, text_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=random_seed)

	return text_train, text_test, y_train, y_test


if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('input_file', help='Combined Cleaned data (CSV)')
	parser.add_argument('output_file_1', help='X training data (CSV)')
	parser.add_argument('output_file_2', help='X test data (CSV)')
	parser.add_argument('output_file_3', help='Y training data (CSV)')
	parser.add_argument('output_file_4', help='Y test data (CSV)')
	args = parser.parse_args()

	x_train, x_test, y_train, y_test = train_test(args.input_file)

	np.save(args.output_file_1, x_train)
	np.save(args.output_file_2, x_test)
	np.save(args.output_file_3, y_train)
	np.save(args.output_file_4, y_test)
