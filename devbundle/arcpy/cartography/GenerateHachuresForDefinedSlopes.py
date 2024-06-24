# Generated documentation for module arcpy.cartography


class GenerateHachuresForDefinedSlopes(object):
    """
    Creates multipart lines or polygons representing the slope between the lines representing the upper and lower parts of a slope.
    """

    @property
    def description(self) -> str:
        return """

        GenerateHachuresForDefinedSlopes_cartography(upper_lines, lower_lines, output_feature_class, {output_type}, {fully_connected}, {search_distance}, {interval}, {minimum_length}, {alternate_hachures}, {perpendicular}, {polygon_base_width})

        Creates multipart lines or polygons representing the slope between the
        lines representing the upper and lower parts of a slope.

     INPUTS:
      upper_lines (Feature Layer):
          The line features that represent the top of a slope.
      lower_lines (Feature Layer):
          The line features that represent the bottom of a slope.
      output_type {String}:
          Specifies whether polygon triangles or tick lines will be created to
          represent the slope.POLYGON_TRIANGLES-Multipart polygon features will
          be created in which
          a triangular polygon is created for each hachure, with the base along
          the upper line. This is the default.LINE_TICKS-Multipart line features
          will be created in which a linear
          tick is created for each hachure.
      fully_connected {Boolean}:
          Specifies whether the upper and lower lines in the input data form
          fully connected areas. If the upper and lower lines are not fully
          connected, choose NOT_CONNECTED to create hachures inside areas that
          are derived by connecting the extremities of the upper and lower
          features. If the upper and lower lines are fully connected, choose
          FULLY_CONNECTED to create hachures inside the fully enclosed
          areas.NOT_CONNECTED-The upper and lower features are not fully
          connected in
          the input data. New connections between the upper and lower features
          will be derived. This is the default.FULLY_CONNECTED-The upper and
          lower features are fully connected in
          the input data. New connections between features will not be derived.
      search_distance {Linear Unit}:
          The distance used when deriving connections between the upper and
          lower features. When the extremities for the upper and lower feature
          are within this distance, the area between the features is used for
          creating hachures. The default value is 20 meters. When the
          fully_connected parameter is set to FULLY_CONNECTED, this parameter is
          ignored.
      interval {Linear Unit}:
          The distance between the hachure ticks or triangles within the slope
          area. The default value is 10 meters.
      minimum_length {Linear Unit}:
          The length a hachure tick or triangle must be to be created. Hachures
          that are shorter than this length will not be created. The default
          value is 0 meters.
      alternate_hachures {Boolean}:
          Specifies whether the length of every other hachure triangle or tick
          will differ.UNIFORM_HACHURES-All hachures will be of uniform length,
          which is the
          distance between the upper and lower slope lines. This is the
          default.ALTERNATE_HACHURES-Every other hachure will be one-half the
          distance
          between the upper and lower slope lines.
      perpendicular {Boolean}:
          Specifies whether the hachure ticks or triangles will be perpendicular
          to the upper slope line.NOT_PERPENDICULAR-Hachures will be oriented
          to obtain even spacing.
          This is the default.PERPENDICULAR-Hachures will be oriented
          perpendicularly to the upper
          line.
      polygon_base_width {Linear Unit}:
          The width of the base of triangular polygon hachures. This parameter
          is enabled only when the output_type parameter is set to
          polygon_triangles. The default value is 5 meters.

     OUTPUTS:
      output_feature_class (Feature Class):
          The output feature class containing multipart line or polygon hachures
          representing the slope area.

        """