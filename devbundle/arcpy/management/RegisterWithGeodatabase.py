# Generated documentation for module arcpy.management


class RegisterWithGeodatabase(object):
    """
    Registers feature classes, tables, views, and raster layers with the geodatabase. Registering is used for data created in the database with third-party tools using SQL or in ArcGIS Pro with tools that do not register with the geodatabase (Create Unregistered Feature Class, Create Unregistered Table, and Create Database View tools).
    """

    @property
    def description(self) -> str:
        return """

        RegisterWithGeodatabase_management(in_dataset, {in_object_id_field}, {in_shape_field}, {in_geometry_type}, {in_spatial_reference}, {in_extent})

        Registers feature classes, tables, views, and raster layers with the
        geodatabase. Registering is used for data created in the database with
        third-party tools using SQL or in ArcGIS Pro with tools that do not
        register with the geodatabase (Create Unregistered Feature Class,
        Create Unregistered Table, and Create Database View tools).

     INPUTS:
      in_dataset (Table View / Raster Layer):
          The feature class, table, view, or raster created using third-party
          tools or SQL, or the view created using the Create Database View tool
          that will be registered with the geodatabase. The dataset must exist
          in the same database as the geodatabase.
      in_object_id_field {Field}:
          The field that will be used as thefield. When using an
          existing field from the input datasets, an integer data type is
          required. If an existing field is not used, anfield will be created
          and populated. ObjectIDObjectIDWhen registering a view, an
          existing integer field is required.
      in_shape_field {Field}:
          The field that identifies the shape of the features. If the input
          dataset contains a spatial data type column, include this field during
          the registration process.
      in_geometry_type {String}:
          Specifies the geometry type. If the in_shape_field parameter value is
          provided, you must specify a geometry type. If the dataset being
          registered contains existing features, the geometry type specified
          must match the entity type of these features.POINT-The geometry type
          will be point.MULTIPOINT-The geometry type
          will be multipoint.POLYGON-The geometry type will be
          polygon.POLYLINE-The geometry type will be polyline.MULTIPATCH-The
          geometry type will be multipatch.
      in_spatial_reference {Spatial Reference}:
          If the in_shape_field parameter value is provided and the table is
          empty, specify the coordinate system to be used for features. If the
          dataset being registered contains existing features, the coordinate
          system specified must match the coordinate system of the existing
          features. Valid values are a Spatial Reference object, a file with a
          .prj extension, or a string representation of a coordinate system.
      in_extent {Envelope}:
          If the in_shape_field parameter value is provided, specify the
          allowable coordinate range for x,y coordinates in the following order:
          "XMin YMin XMax YMax". If the dataset being registered contains
          existing features, the extent of the existing features will be used.

        """