#still not working
#having many mistake 
#i will correct it tomorrow

class VendingMachine:

    finlis=[]
    def init(self):
        self.id=0
        self.name=""
        self.ingre=""
        self.choice=""
    def addItem(self):
        VendingMachine.finlis.append(self)
    def searchCoustomer(self,Id):
        if VendingMachine.finlis==None:
            print("bucket is empty")
            pass
        for e in VendingMachine.finlis:
            if(e.id==id):
                self.id=e.id
                self.name=e.name
                self.ingre=e.ingre
                self.choice=e.choice
                return
        print("Id not found")
    def choiceing(self,ch):
        if ch == 1:
            VendingMachine.finlis.append("Tea")
            print("Ur choice is added")
        elif ch ==2:
            VendingMachine.finlis.append("Coffee")
            print("Ur choice is added")
        else:
            print("enter write choice\n Error 404 \U0001f600")
            pass
    def ingreedients(self,ch,*ching):
        e=0
        totaling=""
        if ch==1:
            print("1- extar sugar \n2- extra powder \n3- less powder \n4- extra Milk \n5- **final** ")
            for e in ching:
                if ching == 1:
                    totaling=totaling+"extra sugar\t"
                elif ching == 2:
                    totaling=totaling+"extra powder\t"
                elif ching == 3:
                    totaling=totaling+"less powder\t"
                elif ching == 4:
                    totaling=totaling+"extra milk\t"
                elif ching == 5:
                    pass
                else:
                    print("enter write choice\n Error 404 \U0001f600")
            VendingMachine.finlis.ingre.append(totaling)
        elif ch == 2:
            print("1- extar sugar \n2- extra Adrak  \n4- extra Milk \n5- **final** ")
            for e in ching:
                if ching == 1:
                    totaling=totaling+"extra sugar\t"
                elif ching == 2:
                    totaling=totaling+"extra Adrak\t"
                elif ching == 3:
                    totaling=totaling+"extra milk\t"
                elif ching == 4:
                    pass
                else:
                    print("enter write choice\n Error 404 \U0001f600")
            VendingMachine.finlis.ingre.append(totaling)
        else:
            pass
    @staticmethod
    def showallCustomer():
        for e in VendingMachine.finlis:
            print(f"Id = {e.id} \nName = {e.name} \nchoice = {e.choice}  \ningredients = {e.ingre} /")


while(True):
    print("1.Add customer\n2.Search customer with their choice \n4.Show all customer\n0.Exit")
    ch=input("Enter your choice: ")
    if(ch=='1'):
        print("Add customer is selected.")
        cus=VendingMachine()
        cus.id=int(input("Enter Id : "))
        cus.name=str(input("Enter Name : "))
        lkll=int(input("enter \n1 for coffee \n2 for tea :\n"))
        cus.choice = VendingMachine.choiceing(lkll)
        cus.addItem()
        print("Customer info added successfully")
    elif(ch=='2'):
        print("Search customer is selected")
        Id=int(input("enter Id"))
        Cus=VendingMachine()
        Cus.searchCoustomer(Id)
        print("Id:",Cus.id,"Name:",Cus.name,"Address:",Cus.choice,"Mobile:",Cus.ingre)
    elif(ch=='3'):
        print("Showall Customer is selected")
        VendingMachine.showallCustomer()
        pass
    else:
        break

