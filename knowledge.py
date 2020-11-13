class MyObject:
    name = ""
    type = ""
    link_number=0
    links = []
    desc = ""
chiangmai = MyObject()
chiangmai.type = "province"
chiangmai.desc = "Tourism Land"
chiangmai.name = "Chaingmai"
north = MyObject()
north.type = "Region"
north.links.append(chiangmai)
north.desc = "Cool weather"
north.name = "North"
songkhla = MyObject()
songkhla.type = "province"
songkhla.desc = "Land of blue sea"
songkhla.name = "Songkhla"
phuket = MyObject()
phuket.type = "province"
phuket.desc = "Amazing island"
phuket.name = "Phuket"
south = MyObject()
south.type = "Region"
south.links.append(songkhla)
south.links.append(phuket)
south.desc = "Rain weather"
south.name = "South"
thai = MyObject()
thai.type="Country"
thai.links.append(north)
thai.links.append(south)
#print(thai.links[0].desc)
def find(key):
    x = len(thai.links)
    for i in range(x):
        if key in thai.links[i].desc:
            print("found " , thai.links[i].name)
find("Amazing")