# Generated documentation for module arcpy.geoanalytics


class CalculateField(object):
    """
    Creates a layer with calculated field values.
    """

    @property
    def description(self) -> str:
        return """

        CalculateField_geoanalytics(input_layer, output_name, field_name, field_type, expression, {track_aware}, {track_fields;track_fields...}, {data_store}, {time_boundary_split}, {time_boundary_reference})

        Creates a layer with calculated field values.

     INPUTS:
      input_layer (Record Set):
          The input features that will have a field calculated.
      output_name (String):
          The name of the output feature service.
      field_name (String):
          The name of the field that will have values calculated. This can be an
          existing field or a new field name.
      field_type (String):
          Specifies the field type for the calculated field.STRING-The new field
          will be of type text.INTEGER-The new field will
          be of type integer.FLOAT-The new field will be of type float.DATE-
          The new field will be of type date.
      expression (Calculator Expression):
          Calculates values in the field. Expressions are written in Arcade and
          can include operators and multiple fields. Calculated values are
          applied in the units of the spatial reference of the input unless you
          are using a geographic coordinate system, in which case they will be
          in meters.
      track_aware {Boolean}:
          Specifies whether the expression will use a track-aware
          expression.TRACK_AWARE-The expression will use a track-aware
          expression, and a
          track field must be specified.NOT_TRACK_AWARE-The expression will not
          use a track-aware expression.
          This is the default.
      track_fields {Field}:
          One or more fields that will be used to identify unique tracks.
      data_store {String}:
          Specifies the ArcGIS Data Store where the output will be saved. The
          default is SPATIOTEMPORAL_DATA_STORE. All results stored in a
          spatiotemporal big data store will be stored in WGS84. Results stored
          in a relational data store will maintain their coordinate
          system.SPATIOTEMPORAL_DATA_STORE-Output will be stored in a
          spatiotemporal
          big data store. This is the default.RELATIONAL_DATA_STORE-Output will
          be stored in a relational data
          store.
      time_boundary_split {Time Unit}:
          A time span to split the input data into for analysis. A time boundary
          allows you to analyze values within a defined time span. For example,
          if you use a time boundary of 1 day, starting on January 1, 1980,
          tracks will be split at the beginning of every day. This parameter is
          only available with ArcGIS Enterprise 10.7 and later.
      time_boundary_reference {Date}:
          The reference time used to split the input data into for analysis.
          Time boundaries will be created for the entire span of the data, and
          the reference time does not need to occur at the start. If no
          reference time is specified, January 1, 1970, is used. This parameter
          is only available with ArcGIS Enterprise 10.7 and later.

        """