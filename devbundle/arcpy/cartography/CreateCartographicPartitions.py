# Generated documentation for module arcpy.cartography


class CreateCartographicPartitions(object):
    """
    Creates a mesh of polygon features that cover the input feature class in which each output polygon encloses no more than a specified number of input features or input vertices. as determined by the density and distribution of the input features.
    """

    @property
    def description(self) -> str:
        return """

        CreateCartographicPartitions_cartography(in_features;in_features..., out_features, feature_count, {partition_method})

        Creates a mesh of polygon features that cover the input feature class
        in which each output polygon encloses no more than a specified number
        of input features or input vertices. as determined by the density and
        distribution of the input features.

     INPUTS:
      in_features (Feature Layer):
          The input feature classes or layers with feature distribution and
          density, or vertex distribution and density, that determine the size
          and arrangement of output polygons. The input features are typically
          destined for subsequent processing with other geoprocessing tools.
          Typically, the input features, when considered simultaneously, would
          exceed memory limitations of other tools, so partitions are created to
          subdivide inputs for processing.
      feature_count (Long):
          The ideal number of features or vertices (depending on the
          partition_method parameter value) to be enclosed by each polygon in
          the output feature class. The recommended count for features is
          50,000, which is the default value. For vertices, 1 million vertices
          will consume approximately 0.5 GB of memory depending on the tool
          using the partitions. The feature count cannot be less than 500.
      partition_method {String}:
          Specifies whether the feature_count parameter references the ideal
          number of features or the ideal number of vertices in each output
          polygon.FEATURES-Partitioning considers the number and density of
          individual
          features. This method is applicable in most cases and is the
          default.VERTICES-Partitioning considers the number and density of
          vertices.
          This method is used in cases in which the input data contains a
          relatively small number of very complex features, such as high-
          resolution country polygons, or when very long features are likely to
          cross multiple partition boundaries, such as contour lines.

     OUTPUTS:
      out_features (Feature Class):
          The output polygon feature class of partitions each of which encloses
          a manageable number of input features or manageable number of input
          vertices not exceeding the number specified by the feature_count
          parameter.

        """