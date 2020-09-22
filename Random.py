class vulnerability:
    def __init__(self,vulnID,category):
        self.vulnID = vulnID
        self.category = category

FIPS = vulnerability('v23243','II')

print(FIPS.category)
print(FIPS.vulnID)
