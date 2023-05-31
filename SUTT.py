import pandas as pd

def branch_sin(br1):
    global branch1
    if br1 == 'AA':
        branch1 = 'ECE'
    elif br1 == 'AB':
        branch1 = 'Manu'
    elif br1 == 'A1':
        branch1 = 'Chemical'
    elif br1 == 'A2':
        branch1 = 'Civil'
    elif br1 == 'A3':
        branch1 = 'EEE'
    elif br1 == 'A4':
        branch1 = 'Mech'
    elif br1 == 'A5':
        branch1 = 'Pharma'
    elif br1 == 'A7':
        branch1 = 'CSE'
    elif br1 == 'A8':
        branch1 = 'ENI'
    return branch1

def branch_du(br2):
    global branch2
    if br2 == 'B1':
        branch2 = 'MSc BIO'
    elif br2 == 'B2':
        branch2 = 'MSc Chem'
    elif br2 == 'B3':
        branch2 = 'MSc Eco'
    elif br2 == 'B4':
        branch2 = 'MSc Mathematics'
    elif br2 == 'B5':
        branch2 = 'MSc Physics'
    return branch2


SHEET_ID = '1jPq_zyLptX3My07oOxUpsrkPYJUB_ryEst8KA4dvMfk'
SHEET_NAME = 'AAPL'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
df2 = df.rename(columns={'Name': 'BITS ID', 'BITS ID': 'Name'})
df3 = df2.to_dict('records')
for i in df3:
    id = i['BITS ID']
    year = id[0:4]
    eml = id[8:12]
    br = id[4:6]
    check = id[4:5]
    dual = id[6:8]
    if check == 'A':
        b = branch_sin(br)
    elif check == 'B' and dual == 'PS':
        b = branch_du(br)
    elif check == 'B' and dual != 'PS':
        b = (branch_sin(br) + ' + ' + branch_du(dual))
    i['Email'] = f'f{year}{eml}@pilani.bits-pilani.ac.in'
    i['Branch'] = b
print(df3)

