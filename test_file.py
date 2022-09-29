import pandas as pd
import numpy as np

def test_file(input_file):
	df = pd.read_csv(
	    input_file
	)

	random_seed = 42

	x = df['original_text'].values

	test_data = np.array(x)

	return test_data


if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('input_file', help='WikiLarge_Test data (CSV)')
	parser.add_argument('output_file', help='WikiLarge_Test data text (npy)')
	args = parser.parse_args()

	test_data = test_file(args.input_file)

	np.save(args.output_file, test_data)
