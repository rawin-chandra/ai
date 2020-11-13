class Life:
    name = ""
    type = ""    
    inherit = []
    desc = ""
    has = ""
    can = ""
    
dog = Life()
dog.type = "pet"
dog.desc = "lovely and royal"
dog.name = "dog"
dog.has = "hair,nail,..."
dog.can = "run,swim,bark,bite,...."

cat = Life()
cat.type = "pet"
cat.desc = "lovely and pride"
cat.name = "cat"
cat.has = "hair,nail,blink eys,..."
cat.can = "run,meaw,bite,lick,..."

four_leg_animal = Life()
four_leg_animal.type = "4 leg animal"
four_leg_animal.desc = "animal that has 4 legs"
four_leg_animal.name = "4 leg animal"
four_leg_animal.has = "4 legs"
four_leg_animal.can = ""
four_leg_animal.inherit.append(dog)
four_leg_animal.inherit.append(cat)

animal = Life()
animal.inherit.append(four_leg_animal)

def find(key):   
    for x in animal.inherit:
        if key in x.desc:
            print("found " , x.name)
            
find("lovely")



