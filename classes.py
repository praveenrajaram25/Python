class StudentRecordBoys():
    def __init__(self, sname, srollno, sdob, sdept,shomework):
        self.sname = sname
        self.srollno = srollno
        self.sdob = sdob
        self.sdept = sdept
        self.shomework=shomework

    def takeAttendence(self):
        if self.sname == 'Praveen':
            return "{} is Present".format(self.sname)
    def homeWorkCheck(self):
        if self.shomework =='Y':
            return "{} is completed the homework".format(self.sname)
        else:
            return "homework pending"

class StudentRecordGirls(StudentRecordBoys):
    pass


Record1 = StudentRecordBoys(sname='Praveen', srollno=2116372, sdob='25-11-2000', sdept='ADM',shomework='N')
Record2 =  StudentRecordBoys(sname='Rajan', srollno=2116373, sdob='21-11-1999', sdept='Civil',shomework='Y')
record3 = StudentRecordGirls(sname='Sai Keshavi', srollno=2116374, sdob='25-11-2000', sdept='ADM',shomework='N')
print("Report 1 : ",Record1.sname, Record1.srollno, Record1.sdob, Record1.sdept)
print(Record1.homeWorkCheck())
print("Report 2 : ",Record2.sname, Record2.srollno, Record2.sdob, Record2.sdept)
print(Record2.homeWorkCheck())
print("Report 3 : ",record3.sname,record3.srollno,record3.sdob,record3.sdept)
print(record3.homeWorkCheck())


