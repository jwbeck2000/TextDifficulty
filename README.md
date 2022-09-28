# TextDifficulty
This a text classification task to determine if textual information is comprehensible by audiences who may not have high reading proficiency.
# Data
### dale_chall.csv
The Dale Chall file is a list of approximately 3,000 elementary English words that are typically familiar to 80% of Americann 4th grade students in the 90s.  
### AoA_Words.csv  

The AoA Words file is a list of approximate age (in years) when a word was learned for 50,000 English words.  
### Wiki_Train_1.csv | Wiki_Train_2.csv | Wiki_Train_3.csv  

The Wiki_Train files are three files that contain training data consisting of 416,768 sentences drawn from wikipedia articles.  The training files are labeled as 
  * 0 - The sentence does not need to be simplified
  * 1 - The sentence does need to be simplified. 
  
The original Wiki_Train file was split into three files in order to be uploaded to Git.  They will need to be joined in the code.  
### Wiki_Test.csv  
The Wiki_Test file contains 119,092 comments that are unlabeled. The predictions on this file should be submitted in a .csv (comma separated free text) file with a header line "ID, Category" followed by exactly 119,092 lines. In each line, there should be exactly two integers, separated by a comma. The first integer is the line ID of a test sentence **(0-119,091)**, and the second integer is the category your classifier predicts one of (0,1).
