# Generated documentation for module arcpy.management


class CreateUnRegisteredFeatureclass(object):
    """
    Creates an empty feature class in an enterprise or mobile geodatabase. The feature class is not registered with the geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        CreateUnRegisteredFeatureclass_management(out_path, out_name, {geometry_type}, {template;template...}, {has_m}, {has_z}, {spatial_reference}, {config_keyword})

        Creates an empty feature class in an enterprise or mobile geodatabase.
        The feature class is not registered with the geodatabase.

     INPUTS:
      out_path (Workspace / Feature Dataset):
          The enterprise geodatabase or mobile geodatabase in which the feature
          class will be created.
      out_name (String):
          The name of the feature class that will be created.
      geometry_type {String}:
          Specifies the geometry type of the feature class. This parameter is
          only relevant for those geometry types that store dimensionality
          metadata, such as ST_Geometry in PostgreSQL, PostGIS Geometry, and
          Oracle SDO_Geometry.POINT-The geometry type will be
          point.MULTIPOINT-The geometry type
          will be multipoint.POLYLINE-The geometry type will be
          polyline.POLYGON-The geometry type will be polygon. This is the
          default.
      template {Feature Layer}:
          An existing feature class or list of feature classes with fields and
          attribute schema that will be used to defined the fields in the output
          feature class.
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
          the spatial reference parameter.
      config_keyword {String}:
          Specifies the default storage parameters (configurations) for
          geodatabases in a relational database management system (RDBMS). This
          setting is applicable only when using enterprise geodatabase
          tables.Configuration keywords are set by the database administrator.

        """