import pandas as pd

def extract_data():

    features_df = pd.read_csv(r"data\Features_dataset.csv")
    sales_df= pd.read_csv(r"data\sales_dataset.csv")
    stores_df= pd.read_csv(r"data\stores_dataset.csv")

    print('Features Dataset')
    print(features_df.head())
    print(features_df.dtypes)

    print('Sales Dataset')
    print(sales_df.head())
    print(sales_df.dtypes)

    print('Stores Dataset')
    print(stores_df.head())
    print(stores_df.dtypes)

    return features_df, sales_df, stores_df