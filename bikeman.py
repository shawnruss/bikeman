class Bicycle(object):
    def __init__(self, theModelName, theWeight, theCostToProduce):
        self.modelName = theModelName
        self.Weight = theWeight
        self.CostToProduce = theCostToProduce
        
class BikeShop(object):
    def __init__(self, theShopName):
        self.shopName = theShopName
        self.bikeInventory = []
        self.margin = .2
        self.profit = 0

    def getBikePrice(self, theBike):
         bikePrice = (theBike.CostToProduce * self.margin) + theBike.CostToProduce
         return bikePrice

    def sellBike(self, theBike):
        self.profit += theBike.CostToProduce * self.margin
        self.bikeInventory.remove(theBike)
        
    def buyBike(self, theBike):
        self.bikeInventory.append(theBike)
        # need to increment the inventory of the model bought
        
class Customer(object):
    def __init__(self, theCustomerName, theFund):
        self.customerName = theCustomerName
        self.fund = theFund
        self.bikeCollection = []
    
    def buyBike(self, theBike, thePurchasePrice):
        self.fund -= thePurchasePrice
        self.bikeCollection.append(theBike)
        
        
theBikeShop = BikeShop("Easy Bikes")

theBikeShop.buyBike(Bicycle("Rockhopper", 20, 100))
theBikeShop.buyBike(Bicycle("Rockhopper", 20, 100))
theBikeShop.buyBike(Bicycle("Speed Demon", 8, 300))
theBikeShop.buyBike(Bicycle("Folding Mini", 10, 200))
theBikeShop.buyBike(Bicycle("Chopper", 15, 150))
theBikeShop.buyBike(Bicycle("Kiddy Widdy", 9, 180))
theBikeShop.buyBike(Bicycle("Penny Farthing", 30, 600))

customerList = []
customerList.append(Customer("Shawn", 200))
customerList.append(Customer("Bob", 500))
customerList.append(Customer("Billy", 1000))

for customer in customerList:
    print()
    print(customer.customerName)
    for bike in theBikeShop.bikeInventory:
        if theBikeShop.getBikePrice(bike) <= customer.fund:
            print(bike.modelName)

print()
print("Inventory of " + theBikeShop.shopName + ":") 
for bike in theBikeShop.bikeInventory:
    print(bike.modelName)
    
