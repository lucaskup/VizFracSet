myline = qgis.utils.iface.activeLayer()
myline.selectByExpression("\"id\">0")

d = QgsDistanceArea()


d = QgsDistanceArea()
d.setEllipsoid('WGS84')

for elem in myline.selectedFeatures():
    id = elem.id()
    xy = elem.geometry().asMultiPolyline()
    #calculates the azimuth
    az = xy[0][0].azimuth(xy[0][-1])
    #normalize the angle 0 - 180
    if (az < 0):
        az = 180 + az
        
    #length = xy[0][0].sqrDist(xy[0][-1])
    measure = d.measureLine(xy[0])
    
    print(id,  az,measure)