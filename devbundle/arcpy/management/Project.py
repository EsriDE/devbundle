# Generated documentation for module arcpy.management


class Project(object):
    """
    Projects spatial data from one coordinate system to another.
    """

    @property
    def description(self) -> str:
        return """

        Project_management(in_dataset, out_dataset, out_coor_system, {transform_method;transform_method...}, {in_coor_system}, {preserve_shape}, {max_deviation}, {vertical})

        Projects spatial data from one coordinate system to another.

     INPUTS:
      in_dataset (Feature Layer / Feature Dataset / Scene Layer / Building Scene Layer / File):
          The feature class, feature layer, feature dataset, scene layer, scene
          layer package, or OGC Geopackage to be projected.
      out_coor_system (Coordinate System):
          Valid values are a SpatialReference object, a file with a .prj
          extension, or a string representation of a coordinate system.
      transform_method {String}:
          This method can be used to convert data between two geographic
          coordinate systems or datums. This optional parameter may be required
          if the input and output coordinate systems have different datums.To
          get a list of valid transformations, use the
          arcpy.ListTransformations method. The most appropriate transformation
          is usually the first one in the returned list. The list is sorted by
          amount of overlap of the data versus the areas of use of the
          transformations. If two or more transformations have the same amount
          of overlap with the data, the transformation accuracy values are used
          as a secondary sort parameter.Transformations are bidirectional. For
          example, if you're converting
          data from WGS84 to NAD 1927, you can choose the NAD_1927_to_WGS_1984_3
          transformation, and the tool will apply it correctly. If no
          transformation is provided, a default transformation is used. This
          default transformation is suitable for general mapping applications
          but may not be suitable for applications that require precise
          locational accuracy.
      in_coor_system {Coordinate System}:
          The coordinate system of the input feature class or dataset. When the
          input has an unknown or unspecified coordinate system, you can specify
          the data's coordinate system without having to modify the input data
          (which may not be possible if the input is in read-only format).
      preserve_shape {Boolean}:
          Specifies whether vertices will be added to the output lines or
          polygons so their projected shape is more
          accurate.NO_PRESERVE_SHAPE-Extra vertices will not be added to the
          output lines
          or polygons. This is the default.PRESERVE_SHAPE-Extra vertices will be
          added to the output lines or
          polygons as needed, so their projected shape is more accurate.
      max_deviation {Linear Unit}:
          The distance a projected line or polygon can deviate from its exact
          projected location when the preserve_shape parameter is set to
          PRESERVE_SHAPE. The default is 100 times the x,y tolerance of the
          spatial reference of the output dataset.
      vertical {Boolean}:
          Specifies whether a vertical transformation will be applied.This
          parameter is only enabled when the input and output coordinate
          systems have a vertical coordinate system and the input feature class
          coordinates have z-values. Also, many vertical transformations require
          additional data files that must be installed using the ArcGIS
          Coordinate Systems Data installation package.This parameter is not
          compatible with the preserve_shape parameter.NO_VERTICAL-A vertical
          transformation will not be applied. The
          z-values of geometry coordinates will be ignored and the z-values will
          not be modified. This is the default.VERTICAL-The transformation
          specified in the transform_method
          parameter will be applied. The x-, y-, and z-values of geometry
          coordinates will be transformed.

     OUTPUTS:
      out_dataset (Feature Class / Feature Dataset / File):
          The output dataset to which the results will be written.

        """