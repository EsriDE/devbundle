# Generated documentation for module arcpy.management


class GenerateRectanglesAlongLines(object):
    """
    Creates a series of rectangular polygons that follow a single linear feature or a group of linear features.
    """

    @property
    def description(self) -> str:
        return """

        GenerateRectanglesAlongLines_management(in_features, out_feature_class, {length_along_line}, {length_perpendicular_to_line}, {spatial_sort_method})

        Creates a series of rectangular polygons that follow a single linear
        feature or a group of linear features.

     INPUTS:
      in_features (Feature Layer):
          The input polyline features defining the path of the features.
      length_along_line {Linear Unit}:
          The length of the output polygon features along the input line
          features. The default value is determined by the spatial reference of
          the input line features. This value will be 1/100 of the input feature
          class extent along the x-axis.
      length_perpendicular_to_line {Linear Unit}:
          The length of the output polygon features perpendicular to the input
          line features. The default value is determined by the spatial
          reference of the input line features. This value will be one-half the
          number used for the length along the line.
      spatial_sort_method {String}:
          Output features are created in a sequential order and require a
          spatial starting point. Setting the direction type to upper right will
          start the output features in the upper right of each input
          feature.UR-Features start in the upper right corner. This is the
          default.UL-Features start in the upper left corner.LR-Features starts
          in the lower right corner.LL-Features starts in the lower left corner.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class.

        """