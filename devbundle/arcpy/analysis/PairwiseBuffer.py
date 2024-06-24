# Generated documentation for module arcpy.analysis


class PairwiseBuffer(object):
    """
    Creates buffer polygons around input features to a specified distance using a parallel processing approach.
    """

    @property
    def description(self) -> str:
        return """

        PairwiseBuffer_analysis(in_features, out_feature_class, buffer_distance_or_field, {dissolve_option}, {dissolve_field;dissolve_field...}, {method}, {max_deviation})

        Creates buffer polygons around input features to a specified distance
        using a parallel processing approach.

     INPUTS:
      in_features (Feature Layer):
          The input point, line, or polygon features that will be buffered.
      buffer_distance_or_field (Linear Unit / Field):
          The distance around the input features that will be buffered.
          Distances can be provided as either a value representing a linear
          distance or a field from the input features that contains the distance
          to buffer each feature.If linear units are not specified or are
          entered as Unknown, the
          linear unit of the input features' spatial reference will be used.When
          specifying a distance, if the linear unit has two words, such as
          Decimal Degrees, combine the two words into one (for example, 20
          DecimalDegrees).
      dissolve_option {String}:
          Specifies the type of dissolve operation that will be performed to
          remove buffer overlap.NONE-An individual buffer for each feature will
          be maintained,
          regardless of overlap. This is the default.ALL-All buffers will be
          dissolved together into a single feature,
          removing any overlap.LIST-Any buffers sharing attribute values in the
          listed fields
          (carried over from the input features) will be dissolved.
      dissolve_field {Field}:
          The list of fields from the input features on which the output buffers
          will be dissolved. Any buffers sharing attribute values in the listed
          fields (carried over from the input features) will be dissolved.
      method {String}:
          Specifies whether the planar or geodesic method will be used to create
          the buffers. PLANAR-If the input features are in a projected
          coordinate
          system, Euclidean buffers will be created. If the input features are
          in a geographic coordinate system and the buffer distance is in linear
          units (meters, feet, and so forth, as opposed to angular units such as
          degrees), geodesic buffers will be created. This is the default.
          You can use the Output Coordinate System environment setting to
          specify the coordinate system to use. For example, if the input
          features are in a projected coordinate system, you can set the
          environment to a geographic coordinate system to create geodesic
          buffers.GEODESIC-All buffers will be created using a shape-preserving
          geodesic
          buffer method, regardless of the input coordinate system.
      max_deviation {Linear Unit}:
          The maximum distance the resulting output buffer polygon boundary will
          deviate from the true buffer boundary.The true buffer boundary is a
          curve. However, the resulting polygon
          boundary is a densified polyline. Using this parameter, you can
          control how the output polygon boundary approximates the true buffer
          boundary.If this parameter is not set or is set to 0, the tool will
          identify
          the maximum deviation. It is recommended that you use the default
          value. Performance degradation (in the tool and in subsequent
          analyses) may result from using a maximum offset deviation that is too
          small.See the max_deviation parameter information in the Densify tool
          documentation for details.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class containing the output buffers.

        """