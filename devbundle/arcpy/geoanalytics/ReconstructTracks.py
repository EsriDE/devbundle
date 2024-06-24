# Generated documentation for module arcpy.geoanalytics


class ReconstructTracks(object):
    """
    Creates line or polygon tracks from time-enabled input data.
    """

    @property
    def description(self) -> str:
        return """

        ReconstructTracks_geoanalytics(input_layer, output_name, track_fields;track_fields..., method, {buffer_type}, {buffer_field}, {buffer_expression}, {time_split}, {summary_fields;summary_fields...}, {data_store}, {distance_split}, {time_boundary_split}, {time_boundary_reference}, {split_expression}, {split_type})

        Creates line or polygon tracks from time-enabled input data.

     INPUTS:
      input_layer (Feature Set):
          The points or polygons to be reconstructed into tracks. The input must
          be a time-enabled layer that represents an instant in time.
      output_name (String):
          The name of the output feature service.
      track_fields (Field):
          One or more fields that will be used to identify unique tracks.
      method (String):
          Specifies the criteria that will be used to reconstruct tracks. If a
          buffer is used, the method parameter determines the type of
          buffer.GEODESIC-If the spatial reference can be panned, tracks will
          cross
          the date line when appropriate. If the spatial reference cannot be
          panned, tracks will be limited to the coordinate system extent and may
          not wrap.PLANAR-The tracks will not cross the date line.
      buffer_type {String}:
          Specifies how the buffer distance will be defined.FIELD-A single field
          will be used to define the buffer
          distance.EXPRESSION-An equation using fields and mathematical
          operators will be
          used to define the buffer distance.
      buffer_field {Field}:
          The field that will be used to buffer the input features. Field values
          are applied in the units of the spatial reference of the input unless
          you are using a geographic coordinate system, in which case they will
          be in meters.
      buffer_expression {Calculator Expression}:
          The expression that will be used to buffer input features. Fields must
          be numeric, and the expression can include [+ - * / ] operators and
          multiple fields. Calculated values are applied in the units of the
          spatial reference of the input unless you are using a geographic
          coordinate system, in which case they will be in meters.In ArcGIS
          Enterprise 10.5 and 10.5.1, expressions are formatted as
          as_kilometers(distance) * 2 + as_meters(15). In ArcGIS Enterprise 10.6
          or later, use Arcade expressions such as
          as_kilometers($feature.distance) * 2 + as_meters(15).The expression
          that will be used to buffer input features. Fields must
          be numeric, and the expression can include [+ - * / ] operators and
          multiple fields. Calculated values are applied in the units of the
          spatial reference of the input unless you are using a geographic
          coordinate system, in which case they will be in meters.In ArcGIS
          Enterprise 10.5 and 10.5.1, expressions are formatted as
          as_kilometers(distance) * 2 + as_meters(15). In ArcGIS Enterprise 10.6
          or later, use Arcade expressions such as
          as_kilometers($feature.distance) * 2 + as_meters(15).
      time_split {Time Unit}:
          Features that are farther apart in time than the time-split duration
          will be split into separate tracks.
      summary_fields {Value Table}:
          The statistics that will be calculated on specified fields.COUNT-The
          number of nonnull values. It can be used on numeric fields
          or strings. The count of [null, 0, 2] is 2.SUM-The sum of numeric
          values in a field. The sum of [null, null, 3]
          is 3.MEAN-The mean of numeric values. The mean of [0,2, null] is
          1.MIN-The minimum value of a numeric field. The minimum of [0, 2,
          null]
          is 0.MAX-The maximum value of a numeric field. The maximum value of
          [0, 2,
          null] is 2.STDDEV-The standard deviation of a numeric field. The
          standard
          deviation of [1] is null. The standard deviation of [null, 1,1,1] is
          null.VAR-The variance of a numeric field in a track. The variance of
          [1] is
          null. The variance of [null, 1,1,1] is null.RANGE-The range of a
          numeric field. This is calculated as the minimum
          value subtracted from the maximum value. The range of [0, null, 1] is
          1. The range of [null, 4] is 0.ANY-A sample string from a field of
          type string.FIRST-The first value of a specified field in a track.
          This option is
          available with ArcGIS Enterprise 10.8.1.LAST-The last value of a
          specified field in a track. This option is
          available with ArcGIS Enterprise 10.8.1.
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
      split_expression {Calculator Expression}:
          An expression that splits tracks based on values, geometry or time
          values. Expressions that validate to true will be split. This
          parameter is only available with ArcGIS Enterprise 10.9 and later.
      split_type {String}:
          Specifies how the track segment between two features is created when a
          track is split. The split type is applied to split expressions,
          distance splits, and time splits. This parameter is only available
          with ArcGIS Enterprise 10.9 and later.GAP-No segment is created
          between the two features. This is the
          default.FINISH_LAST-A segment is created between the two features that
          ends
          after the split.START_NEXT-A segment is created between the two
          features that ends
          before the split.

        """