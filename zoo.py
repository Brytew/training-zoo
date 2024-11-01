

class Zoo:

    def __init__(
        self,
        zooName:str,
        zooLocation:str = None,
        zooAnimals:list = None,
        zooEmployee:list = None,
    ):
        self.zooName=zooName
        self.zooLocation=zooLocation
        self.zooAnimals=zooAnimals if zooAnimals is not None else []
        self.zooEmployee=zooEmployee if zooEmployee is not None else []
        


    def dodaj_zwierze(
        self,
        zwierze:str         
    ):
        if zwierze not in self.zooAnimals:
            self.zooAnimals.append(zwierze) 
        else:
            print(f'zwierzę {zwierze} już jest w zoo')


    def lista_zwierzat(self):
        for listAnimal in self.zooAnimals:
            print(listAnimal)
  

zooWroclaw = Zoo("Wro",zooAnimals=["Kogut"])
zooWroclaw.dodaj_zwierze("Pies")

zooWroclaw.lista_zwierzat()
