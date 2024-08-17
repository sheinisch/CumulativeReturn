== Standalone Python Library ==

NM_Finance.py is a proof-of-concept of a custom Python library that could be developed to perform various finance-related tasks
Currently the only function this library contains is calculate_cumulative_return()
This function takes a list of returns and caluculates the cumulative return

Example.py shows how the NM_Finance library could be imported and used.

1. Save NM_Finance.py, Example.py, and Bond_Data.csv all in the same location
2. Open Example.py in IDLE or your preferred Python IDE and run it to see how it uses NM_Finance to calculate cumulative returns
	- Note that Example.py requires the pandas library to be available



If you want to run the Snowflake worksheets below, I created a temporary password for my account so you can access the database. The dataset is the same as the one in the previous example.

username: sheinisch
password: Pass123!


== Snowflake via SQL ==

1. Navigate to the Snowflake worksheet: https://app.snowflake.com/hzuyajc/xx56150/w1u8G9Z6YoPv#query
2. Run the various SQL commands to see the dataset and cumulative returns. We use two different methods




== Snowflake User-Defined Function ==

1. Navigate to the Snowflake worksheet: https://app.snowflake.com/hzuyajc/xx56150/w14KjAeWsEIx#query
2. Highlight and run lines 4-20 to create the function using Python code
3. Run the subsequent SQL command to call the UDF




== Future work ==
Add error-handling of bad values.
Generalize to any number of periods instead of hard-coding to 5.
Test performance on larger datasets.
