class Shelf:
    def __init__(self,name,auth,ils,dop,price,dopy):
        self.bkname= name
        self.bkauth=auth
        self.bkils=ils
        self.bkdop=dop
        self.bkprice = price
        self.bkdopy=dopy
        
    def bkadd(self):
        print("Name: "+str(self.bkname))
        print("Author: "+str(self.bkauth))
        print("Illustrator: "+str(self.bkils))
        print("Published: "+str(self.bkdop))
        
    def snpb(self):
        self.bksnpb = 2021 - int(self.bkdopy)
        print("This book was published " + str(self.bksnpb) + " years ago")
        print("Book Added")
        

bk1 = Shelf("Five On a Tresure Island","Enid Blyton","Eileen A. Soper","11.9.1942", "165/-", 1942)
bk1.bkadd()
bk1.snpb()

bk2 = Shelf("The Count of Monte Cristo(original: Le comte de Monte-Cristo)","Alexandre Dumas, pere","none","1844", "338/-", 1844)
bk2.bkadd()
bk2.snpb()