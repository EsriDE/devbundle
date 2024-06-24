# ArcGIS Developer Bundle
## We deliver the bundle. You shape the digital era.

The ArcGIS Developer Bundle is the perfect combination of innovation and digital sovereignty.

It provides you with advanced, innovative tools for development of customized solutions using ArcGIS Enterprise, while also allowing you to maintain control over your digital sovereignity. Experience the perfect blend of technology and control with the ArcGIS Developer Bundle.

As digital transformation accelerates, technology cycles are becoming increasingly shorter. We understand that you, as a developer, need straightforward access to ArcGIS Enterprise for development and testing within secure sandbox environments.

## The developers guide to the ArcGIS Developer Bundle
List all the included software products.

```python
from devbundle.content import DevBundle

bundle = DevBundle()
bundle.software_names
```
```
['ArcGIS Enterprise', 'ArcGIS Notebook Server', 'ArcGIS Knowledge', 'ArcGIS GeoEvent Server', 'ArcGIS GeoAnalytics Server', 'ArcGIS Image Server']
```

Show the detailed description of the Buffer analysis tool.

```python
from devbundle.arcpy.analysis import Buffer

buffer_tool = Buffer()
print(buffer_tool.description)
```
```
        Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field, {line_side}, {line_end_type}, {dissolve_option}, {dissolve_field;dissolve_field...}, {method})

        Creates buffer polygons around input features to a specified distance.

     INPUTS:
      in_features (Feature Layer):
          The input point, line, or polygon features that will be buffered.
      buffer_distance_or_field (Linear Unit / Field):
          The distance around the input features that will be buffered.
          Distances can be provided as either a value representing a linear
          distance or a field from the input features that contains the distance
          to buffer each feature.If linear units are not specified or are
          entered as Unknown, the
          linear unit of the input features' spatial reference will be used.When
          specifying a distance, if the linear unit has two words, such as
          Decimal Degrees, combine the two words into one (for example, 20
          DecimalDegrees).
      line_side {String}:
          Specifies the sides of the input features that will be buffered. This
          parameter is only supported for polygon and line features.FULL-For
          lines, buffers will be generated on both sides of the line.
          For polygons, buffers will be generated around the polygon and will
          contain and overlap the area of the input features. This is the
          default.LEFT-For lines, buffers will be generated on the topological
          left of
          the line. This option is not supported for polygon input
          features.RIGHT-For lines, buffers will be generated on the topological
          right of
          the line. This option is not supported for polygon input
          features.OUTSIDE_ONLY-For polygons, buffers will be generated outside
          the input
          polygon only (the area inside the input polygon will be erased from
          the output buffer). This option is not supported for line input
          features.This optional parameter is not available with a Desktop Basic
          or
          Desktop Standard license.
      line_end_type {String}:
          Specifies the shape of the buffer at the end of line input features.
          This parameter is not valid for polygon input features.ROUND-The ends
          of the buffer will be round, in the shape of a half
          circle. This is the default.FLAT-The ends of the buffer will be flat
          or squared and will end at
          the endpoint of the input line feature.This optional parameter is not
          available with a Desktop Basic or
          Desktop Standard license.
      dissolve_option {String}:
          Specifies the type of dissolve that will be performed to remove buffer
          overlap.NONE-An individual buffer for each feature will be maintained,
          regardless of overlap. This is the default.ALL-All buffers will be
          dissolved together into a single feature,
          removing any overlap.LIST-Any buffers sharing attribute values in the
          listed fields
          (carried over from the input features) will be dissolved.
      dissolve_field {Field}:
          The list of fields from the input features on which the output buffers
          will be dissolved. Any buffers sharing attribute values in the listed
          fields (carried over from the input features) will be dissolved.
      method {String}:
          Specifies whether the planar or geodesic method will be used to create
          the buffers. PLANAR-If the input features are in a projected
          coordinate
          system, Euclidean buffers will be created. If the input features are
          in a geographic coordinate system and the buffer distance is in linear
          units (meters, feet, and so forth, as opposed to angular units such as
          degrees), geodesic buffers will be created. This is the default.
          You can use the Output Coordinate System environment setting to
          specify the coordinate system to use. For example, if the input
          features are in a projected coordinate system, you can set the
          environment to a geographic coordinate system to create geodesic
          buffers.GEODESIC-All buffers will be created using a shape-preserving
          geodesic
          buffer method, regardless of the input coordinate system.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class containing the output buffers.
```


## [ArcGIS Enterprise](https://enterprise.arcgis.com/en/)
Deliver industry-leading mapping and analytics to your infrastructure and the cloud.

### The base deployment of ArcGIS Enterprise

![ArcGIS Enterprise Base Deployment](https://enterprise.arcgis.com/en/get-started/latest/windows/GUID-9C69258B-DBAE-47B2-8AFE-816D93B8F276-web.png)

### Federated three-machine ArcGIS GIS Server Site
![Federated ArcGIS Server](https://enterprise.arcgis.com/en/get-started/latest/windows/GUID-C37D7AD9-645E-494C-9B6C-C4730658C407-web.png)

## [ArcGIS Notebook Server](https://enterprise.arcgis.com/en/notebook/)
The power of data science in your enterprise GIS.

### Single ArcGIS Notebook Server Site
![Single ArcGIS Notebook Server](https://enterprise.arcgis.com/en/get-started/latest/windows/GUID-12FF23A3-4A74-4942-81E3-DA3E7C79DC6D-web.png)

### Federated three-machine ArcGIS Notebook Server Site
![Federated ArcGIS Notebook Server](https://enterprise.arcgis.com/en/get-started/latest/windows/GUID-CEB981E7-B843-4176-86EB-1DD442F0E893-web.png)

## [ArcGIS Knowledge](https://enterprise.arcgis.com/en/knowledge/)
Where knowledge graphs and link analysis meet GIS.

### Single ArcGIS Knowledge Server Site
![Single ArcGIS Knowledge Server Site](https://enterprise.arcgis.com/en/get-started/latest/windows/GUID-5A838027-808A-4FC6-9E2E-7462E763F4E6-web.png)

### Federated two-machine ArcGIS Knowledge Server Site
![Federated ArcGIS Knowledge Server Site](https://enterprise.arcgis.com/en/get-started/latest/windows/GUID-C3AD9826-2C77-4E45-9AF0-473D5A21735B-web.png)

## [ArcGIS GeoEvent Server](https://enterprise.arcgis.com/en/geoevent/)
Real-time visualization and analytics in your frontline GIS apps.

### Single GeoEvent Server Site
![Single GeoEvent Server Site](https://enterprise.arcgis.com/en/get-started/latest/windows/GUID-F68C8F46-FBF3-483E-93B5-0CD9914296E6-web.png)

## [ArcGIS GeoAnalytics Server](https://enterprise.arcgis.com/en/geoanalytics/)
Bring advanced big data analytics to your organization.

### Single ArcGIS GeoAnalytics Server Site
![Single ArcGIS GeoAnalytics Server Site](https://enterprise.arcgis.com/en/get-started/latest/windows/GUID-B66440E4-3611-4C1C-850A-F00CE20DD66C-web.png)

### Federated three-machine ArcGIS GeoAnalytics Server Site
![Federated ArcGIS GeoAnalytics Server Site](https://enterprise.arcgis.com/en/get-started/latest/windows/GUID-73AA84CD-4B2B-466C-895E-67090125DED2-web.png)

## [ArcGIS Image Server](https://enterprise.arcgis.com/en/image/)
Share large volumes of imagery and power raster analytics.

### Single ArcGIS Image Server Site
![Single ArcGIS Image Server Site](https://enterprise.arcgis.com/en/get-started/latest/windows/GUID-6BF9D591-5E03-40DC-95F1-907E1D959224-web.png)

### Federated three-machine ArcGIS Image Server Site
![Federated ArcGIS Image Server Site](https://enterprise.arcgis.com/en/get-started/latest/windows/GUID-E17E754F-910E-4580-8FF4-3495E031CBD3-web.png)