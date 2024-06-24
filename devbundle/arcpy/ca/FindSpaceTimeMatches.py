# Generated documentation for module arcpy.ca


class FindSpaceTimeMatches(object):
    """
    Identifies matches between two feature classes based on proximity, time extent, or both.
    """

    @property
    def description(self) -> str:
        return """

        FindSpaceTimeMatches_ca(in_primary_features, in_comparison_features, out_primary_feature_class, out_comparison_feature_class, match_types;match_types..., {search_radius}, {temporal_search_radius}, {primary_start_date_field}, {comparison_start_date_field}, {primary_end_date_field}, {comparison_end_date_field})

        Identifies matches between two feature classes based on proximity,
        time extent, or both.

     INPUTS:
      in_primary_features (Feature Layer):
          The primary input feature class.
      in_comparison_features (Feature Layer):
          The comparison input feature class.
      match_types (String):
          Specifies the types of matches to compare.SPACE_AND_TIME-Matches based
          on both the time extent and proximity
          defined in the temporal and spatial search radius will be compared,
          for example, 25 meters and 10 minutes.SPACE_ONLY-Matches based only on
          the proximity defined in the spatial
          search radius will be compared, for example, 25
          meters.TIME_ONLY-Matches based only on the time extent defined in the
          temporal search radius will be compared, for example, 10 minutes.
      search_radius {Linear Unit}:
          The radius used to search between input feature classes.
      temporal_search_radius {Time Unit}:
          The time extent used to search between input feature classes.
      primary_start_date_field {Field}:
          The primary start date and time field of the input primary features.
      comparison_start_date_field {Field}:
          The comparison start date and time field of the input comparison
          features.
      primary_end_date_field {Field}:
          The primary end date and time field of the input primary features.
          When specified, the time range defined by the start and end date and
          the temporal search radius will be used to search comparison features.
          The temporal search radius can be set to 0 to compare only the time
          defined by the feature's time range.
      comparison_end_date_field {Field}:
          The comparison end date and time field of the input comparison
          features. When specified, the time range defined by the start and end
          date and the temporal search radius will be used to evaluate
          relationships with primary features. The temporal search radius can be
          set to 0 to compare only the time defined by the feature's time range.

     OUTPUTS:
      out_primary_feature_class (Feature Class):
          The output feature class containing features from the input primary
          features where output match types occurred.
      out_comparison_feature_class (Feature Class):
          The output feature class containing features from input comparison
          features where output match types occurred.

        """