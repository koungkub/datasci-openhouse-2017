import pandas as pd

csvfile = pd.read_csv('db.csv', encoding = 'utf8')

for i in range (len(csvfile)):
    if (csvfile['Mathematics'][i] >= 2):
        csvfile['Programming skill'][i] = 'P'
    elif (csvfile['English'][i] >= 3):
        csvfile['Programming skill'][i] = 'P'
    else:
        csvfile['Programming skill'][i] = 'N'

csvfile.to_csv('dataset.csv', encoding='utf-8')
