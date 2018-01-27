from utils import start_sw, open_doc

swApp = start_sw(sw_version='2014', visible=1)
swDoc = open_doc(swApp, 'E:\\Files\\KPI\\macro\\Деталь2.SLDPRT')

myFeat = swDoc.FirstFeature
while myFeat:
    print(myFeat.GetTypeName2)
    myFeat = myFeat.GetNextFeature
