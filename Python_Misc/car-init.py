class car:
    def __init__(self, brand, series='', license_plate='', name=''):
        self.brand = brand
        self.series = series
        self.license_plate = license_plate
        self.name = name

    #def getBrand(self):
        #return self.brand
    
    #def getSeries(self):
        #return self.series
    
    #def getLicensePlate(self):
        #return self.license_plate

    def __str__(self):
        return ('This car is a ' + self.brand + ' ' + self.series + ', \
and its license plate number is: ' + self.license_plate)

    def setName(self, name):
        self.name = name

import sys
import dill

def ask():
    consent = str(input("Do you want to record your car information?(y/n)... "))
    if consent.lower() == 'y':
        b = str(input("Enter the brand of your car: "))
        s = str(input("Enter the series of your car: "))
        lp = str(input("Enter your license plate: "))
        carName = str(input("Name your car: "))
        car1 = car(b, s, lp, carName)

        moduleName = __name__
        currModule = sys.modules[moduleName]
        setattr(currModule, carName, car1)
        save = str(input("Do you want to save?(y/n)... "))
        if save == 'y':
            x = getattr(currModule, carName)
            save_object(x, 'car_data.pkl')
            
            print("Your car is saved successfully in the system.")

def save_object(obj, filename):
    from os.path import exists as file_exists
    filename = str(filename)
    if file_exists(filename):
        with open(filename, 'ab') as outp:  # Append to existing file.
            dill.dump(obj, outp)
    else:
        with open(filename, 'wb') as outp:  # (Over)writes new file.
            dill.dump(obj, outp)

def open_saved_objects(obj, filename):
    saved_objects = []
    found = False
    with open(str(filename), 'rb') as inp:
        while True:
            try:
                saved_objects.append(dill.load(inp))
            except EOFError:
                break
        for r in saved_objects:
            if r.name == str(obj):
                print(r)
                found = True
        if found == False:
            print("cannot find object...")
    
ask()

