def popupTable(dataframe, row):
   # chlorophyll = '%.6f'%dataframe["Chlorophyll"][row]
   # dissolvedo2 = str('%.6f'%dataframe["DissolvedOxygen"][row])+" mg/l"
   # ph = '%.6f'%dataframe["pH"][row]
   # salinity = str('%.6f'%dataframe["Salinity"][row])+" ppt"
   # turbidity = str('%.6f'%dataframe["Turbidity"][row])+" NTU"
    centroidCoordinates = ['%.6f'%dataframe["geometry"][row].centroid.x, '%.6f'%dataframe["geometry"][row].centroid.y] 
    #print(centroidCoordinates)
    html = """<!DOCTYPE html>
    <html>
    <head>
    <h4 style="margin-bottom:5"; width="300px">{}</h4>""".format("AOI coordinates") + """
    </head>
        <table style="height: 150px; width: 300px;">
    <tbody>
    <tr>
    <td style="padding-left: 5px;width:100px;background-color: """+ "#6573c3" +""";"><span style="color: #ffffff;">Coordinates</span></td>
    <td style="width: 150px;background-color: """+ "#6573c3" +""";"><span style="color: #ffffff;">{}</td>""".format(centroidCoordinates) + """
    </tr>
    </tbody>
    </table>
    </html>
    """
    return html