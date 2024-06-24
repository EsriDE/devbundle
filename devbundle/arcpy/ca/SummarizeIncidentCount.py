# Generated documentation for module arcpy.ca


class SummarizeIncidentCount(object):
    """
    Creates a feature class with coincident point counts. Coincident point counts for line and point features are determined by a specified maximum distance. Point counts for polygon features are determine by whether point features or portions of features overlap with the polygon feature.
    """

    @property
    def description(self) -> str:
        return """

        SummarizeIncidentCount_ca(in_features, in_sum_features, out_feature_class, {search_radius}, {group_field})

        Creates a feature class with coincident point counts. Coincident point
        counts for line and point features are determined by a specified
        maximum distance. Point counts for polygon features are determine by
        whether point features or portions of features overlap with the
        polygon feature.

     INPUTS:
      in_features (Feature Layer):
          The input features to which coincident point counts will be
          calculated.
      in_sum_features (Feature Layer):
          The point features coincident with the input features.
      search_radius {Linear Unit}:
          The maximum distance from anpoint or line that a point feature
          will be considered coincident. Input Features        This
          parameter is not active when theis a polygon.
          Input Features
      group_field {Field}:
          A field containing the value used to split point counts. Additional
          fields containing counts for each unique value in the group field will
          be generated.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output choropleth count feature class, symbolized by total count.

        """