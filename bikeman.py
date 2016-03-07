class Bicycle(object):
    def __init__(self, theModelName, theWeight, theCostToProduce):
        self.modelName = theModelName
        self.Weight = theWeight
        self.CostToProduce = theCostToProduce
        

class BikeShop(object):
    def __init__(self, theShopName):
        self.shopName = theShopName
        self.bikeInventory = []
        self.margin = .1
        self.profit = 0

    def sellBike(self, theBike):
        self.profit += theBike.CostToProduce * self.margin
        self.bikeInventory.remove(theBike)
