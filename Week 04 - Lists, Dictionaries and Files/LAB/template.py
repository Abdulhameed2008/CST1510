"""
RECORD CHECK  -  my version
===========================

Name  :  Abdul Hameed
Lane  :  AI
Date  :  17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value,limit):
    """ This function checks the value and limit and returns the difference and percentage between them  """
    difference = limit - value
    percent = (value/limit)*100
    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"
    return difference, percent , status

def print_report(label, value, limit, difference, percent, status):
    """Prints the full report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f" Used          :{value:>10.2f}")
    print(f" Total         :{limit:>10.2f}")
    print(f" Free          :{difference:>10.2f}")
    print(f" Percent       :{percent:>10.2f} %")
    print(f" Status        :{status:>10}")

    print("=" * 34)


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.
  
with open("records2.txt","w") as f:
    f.write("R-001,87,100\n")
    f.write("R-002,120,100\n")
    f.write("R-003,45,100\n")

def load_records(path):
    """Loads data from file and converts it into list of dicts and if file not present then gives a clear line instead of an error"""
    try:
        records=[]
        with open(path) as f:
            for line in f:
                line=line.strip()
                label,value,limit=line.split(",") 
                records.append({"label":label,"value":float(value),"limit":float(limit)})
    except FileNotFoundError:
        print(f"{path} Not Found")
        return []
    return records





# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
records = load_records("records2.txt")
count = 0
results = []

for r in records:
    difference, percent , status = check_record(r["value"],r["limit"])
    print_report(r["label"],r["value"],r["limit"],difference,percent,status)
    results.append((r["label"],status))
    if status == "OVER LIMIT":
        count += 1

with open("results.txt","w") as f:
    for label, status in results:
        f.write(f"{label}: {status}\n")

print()
print(f"Over Limit count: {count}")
print()


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
