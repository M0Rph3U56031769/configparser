import configparser
# import sys
# import os
config = configparser.ConfigParser()
config.read("config.cfg")
config.sections()
config


# Ez az alap config lekérdező, kifejtve
def configSectionMap(section):
    global config
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


# Ez meg a leegyszerűsített változata
def configLekeres(szekcio2,mezo):
    Szekcio = configSectionMap(szekcio2)
    # print(Cim) #Ez kilistázza a szekció mezőit és értékeit
    # print(str(mezo[szekcio]))
    if Szekcio[mezo] == 'True':
        return True
    elif Szekcio[mezo] == 'False':
        return False
    elif Szekcio[mezo] == 'None':
        return None
    else:
        return Szekcio[mezo]


def configModosito(szekcio3, mezo1, ujErtek):
    # lets create that config file for next time...
    global config
    cfgfile = open("pyconfig.cfg", 'w')
    if ujErtek is not None:
        config.set(szekcio3, mezo1, ujErtek)
        config.write(cfgfile)
        cfgfile.close()


# ==================== Na innentől csak teszt funkciók vannak ====================
def boolTesztelo():
    oprendszer = configLekeres('alap', 'oprendszer')
    print("Oprendszer tipusa:", type(oprendszer))
    if not oprendszer:
        print("Natív False")
        print(type(oprendszer))
    elif oprendszer:
        oprendszer = bool(oprendszer)
        print("Natív True")
        print(type(oprendszer))
    else:
        print("Oprendszer:"+str(oprendszer)+"<")


def tesztIrasOlvasas():
    boolTesztelo()
    configModosito("alap", "oprendszer", 'True')
    boolTesztelo()
    configModosito("alap", "oprendszer", 'False')
    boolTesztelo()

# tesztIrasOlvasas()
