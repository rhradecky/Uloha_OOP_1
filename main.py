class City:
    def __init__(self, city_name, region_name, country_name, nr_citizens, zip_code, area_code ):
        self.city_name = city_name
        self.region_name = region_name
        self.country_name = country_name
        self.nr_citizens = nr_citizens
        self.zip_code = zip_code
        self.area_code = area_code


    def adresa(self):
        print(f"Mesto: {self.city_name}   region: {self.region_name}   Krajina: {self.country_name}   Pocet obyvatelov: {self.nr_citizens}   PSC: {self.zip_code}   Smerove cislo oblasti: {self.area_code}")


bratislava = City( "Bratislava", "Bratislavsky Kraj", "Slovensko", "5.4 mil", "841 01", "42842684")


print(bratislava.adresa())
