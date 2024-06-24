# Generated documentation for module arcpy.geoanalytics


class SnapTracks(object):
    """
    Snaps input track points to lines. The time-enabled point data must include features that represent an instant in time. Traversable lines with fields indicating the from and to nodes are required for analysis.
    """

    @property
    def description(self) -> str:
        return """

        SnapTracks_geoanalytics(input_points, input_lines, output_name, track_fields;track_fields..., search_distance, connectivity_field_matching;connectivity_field_matching..., {line_fields_to_include;line_fields_to_include...}, {distance_method}, {direction_value_matching;direction_value_matching...}, {output_mode}, {data_store}, {time_split}, {distance_split}, {time_boundary_split}, {time_boundary_reference})

        Snaps input track points to lines. The time-enabled point data must
        include features that represent an instant in time. Traversable lines
        with fields indicating the from and to nodes are required for
        analysis.

     INPUTS:
      input_points (Feature Set):
          The points that will be matched to lines. The input must be a time-
          enabled point layer that represents an instant in time and must
          contain at least one field that identifies unique tracks.
      input_lines (Feature Set):
          The lines to which points will be matched. The input must contain
          fields with values indicating the from and to nodes of the line.
      output_name (String):
          The name of the output feature service.
      track_fields (Field):
          One or more fields that will be used to identify unique tracks.
      search_distance (Linear Unit):
          The maximum distance allowed between a point and any line to be
          considered a match. It is recommended that you use values less than or
          equal to 75 meters. Larger distances will result in a longer process
          time and less accurate results.
      connectivity_field_matching (Value Table):
          The line layer fields that will be used to define the connectivity of
          the input line features.Unique ID-The line layer field that contains
          the unique ID value for
          each line featureFrom Node-The line layer field that contains the from
          node valuesTo Node-The line layer field that contains the to node
          values
      line_fields_to_include {Field}:
          One or more fields from the input line layer that will be included in
          the output result.
      distance_method {String}:
          Specifies the method that will be used to calculate distances between
          points and lines.GEODESIC-Geodesic distances will be
          calculated.PLANAR-Planar distances
          will be calculated.
      direction_value_matching {Value Table}:
          The line layer field and attribute values that will be used to
          define the direction of the input line features. For example, a line
          layer has a field namedwith values T (backward), F (forward), B
          (both), and "" (none). If no value is specified, the line is assumed
          to be bidirectional. directionDirection Field-The field from
          the line layer that describes the
          direction of travel. Forward Value-The value from thethat
          indicates the supported
          direction of travel is forward along a line. Direction Field
          Backward Value-The value from thethat indicates the
          supported direction of travel is backward along a line.
          Direction Field          Both Value-The value from thethat indicates
          both forward and
          backward directions of travel are supported along a line.
          Direction Field          None Value-The value from thethat indicates
          there are no
          supported directions of travel along a line. Direction Field
      output_mode {String}:
          Specifies whether all input features or only the input features that
          were matched to a line feature will be returned.ALL_FEATURES-All input
          point features will be returned regardless of
          whether they were matched to a line feature. This is the
          default.MATCHED_FEATURES-Only input point features that were matched
          to a line
          feature will be returned.
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
      time_split {Time Unit}:
          Features that are farther apart in time than the time-split duration
          will be split into separate tracks.
      distance_split {Linear Unit}:
          Features that are farther apart in distance than the distance split
          value will be split into separate tracks. This parameter is only
          available with ArcGIS Enterprise 10.6 and later.
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