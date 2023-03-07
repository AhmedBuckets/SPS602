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
	print("This returns aggregate information (count, mean, stf, min, max, and quartiles)")

	# Q5. Use the .head() and .tail() command - what does this do?
	print("\n ************** Head and tail df" + str(i+1) + " **************** \n")
	print(df.head())
	print(df.tail())
	print("These print the first and last 5 rows of the data set")


print("\n \n ************** EXTRA CREDIT **************** \n")
# Extra Credit (3 pts)
# 1. Choose one of your datasets and remove the header information. (Can delete
# the row in excel, etc..)
no_header_url = 'https://raw.githubusercontent.com/AhmedBuckets/SPS602/main/nba_modded.csv'

# 2. Import the data into your environment using pandas. Display the .head() of your
# data showing no header information.
print("Showing the df with no headers: ")
no_header_pd = pd.read_csv(no_header_url, header=None)
print(no_header_pd.head())

# 3. Using pandas, update the dataset to include the header information. Display the
# updated data using .head().
print("\n Adding back headers:")
updated_headers_df = no_header_pd.set_axis(["Name","Team","Number","Position","Age","Height","Weight","College","Salary"], axis=1, inplace=False)
print(updated_headers_df.head())

print("\n \n ************** EXTRA CREDIT 2 **************** \n")
print("Investigating missing data in the above NBA dataframe:")

# 1. Import a “dirty” dataset from the internet into your environment. (Missing values,
# improper coding of columns, etc.)
print(updated_headers_df.isnull().sum())

# 2. Clean or “tidy” the data when loading into python using pandas.
print("\n It appears there exist nulls in the College and Salary columns in this data set. ")
print("For cleanliness we can label the null colleges Unknown instead of leaving them blank: ")
updated_headers_df["College"].fillna("Unknown", inplace = True)
print(updated_headers_df.isnull().sum())

print("We can also include/impute a salary, or simply drop the rows that contain no salary if it doesn't make sense to impute.")
cleaned_df = updated_headers_df.dropna()
print(cleaned_df.isnull().sum())
