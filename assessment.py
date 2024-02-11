import pandas as pd
from pathlib import Path

# data_dir = Path('green_taxi')
# full_df = pd.concat(pd.read_parquet(parquet_file) for parquet_file in data_dir.glob('*.parquet'))
# full_df.to_csv('output.csv', index=False)

# Get the shape (number of rows and columns)
full_df = pd.read_csv("output.csv")
print(full_df.shape)

print(full_df[full_df['fare_amount'] == 0].shape)