outputs/lr_predictions.csv: logistic_reg.py outputs/X_train_tfidf.pickle outputs/X_test_tfidf.pickle outputs/y_train.npy outputs/y_test.npy outputs/A_test_tfidf.pickle
	python3 logistic_reg.py outputs/X_train_tfidf.pickle outputs/X_test_tfidf.pickle outputs/y_train.npy outputs/y_test.npy outputs/A_test_tfidf.pickle outputs/lr_predictions.csv

outputs/X_train_count.pickle outputs/X_test_count.pickle outputs/X_train_feature_names.pickle: count_vector.py outputs/x_train.npy outputs/x_test.npy outputs/test_data.npy
	python3 count_vector.py outputs/x_train.npy outputs/x_test.npy outputs/test_data.npy outputs/X_train_count.pickle outputs/X_test_count.pickle outputs/A_test_count.pickle outputs/X_train_feature_names.pickle

outputs/X_train_tfidf.pickle outputs/X_test_tfidf.pickle: tfidf_vector.py outputs/x_train.npy outputs/x_test.npy outputs/test_data.npy
	python3 tfidf_vector.py outputs/x_train.npy outputs/x_test.npy outputs/test_data.npy outputs/X_train_tfidf.pickle outputs/X_test_tfidf.pickle outputs/A_test_tfidf.pickle

outputs/x_train.npy outputs/x_test.npy outputs/y_train.npy outputs/y_test.npy: train_test.py outputs/clean_combined.csv
	python3 train_test.py outputs/clean_combined.csv outputs/x_train.npy outputs/x_test.npy outputs/y_train.npy outputs/y_test.npy

outputs/test_data.npy: test_file.py data/Wiki_Test.csv
	python3 test_file.py inputs/Wiki_Test.csv outputs/test_data.npy

outputs/wordcloud_zero.png outputs/wordcloud_one.png: word_clouds.py outputs/clean_combined.csv
	python3 word_clouds.py outputs/clean_combined.csv outputs/wordcloud_zero.png outputs/wordcloud_one.png

outputs/clean_combined.csv: data_clean.py outputs/combined.csv
	python3 data_clean.py outputs/combined.csv outputs/clean_combined.csv

outputs/clean_combined.csv: feature_extraction.py outputs/clean_combined.csv
	python3 feature_extraction.py outputs/clean_combined.csv
	
outputs/combined.csv: combine.py data/Wiki_Train_1.csv data/Wiki_Train_2.csv data/Wiki_Train_3.csv
	python3 combine.py data/Wiki_Train_1.csv data/Wiki_Train_2.csv data/Wiki_Train_3.csv outputs/combined.csv
