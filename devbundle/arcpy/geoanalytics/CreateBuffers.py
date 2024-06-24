# Generated documentation for module arcpy.geoanalytics


class CreateBuffers(object):
    """
    Creates buffers around input features to a specified distance.
    """

    @property
    def description(self) -> str:
        return """

        CreateBuffers_geoanalytics(input_layer, output_name, method, buffer_type, {buffer_field}, {buffer_distance}, {buffer_expression}, {dissolve_option}, {dissolve_fields;dissolve_fields...}, {summary_fields;summary_fields...}, {multipart}, {data_store})

        Creates buffers around input features to a specified distance.

     INPUTS:
      input_layer (Feature Set):
          The point, polyline, or polygon features that will be buffered.
      output_name (String):
          The name of the output feature service.
      method (String):
          Specifies the method that will be used to create the buffers.GEODESIC-
          Buffers will be created using a shape-preserving geodesic
          buffer method regardless of the input coordinate system. This is the
          default.PLANAR-If the input features are in a projected coordinate
          system,
          Euclidean buffers will be created. If the input features are in a
          geographic coordinate system, geodesic buffers will be created. The
          Output Coordinate System environment setting can be used to specify a
          coordinate system.
      buffer_type (String):
          Specifies how the buffer distance will be defined.DISTANCE-The same
          linear distance will be applied to all
          features.FIELD-A numeric or string field will be selected to represent
          the
          buffer distance.EXPRESSION-An expression will be built using fields,
          constants, and
          mathematical operations to represent the buffer distance.
      buffer_field {Field}:
          The field that contains the buffer distance for each feature. If a
          field value is a number, it is assumed that the distance is in the
          linear unit of the input_layer value spatial reference, unless the
          input_layer value is in a geographic coordinate system, in which case,
          the value is assumed to be in meters. If the linear unit specified in
          the field values is invalid or not recognized, the linear unit of the
          input features' spatial reference will be used by default.
      buffer_distance {Linear Unit}:
          The distance around the input features that will be buffered.
      buffer_expression {Calculator Expression}:
          An equation using fields and mathematical operators that will
          be applied as a buffer to each feature. Fields must be numeric and the
          expression can include [+ - * / ] operators and multiple fields.
          Calculated values are applied in meters unless otherwise specified.
          For example, to apply a buffer that multiples a numeric field namedin
          kilometers by 2 and adds 15 meters. distanceWith ArcGIS
          Enterprise 10.5 and 10.5.1 expressions will be formatted
          as the following: as_kilometers(distance) * 2 + as_meters(15). With
          ArcGIS Enterprise 10.6 or later, use Arcade expressions such as
          as_kilometers($feature["distance"]) * 2 + as_meters(15).
      dissolve_option {String}:
          Specifies the dissolve option that will be used to remove buffer
          overlap.NONE-An individual buffer for each feature will be maintained
          regardless of overlap. This is the default.ALL-All buffers will be
          dissolved together into a single feature,
          removing any overlap.LIST-Any buffers sharing attribute values in the
          listed fields
          (carried over from the input features) will be dissolved.
      dissolve_fields {Field}:
          A list of one or more fields from the input features on which output
          buffers will be dissolved. Any buffers sharing attribute values in the
          listed fields will be dissolved. This parameter is only required when
          dissolve_option is LIST.
      summary_fields {Value Table}:
          Specifies statistics that will be applied to numeric and string
          fields. If left empty, only count will be calculated. These statistics
          are only applied when dissolve_option is LIST or ALL.COUNT-The number
          of nonnull values. It can be used on numeric fields
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
          type string.
      multipart {Boolean}:
          Specifies whether multipart features will be created.MULTI_PART-Output
          multipart features will be created where
          appropriate.SINGLE_PART-Multipart features will not be created;
          individual
          features will be created for each part instead. This is the default.
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

        """