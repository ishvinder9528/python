#BLL start
class Customer:
    listCus=[]
    def init(self):
        self.Id=0
        self.Name=""
        self.Address=""
        self.Mobile=""
    def addcustomer(self):
        Customer.listCus.append(self)
    def searchcustomer(self,Id):
        for e in Customer.listCus:
            if(e.Id==Id):
                self.Id=e.Id
                self.Name=e.Name
                self.Address=e.Address
                self.Mobile=e.Mobile
                return
        print("Id not found")
    def deleteCustomer(self,Id):
        for e in Customer.listCus:
            if(e.Id==Id):
                Customer.listCus.remove(e)
                return
        print("Id not found")
    def modifyCustomer(self,Id):
        for e in Customer.listCus:
            if(e.Id==Id):
                e.Id=Id
                e.Name=self.Name
                e.Address=self.Address
                e.Mobile=self.Mobile
                return
        print("Id not found")
    def showallCustomer():
        for e in Customer.listCus:
            print(e)
#BLL end
#PL start
while(True):
    print("1.Add customer\n2.Search customer\n3.Delete customer\n4.Modify customer\n5.Show all customer\n0.Exit")
    ch=input("Enter your choice")
    if(ch=='1'):
        print("Add customer is selected.")
        cus=Customer()
        cus.Id=int(input("Enter Id"))
        cus.Name=str(input("Enter Name"))
        cus.Address=str(input("Enter Address"))
        cus.Mobile=str(input("Enter Mobile"))
        cus.addcustomer()
        print("Customer added successfully")
    elif(ch=='2'):
        print("Search customer is selected")
        Id=int(input("enter Id"))
        Cus=Customer()
        Cus.searchcustomer(Id)
        print("Id:",Cus.Id,"Name:",Cus.Name,"Address:",Cus.Address,"Mobile:",Cus.Mobile)
    elif(ch=='3'):
        print("Delete customer is selected")
        Id=int(input("Enter Id"))
        Cus=Customer()
        Cus.deleteCustomer(Id)
        print("Customer deleted successfully")
    elif(ch=='4'):
        print("Modify customer is selected")
        Cus=Customer()
        Id=int(input("Enter Id"))
        Cus.Name=input("Enter Name")
        Cus.Address=input("Enter addresss")
        Cus.Mobile=input("Enter mobile")
        Cus.modifyCustomer(Id)
        print("Customer modified successfully")
    elif(ch=='5'):
        print("Showall Customer is selected")
        Customer.showallCustomer()
        pass
    else:
        break

#PL end