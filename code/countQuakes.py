import models.model as model
year = 2006
for i in range(5):
    print(year + i)
    a = model.loadModelFromFile(
        "../Zona/3.0EastJapanreal" + str(year + i) + ".txt")
    print("EastJapan")
    print(sum(a.bins))
    a = model.loadModelFromFile(
        "../Zona/3.0Kantoreal" + str(year + i) + ".txt")
    print("Kanto")
    print(sum(a.bins))
    a = model.loadModelFromFile(
        "../Zona/3.0Kansaireal" + str(year + i) + ".txt")
    print("Kansai")
    print(sum(a.bins))
    a = model.loadModelFromFile(
        "../Zona/3.0Tohokureal" + str(year + i) + ".txt")
    print("Tohoku")
    print(sum(a.bins))

year = 2006
for i in range(5):
    print(year + i)
    a = model.loadModelFromFile(
        "../Zona/5.0EastJapanreal" + str(year + i) + ".txt")
    print("EastJapan")
    print(sum(a.bins))
    a = model.loadModelFromFile(
        "../Zona/5.0Kantoreal" + str(year + i) + ".txt")
    print("Kanto")
    print(sum(a.bins))
    a = model.loadModelFromFile(
        "../Zona/5.0Kansaireal" + str(year + i) + ".txt")
    print("Kansai")
    print(sum(a.bins))
    a = model.loadModelFromFile(
        "../Zona/5.0Tohokureal" + str(year + i) + ".txt")
    print("Tohoku")
    print(sum(a.bins))

    year = 2005
    while(year < 2012):
        print(year)
        a = model.loadModelFromFile(
            "../Zona/5.0EastJapanreal" + str(year) + ".txt")
        print("EastJapan")
        print(sum(a.bins))
        a = model.loadModelFromFile(
            "../Zona/5.0Kantoreal" + str(year) + ".txt")
        print("Kanto")
        print(sum(a.bins))
        a = model.loadModelFromFile(
            "../Zona/5.0Kansaireal" + str(year) + ".txt")
        print("Kansai")
        print(sum(a.bins))
        a = model.loadModelFromFile(
            "../Zona/5.0Tohokureal" + str(yearccc) + ".txt")
        print("Tohoku")
        print(sum(a.bins))
