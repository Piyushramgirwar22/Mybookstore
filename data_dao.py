import pandas as pd

# df = pd.read_csv(r'C:\Users\lenovo\OneDrive\Desktop\mybooks project\app_folder\mybooks_project_data.csv')

# print(df)

def book_range(price_range, df):
    new_df = df[df['cluster'] == price_range]
    return new_df.T.to_dict().values()

# print(book_range('low range', df))