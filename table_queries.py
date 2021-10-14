import sqlite3
con = sqlite3.connect(database=r'test.db')
cur = con.cursor()
cur.execute("""CREATE TABLE Table_India (
    Customer_Name       VARCHAR (255) NOT NULL
                                      PRIMARY KEY,
    Customer_ID         VARCHAR (18)  NOT NULL,
    Customer_Open_Date  DATE (8)      NOT NULL,
    Last_Consulted_Date DATE (8),
    Vaccination_Type    CHAR (5),
    Doctor_Consulted    CHAR (255),
    State               CHAR (5),
    Country             CHAR (5),
    Post_Code           INT (5),
    Date_of_Birth       DATE (8),
    Active_Customer     CHAR (1) 
);""")
cur.execute("""CREATE TABLE Table_USA (
    Customer_Name       VARCHAR (255) NOT NULL
                                      PRIMARY KEY,
    Customer_ID         VARCHAR (18)  NOT NULL,
    Customer_Open_Date  DATE (8)      NOT NULL,
    Last_Consulted_Date DATE (8),
    Vaccination_Type    CHAR (5),
    Doctor_Consulted    CHAR (255),
    State               CHAR (5),
    Country             CHAR (5),
    Post_Code           INT (5),
    Date_of_Birth       DATE (8),
    Active_Customer     CHAR (1) 
);""")

cur.execute("""CREATE TABLE Table_PHIL (
    Customer_Name       VARCHAR (255) NOT NULL
                                      PRIMARY KEY,
    Customer_ID         VARCHAR (18)  NOT NULL,
    Customer_Open_Date  DATE (8)      NOT NULL,
    Last_Consulted_Date DATE (8),
    Vaccination_Type    CHAR (5),
    Doctor_Consulted    CHAR (255),
    State               CHAR (5),
    Country             CHAR (5),
    Post_Code           INT (5),
    Date_of_Birth       DATE (8),
    Active_Customer     CHAR (1) 
);""")


cur.execute("""CREATE TABLE Table_NYC (
    Customer_Name       VARCHAR (255) NOT NULL
                                      PRIMARY KEY,
    Customer_ID         VARCHAR (18)  NOT NULL,
    Customer_Open_Date  DATE (8)      NOT NULL,
    Last_Consulted_Date DATE (8),
    Vaccination_Type    CHAR (5),
    Doctor_Consulted    CHAR (255),
    State               CHAR (5),
    Country             CHAR (5),
    Post_Code           INT (5),
    Date_of_Birth       DATE (8),
    Active_Customer     CHAR (1) 
);""")

cur.execute("""CREATE TABLE Table_AU (
    Customer_Name       VARCHAR (255) NOT NULL
                                      PRIMARY KEY,
    Customer_ID         VARCHAR (18)  NOT NULL,
    Customer_Open_Date  DATE (8)      NOT NULL,
    Last_Consulted_Date DATE (8),
    Vaccination_Type    CHAR (5),
    Doctor_Consulted    CHAR (255),
    State               CHAR (5),
    Country             CHAR (5),
    Post_Code           INT (5),
    Date_of_Birth       DATE (8),
    Active_Customer     CHAR (1) 
);""")

con.commit()
