# Generated documentation for module arcpy.management


class CreateFeatureclass(object):
    """
    Creates an empty feature class in a geodatabase or a shapefile in a folder.
    """

    @property
    def description(self) -> str:
        return """

        CreateFeatureclass_management(out_path, out_name, {geometry_type}, {template;template...}, {has_m}, {has_z}, {spatial_reference}, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3}, {out_alias}, {oid_type})

        Creates an empty feature class in a geodatabase or a shapefile in a
        folder.

     INPUTS:
      out_path (Workspace / Feature Dataset):
          The enterprise or file geodatabase or the folder in which the output
          feature class will be created. This workspace must already exist.
      out_name (String):
          The name of the feature class to be created.
      geometry_type {String}:
          Specifies the geometry type of the output feature class.POINT-The
          geometry type will be point.MULTIPOINT-The geometry type
          will be multipoint.POLYGON-The geometry type will be
          polygon.POLYLINE-The geometry type will be polyline.MULTIPATCH-The
          geometry type will be multipatch.
      template {Table View}:
          An existing dataset or a list of datasets used as templates to define
          the attribute fields of the new feature class.
      has_m {String}:
          Specifies whether the feature class will have linear measurement
          values (m-values).DISABLED-The output feature class will not have
          m-values. This is the
          default.ENABLED-The output feature class will have m-values.
          SAME_AS_TEMPLATE-The output feature class will have m-values
          if the dataset specified in theparameter (template parameter in
          Python) has m-values. Template Feature Class
      has_z {String}:
          Specifies whether the feature class will have elevation values
          (z-values).DISABLED-The output feature class will not have z-values.
          This is the
          default.ENABLED-The output feature class will have z-values.
          SAME_AS_TEMPLATE-The output feature class will have z-values
          if the dataset specified in theparameter (template parameter in
          Python) has z-values. Template Feature Class
      spatial_reference {Spatial Reference}:
          The spatial reference of the output feature dataset. You can
          specify the spatial reference in the following ways:        Enter the
          path to a .prj file, such as
          C:/workspace/watershed.prj.Reference a feature class or feature
          dataset whose spatial reference
          you want to apply, such as
          C:/workspace/myproject.gdb/landuse/grassland.Define a spatial
          reference object before using this tool, such as sr =
          arcpy.SpatialReference("Sinusoidal (Africa)"), which you then use as
          the spatial reference parameter.If a spatial reference is not
          provided, the output will have an
          undefined spatial reference. The spatial reference of thevalue
          has no effect on the output
          spatial reference. If you want the output to be in the coordinate
          system of thevalue, set theparameter to the spatial reference of
          thevalue. Template Feature ClassTemplate Feature
          ClassCoordinate SystemTemplate Feature Class
      config_keyword {String}:
          The configuration keyword applies to enterprise geodatabase data only.
          It determines the storage parameters of the database table.
      spatial_grid_1 {Double}:
          This parameter is not supported. Any value provided will be ignored.
      spatial_grid_2 {Double}:
          This parameter is not supported. Any value provided will be ignored.
      spatial_grid_3 {Double}:
          This parameter is not supported. Any value provided will be ignored.
      out_alias {String}:
          The alternate name for the output feature class that will be created.
      oid_type {String}:
          Specifies whether the output Object ID field will be 32 bit or 64
          bit.SAME_AS_TEMPLATE-The output Object ID field type (32 bit or 64
          bit)
          will be the same as the Object ID field of the first template dataset.
          This is the default.64_BIT-The output Object ID field will be 64
          bit.32_BIT-The output Object ID field will be 32 bit.

        """