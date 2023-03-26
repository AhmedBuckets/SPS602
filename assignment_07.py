import pandas as pd
from pandas.api.types import is_numeric_dtype

#I've uploaded the file to my github page and will use read_csv from the pandas library to access it
df = pd.read_csv('https://raw.githubusercontent.com/AhmedBuckets/SPS602/main/Phishing_Legitimate_full.csv')

summary_stats = df.groupby("CLASS_LABEL")["UrlLength"].describe()
print(summary_stats)

columns_i_want = ["NumDots","NumDash", "InsecureForms", "PctNullSelfRedirectHyperlinks", "FrequentDomainNameMismatch", "SubmitInfoToEmail", "PctExtNullSelfRedirectHyperlinksRT", "CLASS_LABEL"]

my_set = df[columns_i_want]
print(my_set)

#1. Modify multiple column names:
my_set.rename(columns={"NumDash": "num_dashes", "InsecureForms": "insecure_forms", "FrequentDomainNameMismatch": "freq_domain_name_mismatch", "PctNullSelfRedirectHyperlinks": "pct_null_self_redirect", "SubmitInfoToEmail": "submit_info_to_email", "PctExtNullSelfRedirectHyperlinksRT": "pct_null_self_redirect_rt", "CLASS_LABEL": "label"}, inplace=True)
print(my_set)

# #2. Convert a column to a different data type:
my_set.info()
my_set["pct_null_self_redirect_rt"] = my_set["pct_null_self_redirect_rt"].astype(float)
my_set.info()

# #3. Fill missing values with a specific value:
# Normally I would use my_set["column_name"].fillna(0, inplace=True) to fill in missing data, however I checked it out and the columns that I chose are not missing any.
missing_mask = my_set.isna()
missing_count = missing_mask.sum()

# display missing value information
print("Missing value information:")
print(missing_count)

# #4. Create a new column based on existing columns or calculations:
my_set["pct_redirect_mean"] = (my_set["pct_null_self_redirect"] + my_set["pct_null_self_redirect_rt"])/2
print(my_set)

# #5. Drop column(s) from your dataset:
my_set.drop(columns=["NumDots"], inplace=True)
print(my_set)

# #6. Drop a row(s) from your dataset:
my_set.drop(index=[0, 4], inplace=True)
my_set.reset_index(inplace=True, drop=True)
print(my_set)

# #7. Sort your data based on multiple variables:
my_set.sort_values(by=["pct_null_self_redirect", "pct_null_self_redirect_rt"], ascending=[True, False], inplace=True)
print(my_set)

# #8. Filter your data based on some condition:
filtered_data = my_set[my_set["pct_redirect_mean"] > 0]
print(filtered_data)

# #9. Convert all the string values to upper or lower cases in one column:
# None of the columns in my set are strings


# #10. Check whether numeric values are present in a given column of your dataframe:
is_numeric_dtype(my_set["num_dashes"])

# #11. Group your dataset by one column, and get the mean, min, and max values by group:
grouped_data = my_set.groupby("label").describe()
print(summary_stats)

#               count     mean        std   min   25%   50%   75%    max
# CLASS_LABEL
# 0            5000.0  72.7498  30.837837  12.0  51.0  68.0  90.0  218.0
# 1            5000.0  67.7784  35.552610  19.0  46.0  58.0  75.0  253.0

# #12. Group your dataset by two columns and then sort the aggregated results within the groups:
grouped_data = my_set.groupby(["label", "insecure_forms"]).describe().sort_values(by=[("num_dashes", "count")])
print(grouped_data)

#                      num_dashes                                                ... pct_redirect_mean
#                           count      mean       std  min  25%  50%  75%   max  ...             count      mean       std  min  25%  50%       75%       max
# label insecure_forms                                                           ...
# 1     0                   205.0  1.058537  2.125127  0.0  0.0  1.0  1.0  20.0  ...             205.0  0.234914  0.333463 -0.5  0.0  0.5  0.500000  0.600000
# 0     0                  1354.0  2.694239  4.064649  0.0  0.0  1.0  4.0  55.0  ...            1354.0  0.403643  0.232960 -0.5  0.5  0.5  0.508830  0.625000
#       1                  3646.0  3.078168  3.810055  0.0  0.0  1.0  5.0  26.0  ...            3646.0  0.418150  0.218709 -0.5  0.5  0.5  0.511565  0.651832
# 1     1                  4793.0  0.645107  1.186257  0.0  0.0  0.0  1.0  15.0  ...            4793.0  0.027522  0.421770 -0.5 -0.5  0.0  0.500000  0.636364



