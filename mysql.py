from sqlalchemy import create_engine
import pandas as pd 
import os


MYSQL_HOSTNAME = os.getenv("MYSQL_HOSTNAME")
MYSQL_USERNAME = os.getenv('MYSQL_USERNAME')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')



gators = pd.read_csv('data/fatal_alligator_attacks_US.csv')
gators.to_sql('fatal_alligator_attacks_US', con=engine, if_exists= 'replace')
