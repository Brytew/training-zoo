

class Zoo:
    class Zwierz:

        _id_counter = 1

        def __init__(
            self,
            gatunek:str,
            imie:str,
            iloscNog:int=4       
        ):
            self.gatunek=gatunek
            self.imie=imie
            self.iloscNog=iloscNog
            self.aio_id = self._generate_id()

        @classmethod
        def _generate_id(cls):
            current_id = cls._id_counter
            cls._id_counter += 1
            return current_id

        def zawarcz_kto(self):
            print(f'{self.gatunek} robi "WWRAAAAMIAL" i ma {self.iloscNog} nog')

        
        def __str__(self):
            return f'Gatunek: {self.gatunek}, Imię: {self.imie}, Liczba nóg: {self.iloscNog}'


        class ids:
            @staticmethod           
            def id_kl(aio_id):
                return {
                    'czylata':'tak',
                    'nazwisko': aio_id
            }

    def __init__(
        self,
        zooName:str,
        zooLocation:str = None,
        zooAnimals:list = None,
    ):
        self.zooName=zooName
        self.zooLocation=zooLocation
        self.zooAnimals=zooAnimals if zooAnimals is not None else []
        self.zooEmployee=[]
        

    def dodaj_zwierz(self,gatunek,imie):
        new_Animals=self.Zwierz(gatunek,imie)
        self.zooAnimals.append(new_Animals)

    def wyswietl_zoo(self):
        for zwierze in self.zooAnimals:
            print(zwierze)     


# Tworzenie instancji zoo
zooWroclaw = Zoo('Wro', 'WroclawCity')

# Dodawanie koguta i slonia
zooWroclaw.dodaj_zwierz('Kogut', 'Koko')
zooWroclaw.dodaj_zwierz('Słoń', 'Elephant')

# Wyświetlanie informacji o wszystkich zwierzętach
zooWroclaw.wyswietl_zoo()

# Sprawdzanie aio_id konkretnego zwierzęcia
kogut = zooWroclaw.zooAnimals[0]
print(f'AIO_ID koguta {kogut.imie}: {kogut.aio_id}')

# Opcjonalnie, korzystanie z klasy ids
print(zooWroclaw.zooAnimals[0].ids.id_kl(kogut.aio_id))

