import pandas as pd
df = pd.read_excel('responses.xlsx')

df = df[['SID','Name','Email Address', 'Department Elective Courses (DECs)','Open Electives']]

from util_email import send_email
from util_word import df_to_word

for i,row in df.iterrows():
    student_id = str(row['SID'])
    student_name = row['Name']

    open_ele_id, _, open_ele = row['Open Electives'].partition(' ')

    decs = sorted([dec.strip() for dec in row['Department Elective Courses (DECs)'].split(',')])
    dec1_id, _, dec1 = decs[0].partition(' ')
    dec2_id, _, dec2 = decs[1].partition(' ')

    file_name =  df_to_word(student_id, student_name, open_ele_id, open_ele, dec1_id, dec1, dec2_id, dec2)
    receiver_email = row['Email Address']

    send_email(receiver_email, file_name)
