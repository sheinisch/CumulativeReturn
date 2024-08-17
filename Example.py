from NM_Finance import calculate_cumulative_return
import pandas as pd

bond_data = pd.read_csv('Bond_Data.csv')
print(f'Dataset:\n{bond_data}')

#Get the cumulative return for the first row
returns = []

for r in range(1,6):
    col = f'Period_{r}'
    returns.append(bond_data.iloc[0][col])
    
print(f'\nCumulative Return for first row: {calculate_cumulative_return(returns)}')

#Calculate the cumulative return for each row and add it as a new column
bond_data['Cumulative Return'] = bond_data.apply(
    lambda row: calculate_cumulative_return([row['Period_1'], row['Period_2'], row['Period_3'], row['Period_4'], row['Period_5']]),
    axis=1
)

print(f'\nDataset with Cumulative Returns:\n{bond_data}')