# Generated documentation for module arcpy.geoanalytics


class DetectIncidents(object):
    """
    Creates a layer that detects features that meet a given condition.
    """

    @property
    def description(self) -> str:
        return """

        DetectIncidents_geoanalytics(input_layer, output_name, track_fields;track_fields..., start_condition, {end_condition}, {output_mode}, {data_store}, {time_boundary_split}, {time_boundary_reference})

        Creates a layer that detects features that meet a given condition.

     INPUTS:
      input_layer (Record Set):
          The input features that contain potential incidents.
      output_name (String):
          The name of the output feature service.
      track_fields (Field):
          A field or fields that will be used to identify unique tracks.
      start_condition (Calculator Expression):
          The condition that will be used to identify incidents. Expressions are
          written in Arcade and can include [+ - * / ] operators and multiple
          fields.
      end_condition {Calculator Expression}:
          The condition that will be used to end incidents. If no end condition
          is specified, incidents will end when the start condition is no longer
          true.
      output_mode {String}:
          Specifies the features that will be returned.ALL_FEATURES-All the
          input features will be returned. This is the
          default.INCIDENTS-Only features that were found to be incidents will
          be
          returned.
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