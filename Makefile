outputs/lr_predictions.csv: logistic_reg.py outputs/X_train_tfidf.pickle outputs/X_test_tfidf.pickle outputs/y_train.npy outputs/y_test.npy outputs/A_test_tfidf.pickle
	python3 logistic_reg.py outputs/X_train_tfidf.pickle outputs/X_test_tfidf.pickle outputs/y_train.npy outputs/y_test.npy outputs/A_test_tfidf.pickle outputs/lr_predictions.csv

outputs/X_train_count.pickle outputs/X_test_count.pickle: count_vector.py outputs/x_train.npy outputs/x_test.npy outputs/test_data.npy
	python3 count_vector.py outputs/x_train.npy outputs/x_test.npy outputs/test_data.npy outputs/X_train_count.pickle outputs/X_test_count.pickle outputs/A_test_count.pickle

outputs/X_train_tfidf.pickle outputs/X_test_tfidf.pickle: tfidf_vector.py outputs/x_train.npy outputs/x_test.npy outputs/test_data.npy
	python3 tfidf_vector.py outputs/x_train.npy outputs/x_test.npy outputs/test_data.npy outputs/X_train_tfidf.pickle outputs/X_test_tfidf.pickle outputs/A_test_tfidf.pickle

outputs/x_train.npy outputs/x_test.npy outputs/y_train.npy outputs/y_test.npy: train_test.py outputs/combined.csv
	python3 train_test.py outputs/combined.csv outputs/x_train.npy outputs/x_test.npy outputs/y_train.npy outputs/y_test.npy

outputs/test_data.npy: test_file.py data/Wiki_Test.csv
	python3 test_file.py inputs/Wiki_Test.csv outputs/test_data.npy

outputs/combined.csv: combine.py data/Wiki_Train_1.csv data/Wiki_Train_2.csv data/Wiki_Train_3.csv
	python3 combine.py data/Wiki_Train_1.csv data/Wiki_Train_2.csv data/Wiki_Train_3.csv outputs/combined.csv