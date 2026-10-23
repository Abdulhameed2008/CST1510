# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def status(self,percent):
        return "OVER LIMIT" if percent>=100 else "OK"    # this parameter should be self
         

r = Record()
print(r.status(95))
