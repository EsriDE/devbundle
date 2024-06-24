# Generated documentation for module arcpy.analysis


class GraphicBuffer(object):
    """
    Creates buffer polygons around input features to a specified distance. A number of cartographic shapes are available for buffer ends (caps) and corners (joins) when the buffer is generated around the feature.
    """

    @property
    def description(self) -> str:
        return """

        GraphicBuffer_analysis(in_features, out_feature_class, buffer_distance_or_field, {line_caps}, {line_joins}, {miter_limit}, {max_deviation})

        Creates buffer polygons around input features to a specified distance.
        A number of cartographic shapes are available for buffer ends (caps)
        and corners (joins) when the buffer is generated around the feature.

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
      line_caps {String}:
          Specifies the type of caps (ends) of the input features that will be
          buffered. This parameter is only supported for point and polygon
          features.SQUARE-The output buffer will have a square cap around the
          end of the
          input segment. This is the default.BUTT-The output buffer will have a
          cap perpendicular to the end of the
          input segment.ROUND-The output buffer will have a cap that is round at
          the end of
          the input segment.
      line_joins {String}:
          Specifies the shape of the buffer at corners where two segments join.
          This parameter is only supported for line and polygon
          features.MITER-The output buffer feature will be a square or sharp
          shape around
          corners. For example, a square input polygon feature will have a
          square buffer feature. This is the default.BEVEL-The output buffer
          feature for inner corners will be squared, and
          the outer corner will be cut perpendicular to the farthest point of
          the corner.ROUND-The output buffer feature for inner corners will be
          squared, and
          the outer corner will be round.
      miter_limit {Double}:
          Where line segments meet at a sharp angle and the line_joins parameter
          value has been specified as MITER, this parameter can be used to
          control how sharp corners in buffer output come to a point. In some
          cases, the outer angle where two lines join is quite large when using
          the MITER option. This may cause the point of the corner to extend
          farther than intended.
      max_deviation {Linear Unit}:
          The maximum distance the output buffer polygon boundary will deviate
          from the true ideal buffer boundary. The true buffer boundary is a
          curve, and the output polygon boundary is a densified polyline. Using
          this parameter, you can control how well the output polygon boundary
          approximates the true buffer boundary.If the parameter is not set or
          is set to 0, the tool will identify the
          maximum deviation. It is recommended that you use the default value.
          Performance degradation in the tool or in subsequent analysis can
          result from using a maximum offset deviation value that is too small.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class containing the output buffers.

        """