import models.modelEtasGa as etasGa
import datetime
import models.mathUtil as mathUtil

def modelToZecharTests(model, filename, startDate, endDate):
    """
    Conversion between the model used by this framework to the template needed by zechar files.

    """

    startDate=startDate+"T"+str(00).zfill(2)+":"+str(00).zfill(2)+":"+str(00).zfill(2)+"Z"
    endDate=endDate+"T"+str(00).zfill(2)+":"+str(00).zfill(2)+":"+str(00).zfill(2)+"Z"

    with open(filename, 'w') as f:
        f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
        f.write("<CSEPForecast xmlns='http://www.scec.org/xml-ns/csep/forecast/0.05'>\n")
        f.write("  <forecastData publicID='smi:org.scec/csep/forecast/1'>\n")
        f.write("    <modelName>gaModel-UnB_Tsukuba</modelName>\n")
        f.write("    <version>1.0</version>\n")
        f.write("    <author>PyQuake-https://github.com/PyQuake/earthquakemodels</author>\n")

        now = datetime.datetime.now()
        f.write("    <issueDate>"+str(now.year)+"-"+str(now.month).zfill(2)+"-"+str(now.day).zfill(2)+
            "T"+str(now.hour).zfill(2)+":"+str(now.minute).zfill(2)+":"+str(00).zfill(2)+"Z</issueDate>\n")
        f.write("    <forecastStartDate>"+startDate+"</forecastStartDate>\n")
        f.write("    <forecastEndDate>"+endDate+"</forecastEndDate>\n")
        f.write("    <defaultCellDimension latRange='"+str(model.definitions[0]['step'])+
                                        "' lonRange='"+str(model.definitions[1]['step'])+"'/>\n")
        f.write("    <defaultMagBinDimension>"+str(model.definitions[2]['step'])+"</defaultMagBinDimension>\n")
        f.write("    <lastMagBinOpen>1</lastMagBinOpen>\n")
        f.write("    <depthLayer max='100.0' min='0.0'>\n")

        latSteps,longSteps, magSteps=0,0,0

        binsNormalized = mathUtil.normalize(model.bins)
        for bins in binsNormalized:
            f.write("      <cell lat='"+str(round(model.definitions[0]['min']+latSteps*model.definitions[0]['step'],2))+
                                "' lon='"+str(round(model.definitions[1]['min']+longSteps*model.definitions[1]['step'],2))+"'>\n")
            f.write("        <bin m='"+str(round(model.definitions[2]['min']+magSteps*model.definitions[2]['step'],2))+
                                                    "'>"+str(bins)+"</bin>\n")
            # for num in bins:
            #     f.write("        <bin m='"+str(round(model.definitions[2]['min']+magSteps*model.definitions[2]['step'],2))+
            #                                         "'>"+str(num)+"</bin>\n")
            #     magSteps+=1

            f.write("      </cell>\n")

            latSteps+=1
            magSteps=0
            if latSteps==model.definitions[0]['bins']:
                latSteps=0
                longSteps+=1

        f.write("    </depthLayer>\n")
        f.write("  </forecastData>\n")
        f.write("</CSEPForecast>\n")

    f.close()