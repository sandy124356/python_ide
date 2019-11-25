import pickle
class employee:
    def __init__(self,eno,ename,esal, eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print(self.eno,"\t",self.ename)

e = employee(10,'san',100000,'kon')

with open("empd.dat","wb") as f:

    pickle.dump(e,f)
    print("pickling completed")

with open("empd.dat","rb") as f2:
    emp=pickle.load(f2)
    emp.display()

