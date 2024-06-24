# Generated documentation for module arcpy.conversion


class WFSToFeatureClass(object):
    """
    Imports a feature type from a Web Feature Service (WFS) to a feature class in a geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        WFSToFeatureClass_conversion(input_WFS_server, WFS_feature_type, out_path, out_name, {is_complex}, {max_features}, {expose_metadata}, {swap_xy}, {page_size})

        Imports a feature type from a Web Feature Service (WFS) to a feature
        class in a geodatabase.

     INPUTS:
      input_WFS_server (String):
          The URL of the source WFS service (for example, http://sampleserver6.a
          rcgisonline.com/arcgis/services/SampleWorldCities/MapServer/WFSServer?
          ). If the input is a complex WFS service (is_complex = "COMPLEX"),
          this can also be the path to the .xml file.
      WFS_feature_type (String):
          The name of the WFS layer to extract from the input WFS service.
      out_path (Workspace / Feature Dataset / Folder):
          The location of the output feature class or geodatabase.If the input
          is a simple WFS, the output location can be a geodatabase
          or a feature dataset in a geodatabase. If the output location is a
          feature dataset, the coordinates will be converted from the source
          coordinate system to the coordinate system of the feature dataset.If
          the input is a complex WFS service, the output location must be a
          folder.
      out_name (String):
          The name of the output feature class or geodatabase.If the input is a
          simple WFS service, the name will be used to create
          a feature class in the output location. If the feature class name
          already exists in the geodatabase, the name will be automatically
          incremented. By default, the feature type name is used.If the input is
          a complex WFS service, the name will be used to create
          a geodatabase in the output location.
      is_complex {Boolean}:
          Specifies whether the input_WFS_server parameter value is a complex
          WFS service.COMPLEX-The WFS service is a complex WFS
          service.NOT_COMPLEX-The WFS
          service is not a complex WFS service. This is the
          default.
      max_features {Long}:
          The maximum number of features that can be returned. The default is
          1000.
      expose_metadata {Boolean}:
          Specifies whether metadata tables will be created from the service.
          This is only applicable for complex WFS
          services.EXPOSE_METADATA-Metadata tables will be created in the output
          geodatabase.DO_NOT_EXPOSE-Metadata tables will not be created in the
          output
          geodatabase. This is the default.
      swap_xy {Boolean}:
          Specifies whether the x,y axis order of the output feature class will
          be swapped. Some WFS services may have the order of the x,y
          coordinates swapped on the server side, causing the feature class to
          display incorrectly.SWAP_XY-The x,y axis order will be
          swapped.DO_NOT_SWAP_XY-The x,y axis
          order will not be swapped. This is the
          default.
      page_size {Long}:
          The page size that will be used when downloading features from the WFS
          service. The default is 100.Some servers limit the number of features
          that can be requested at a
          time or server performance may be slow when requesting a large number
          of features in a single request. Use this parameter to request a
          smaller number of features in multiple pages to avoid server timeouts
          or maximum feature limits.This parameter is only applicable for simple
          WFS 2.0 services that
          support startIndex and count WFS parameters. It will be ignored for
          older versions of WFS (1.1.0, 1.0.0).

        """