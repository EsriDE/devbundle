# Generated documentation for module arcpy.management


class MakeQueryLayer(object):
    """
    Creates a query layer from a DBMS table based on an input SQL select statement.
    """

    @property
    def description(self) -> str:
        return """

        MakeQueryLayer_management(input_database, out_layer_name, query, {oid_fields;oid_fields...}, {shape_type}, {srid}, {spatial_reference}, {spatial_properties}, {m_values}, {z_values}, {extent})

        Creates a query layer from a DBMS table based on an input SQL select
        statement.

     INPUTS:
      input_database (Workspace):
          The database connection file that contains the data to be queried.
      out_layer_name (String):
          The output name of the feature layer or table view to be created.
      query (String):
          The SQL statement that defines the select query to be issued to the
          database.
      oid_fields {String}:
          One or more fields from the SELECT statement SELECT list that will
          generate a dynamic, unique row identifier.
      shape_type {String}:
          Specifies the shape type of the query layer. Only those records from
          the result set of the query that match the specified shape type will
          be used in the output query layer. Tool validation will attempt to set
          this property based on the first record in the result set. This can be
          changed before running the tool if it is not the correct output shape
          type. This parameter is ignored if the result set of the query does
          not return a geometry field.POINT-The output query layer will use
          point geometry.MULTIPOINT-The
          output query layer will use multipoint geometry.POLYGON-The output
          query layer will use polygon geometry.POLYLINE-The output query layer
          will use polyline geometry.
      srid {String}:
          The spatial reference identifier (SRID) value for queries that return
          geometry. Only those records from the result set of the query that
          match the specified SRID value will be used in the output query layer.
          Tool validation will attempt to set this property based on the first
          record in the result set. This can be changed before running the tool
          if it is not the correct output SRID value. This parameter is ignored
          if the result set of the query does not return a geometry field.
      spatial_reference {Spatial Reference}:
          The coordinate system that will be used by the output query layer.
          Tool validation will attempt to set this property based on the first
          record in the result set. This can be changed before running the tool
          if it is not the correct output coordinate system. This parameter is
          ignored if the result set of the query does not return a geometry
          field.
      spatial_properties {Boolean}:
          Specifies how the spatial properties for the layer will be
          defined.During the validation process, dimensionality, geometry type,
          spatial
          reference, SRID, and unique identifier properties will be set on the
          query layer. These values are based on the first row returned in the
          query. To manually define these properties instead of the tool
          querying the table to get them, use the default value for this
          parameter.DEFINE_SPATIAL_PROPERTIES-Manually define the spatial
          properties of
          the layer. This is the default.DO_NOT_DEFINE_SPATIAL_PROPERTIES-Layer
          properties will be determined
          based on the first row returned in the query.
      m_values {Boolean}:
          Specifies whether the layer will have m-values.INCLUDE_M_VALUES-The
          layer will have
          m-values.DO_NOT_INCLUDE_M_VALUES-The layer will not have m-values.
          This is the
          default.
      z_values {Boolean}:
          Specifies whether the layer will have z-values.INCLUDE_Z_VALUES-The
          layer will have
          z-values.DO_NOT_INCLUDE_Z_VALUES-The layer will not have z-values.
          This is the
          default.
      extent {Extent}:
          The extent of the layer. This parameter is only used if
          theparameter is checked (spatial_properties =
          DEFINE_SPATIAL_PROPERTIES in Python). The extent must include all
          features in the table. Define the spatial properties of the
          layerMAXOF-The maximum extent of all inputs will be used.MINOF-The
          minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.

        """