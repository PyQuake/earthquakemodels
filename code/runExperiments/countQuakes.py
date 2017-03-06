import models.model as model

def main():
    """
    Count the number of earthquakes in the regions of: EastJapan, Kanto, Kansai, Tohoku  with mag>3.0 or mag>5.0
    """

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

if __name__ == "__main__":
    main()
