# Generated documentation for module arcpy.analysis


class Buffer(object):
    """
    Creates buffer polygons around input features to a specified distance.
    """

    @property
    def description(self) -> str:
        return """

        Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field, {line_side}, {line_end_type}, {dissolve_option}, {dissolve_field;dissolve_field...}, {method})

        Creates buffer polygons around input features to a specified distance.

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
      line_side {String}:
          Specifies the sides of the input features that will be buffered. This
          parameter is only supported for polygon and line features.FULL-For
          lines, buffers will be generated on both sides of the line.
          For polygons, buffers will be generated around the polygon and will
          contain and overlap the area of the input features. This is the
          default.LEFT-For lines, buffers will be generated on the topological
          left of
          the line. This option is not supported for polygon input
          features.RIGHT-For lines, buffers will be generated on the topological
          right of
          the line. This option is not supported for polygon input
          features.OUTSIDE_ONLY-For polygons, buffers will be generated outside
          the input
          polygon only (the area inside the input polygon will be erased from
          the output buffer). This option is not supported for line input
          features.This optional parameter is not available with a Desktop Basic
          or
          Desktop Standard license.
      line_end_type {String}:
          Specifies the shape of the buffer at the end of line input features.
          This parameter is not valid for polygon input features.ROUND-The ends
          of the buffer will be round, in the shape of a half
          circle. This is the default.FLAT-The ends of the buffer will be flat
          or squared and will end at
          the endpoint of the input line feature.This optional parameter is not
          available with a Desktop Basic or
          Desktop Standard license.
      dissolve_option {String}:
          Specifies the type of dissolve that will be performed to remove buffer
          overlap.NONE-An individual buffer for each feature will be maintained,
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

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class containing the output buffers.

        """