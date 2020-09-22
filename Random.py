class vulnerability:

    num_of_vulns = 0

    def __init__(self,vulnID,category):
        self.vulnID = vulnID
        self.category = category

        self.status = "open"

        vulnerability.num_of_vulns += 1

    def changeStatus(self):
        if(self.status == "open"):
            self.status = "closed"
        else:
            self.status = "open"




v1 = vulnerability('v23243','II')
v2 = vulnerability('v23566','I')
v3 = vulnerability('v27866','I')

print(v1.status)
print(v2.__dict__)
print(v3.__dict__)
print(v3.num_of_vulns)
vulnerability.changeStatus(v3)
print(v3.__dict__)
vulnerability.changeStatus(v3)
print(v3.__dict__)
