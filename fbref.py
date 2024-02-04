import pandas as pd

# Assuming df is a list of DataFrames obtained from read_html
df = pd.read_html('https://fbref.com/en/comps/9/gca/Premier-League-Stats')

# Flatten MultiIndex columns
for idx, data_frame in enumerate(df):
    if isinstance(data_frame.columns, pd.MultiIndex):
        data_frame.columns = ['_'.join(map(str, col)).strip() for col in data_frame.columns]

# Print the DataFrame
print(df)

# Save the DataFrame to an Excel file
excel_filename = 'PremierLeague.xlsx'

with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
    for idx, data_frame in enumerate(df):
        data_frame.to_excel(writer, sheet_name=f'data_frame_{idx + 1}', index=False)

print(f'Data saved to {excel_filename}')
