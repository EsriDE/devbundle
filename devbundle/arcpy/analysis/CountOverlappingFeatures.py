# Generated documentation for module arcpy.analysis


class CountOverlappingFeatures(object):
    """
    Generates planarized overlapping features from the input features. The count of overlapping features is written to the output features.
    """

    @property
    def description(self) -> str:
        return """

        CountOverlappingFeatures_analysis(in_features;in_features..., out_feature_class, {min_overlap_count}, {out_overlap_table})

        Generates planarized overlapping features from the input features. The
        count of overlapping features is written to the output features.

     INPUTS:
      in_features (Feature Layer):
          The input feature classes or layers. The input features can be point,
          multipoint, line, or polygon. If multiple inputs are provided, they
          must all be the same geometry type.
      min_overlap_count {Long}:
          Limits the output to only locations that meet or exceed the specified
          number of overlaps. The default value is 1.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the overlap count.
      out_overlap_table {Table}:
          The output table containing records for each individual overlapping
          geometry.

        """