"""
RECORD CHECK  -  my version
===========================

Name  :  Abdul Hameed
Lane  :  AI 
Date  :  06/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt

with open("records2.csv","w") as f:
    f.write("label,value,limit\n")
    f.write("R-001,87,100\n")
    f.write("R-002,120,100\n")
    f.write("R-003,129,100\n")
    f.write("R-004,90,100\n")
    f.write("R-005,95,100\n")


df = pd.read_csv("records2.csv")


df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(lambda x : "OVER LIMIT" if x >= 100 else "WARNING" if x >= 90 
                                   else "OK")


print(df[df["status"] != "OK"])
df_status = df.groupby("status").size()

df.to_csv("records_checked.csv", index=False)

df_status.plot(kind="bar",title="Status Counts")
plt.xlabel("Status")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("status_counts.png")




