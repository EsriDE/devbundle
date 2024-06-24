# Generated documentation for module arcpy.ca


class SummarizePercentChange(object):
    """
    Calculates the percent change for features that correspond with point features representing two equal comparison time periods.
    """

    @property
    def description(self) -> str:
        return """

        SummarizePercentChange_ca(in_features, in_current_features, in_previous_features, out_feature_class, {search_radius})

        Calculates the percent change for features that correspond with point
        features representing two equal comparison time periods.

     INPUTS:
      in_features (Feature Layer):
          The coincident features from which comparison time periods will be
          counted and compared.
      in_current_features (Feature Layer):
          The point features filtered to the most recent comparison time
          period.For example, you can filter for crimes from the previous 14
          days.
      in_previous_features (Feature Layer):
          The point features filtered to the time period immediately preceding
          the current period. This time period must be of equal length to the
          current period to provide an accurate comparison.For example, if the
          current period contains features from January 15
          to January 28, the previous period contains features from January 1 to
          January 14.
      search_radius {Linear Unit}:
          The maximum distance from the in_features parameter value that a point
          feature will be considered coincident.This parameter is only enabled
          when point or line features are used as
          the input features.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing difference counts and percent
          change calculations for the time period comparison.

        """