import pandas as pd
import sqlite3


def extract_data():
    dataframe = pd.read_csv('testdata.txt', sep="|", usecols=['Customer_Name', 'Customer_Id', 'Open_Date',
                                                              'Last_Consulted_Date', 'Dr_Name', 'State',
                                                              'Country', 'DOB', 'Is_Active'])
    dataframe = dataframe.drop_duplicates()
    return dataframe


def transform_data(d, country):
    df = pd.DataFrame(d[d['Country'] == country])
    df['DOB'] = pd.to_datetime(df['DOB'].astype(str), format='%m%d%Y')
    df['Open_Date'] = pd.to_datetime(df['Open_Date'].astype(str), format='%Y%m%d')
    df['Last_Consulted_Date'] = pd.to_datetime(df['Last_Consulted_Date'].astype(str), format='%Y%m%d')
    df = df.rename(
        columns={'Customer_Name': 'Customer_Name', 'Customer_Id': 'Customer_ID', 'Open_Date': 'Customer_Open_Date',
                 'Last_Consulted_Date': 'Last_Consulted_Date', 'Dr_Name': 'Doctor_Consulted', 'DOB': 'Date_of_Birth',
                 'Is_Active': 'Active_Customer'})
    return df


def load_data(df, tbl_name):
    con = sqlite3.connect(database='test.db')
    df.to_sql(tbl_name, con, if_exists='append', index=False)


def main():
    print('Extracting data from File')
    df = extract_data()
    print('completed! Data successfully extracted from File')
    print('Transforming data from File for Table_India')
    idf = transform_data(df, 'IND')
    print('Data successfully transformed for Table_India')
    print('Intialising Sqlite connection')
    load_data(idf, 'Table_India')
    udf = transform_data(df, 'USA')
    print('Successfully loaded Table_India')
    print('Data successfully transformed for Table_USA')

    load_data(udf, 'Table_USA')
    pdf = transform_data(df, 'PHIL')
    print('Successfully loaded Table_USA')
    print('Data successfully transformed for Table_PHIL')

    load_data(pdf, 'Table_PHIL')
    ndf = transform_data(df, 'NYC')
    print('Successfully loaded Table_PHIL')
    print('Data successfully transformed for Table_NYC')

    load_data(ndf, 'Table_NYC')
    adf = transform_data(df, 'AU')
    print('Successfully loaded Table_NYC')
    print('Data successfully transformed for Table_AU')

    load_data(adf, 'Table_AU')
    print('Successfully loaded Table_AU')


if __name__ == "__main__":

    main()
