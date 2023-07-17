import yagmail
import os
import datetime
import Info
import pandas as pd
import numpy as np

date = datetime.date.today().strftime("%B %d, %Y")
# path = 'Attendance'
# os.chdir(path)
# files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
df = pd.read_csv('../StudentDetails/student.csv')   
        
receivers = df["Email"]
# newest = files[-1]
filename = newest
sub = "Attendance Marked for " + str(date)
body = " You have Been Marked Present  "

for receiver in receivers:
    # mail information
    if pd.isnull(receiver):
        continue
    else:
        print(Info.EMAIL_ID)
        yag = yagmail.SMTP(Info.EMAIL_ID, Info.PASSWORD)
        
        # sent the mail
        yag.send(
            to=receiver,
            subject=sub, # email subject
            contents=body,  # email body
            # attachments= filename  # file attached
        )
        print("Email Sent to "+receiver)
