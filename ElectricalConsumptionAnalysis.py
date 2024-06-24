import pandas as pd

# Loading the CSV file
file_path = CSV_FILEPATH

# Reading the CSV file
df = pd.read_csv(file_path, encoding='utf-8')

# Converting the 'time' column to datetime
df['time'] = pd.to_datetime(df['time'])

# Convert the 'time' column to the required timezone (Indian/Mauritius)
df['time'] = df['time'].dt.tz_convert('Indian/Mauritius')

# Filter for 'electrical_consumption' variable only
df_electrical = df[df['variable'] == 'electrical_consumption']

# Defining the time range in Indian/Mauritius timezone
start_time = pd.Timestamp('2024-04-10 00:00:00', tz='Indian/Mauritius')
end_time = pd.Timestamp('2024-04-17 00:00:00', tz='Indian/Mauritius')

# Filter the dataframe for the given time range
df_filtered = df_electrical[(df_electrical['time'] >= start_time) & (df_electrical['time'] < end_time)]

# Find the closest timestamp to start_time
closest_start_idx = (df_filtered['time'] - start_time).abs().argmin()
closest_start_time = df_filtered.iloc[closest_start_idx]['time']
closest_start_value = df_filtered.iloc[closest_start_idx]['value']

# Find the closest timestamp to end_time
closest_end_idx = (df_filtered['time'] - end_time).abs().argmin()
closest_end_time = df_filtered.iloc[closest_end_idx]['time']
closest_end_value = df_filtered.iloc[closest_end_idx]['value']

# Calculate the difference in consumption
consumption_difference = closest_end_value - closest_start_value

# Print the closest start time, closest end time, and their values, and total electrical consumption difference
print(f'Closest start time: {closest_start_time} with value: {closest_start_value}')
print(f'Closest end time: {closest_end_time} with value: {closest_end_value}')
print(f'Total electrical consumption difference from {closest_start_time} to {closest_end_time}: {consumption_difference}')
