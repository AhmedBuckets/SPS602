import pandas as pd

url_list = ['https://raw.githubusercontent.com/data602sps/datasetspractice/main/nba.csv', 'https://raw.githubusercontent.com/data602sps/datasetspractice/main/salarydata.csv', 'https://raw.githubusercontent.com/aelsaeyed/Data607/main/vote_predictions.csv', 'https://raw.githubusercontent.com/aelsaeyed/Data607/main/fruitvegprices-2017_2022.csv']

for i in range(0,4):
	# Q1. Load your dataset into python using the pandas library and save data into a
	# dataframe named dfi (where i is one of your datasets, for a total of 4).
	df = pd.read_csv(url_list[i], index_col=0)
	print("\n ************** Analyzing df" + str(i+1) + " **************** \n")

	# Q2. Preview your data by calling your dataframe’s name. How many columns and rows
	# do you see?
	print("\n ************** Columns and rows df" + str(i+1) + " **************** \n")
	#print(df)
	print("The number of rows are: " + str(len(df.index)))
	print("The number of rows are: " + str(len(df.columns)))

	# Q3. Examine the shape of your data using the .shape command and the data types of
	# your columns using .dtypes.
	print("\n ************** Shape and dtypes df" + str(i+1) + " **************** \n")
	print(df.shape)
	print(df.dtypes)

	# Q4. Use .describe() on your data. What do you notice about your data? What does this
	# command return?
	print("\n ************** Describe df" + str(i+1) + " **************** \n")
	print(df.describe())
	print("This returns aggregate information for each column (count, mean, stf, min, max, and quartiles)")

	# Q5. Use the .head() and .tail() command - what does this do?
	print("\n ************** Head and tail df" + str(i+1) + " **************** \n")
	print(df.head())
	print(df.tail())
	print("These print the first and last 5 rows of the data set")