from sqlalchemy import create_engine
import pandas as pd 
import os


gators = pd.read_csv('data/fatal_alligator_attacks_US.csv')
gators.to_sql('fatal_alligator_attacks_US', con=engine, if_exists= 'replace')