import win32com.client
import pythoncom


# get existing sw app instance
swYearLastDigit = 4  # sw 2014
swApp = win32com.client.DispatchEx("SldWorks.Application.%d" % (20 + (swYearLastDigit - 2)))
swApp.Visible = 1

# get active doc or create new one
if swApp.ActiveDoc:
    swDoc = swApp.ActiveDoc
else:
    swApp.NewDocument(
        TemplateName="C:\\ProgramData\\SolidWorks\\SolidWorks 2014\\templates\\gost-part.prtdot",
        PaperSize=0,
        Width=0,
        Height=0,
    )
    swApp.ActivateDoc2(
        Name="Д56",  # name
        Silent=False,  # silent mode
        Errors=Exception
    )
    swDoc = swApp.ActiveDoc

# get view "Спереди"
swDoc.Extension.SelectByID2(
    "Спереди",  # Name
    "PLANE",  # Type
    0,  # X
    0,  # Y
    0,  # Z
    False,  # Append
    0,  # Mark
    win32com.client.VARIANT(pythoncom.VT_DISPATCH, None),  # Callout
    0,  # SelectOption
)

# create new sketch on this view
swDoc.SketchManager.InsertSketch(True)

# create rectangle on created sketch
swDoc.SketchManager.CreateCornerRectangle(
    0,
    0,
    0,
    0.067899689762150967,
    -0.035683453981385727,
    0
)

swDoc.FeatureManager.FeatureExtrusion2(
    True,
    False,
    False,
    0,
    0,
    0.0115,
    0.01,
    False,
    False,
    False,
    False,
    0.017453292519943334,
    0.017453292519943334,
    False,
    False,
    False,
    False,
    True,
    True,
    True,
    0,
    0,
    False
)
