import csv

def pbCompanies(fileName):
    l=[]
    with open(fileName, 'r') as file:
        csvReader=csv.DictReader(file)
        for row in csvReader:
            l.append(row["entity-hover"])
    return l


def ACompanies():
    l=[]
    with open("MITHEALTHCARESTARTUPS.csv", 'r', encoding='utf-8') as file:
        csvReader=csv.DictReader(file)
        for row in csvReader:
            l.append(row["Company Name"])
    return l

def compare(fileName):
    l=[]
    count=0
    original=ACompanies()
    pitchbook=pbCompanies(fileName)
    for i in original:
        if i in pitchbook:
            row = original.index(i)+2
            l.append(i)
            count+=1
            print(f"{i} is in both lists, it is at row {row} ")
    
    print(f"there are {count} companies in both files")
    return l
