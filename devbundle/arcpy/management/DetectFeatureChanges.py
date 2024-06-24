# Generated documentation for module arcpy.management


class DetectFeatureChanges(object):
    """
    Finds where the update line features spatially match the base line features and detects spatial changes, attribute changes, or both, as well as no change. It then creates an output feature class containing matched update features with information about their changes, unmatched update features, and unmatched base features.
    """

    @property
    def description(self) -> str:
        return """

        DetectFeatureChanges_management(update_features, base_features, out_feature_class, search_distance, {match_fields;match_fields...}, {out_match_table}, {change_tolerance}, {compare_fields;compare_fields...}, {compare_line_direction})

        Finds where the update line features spatially match the base line
        features and detects spatial changes, attribute changes, or both, as
        well as no change. It then creates an output feature class containing
        matched update features with information about their changes,
        unmatched update features, and unmatched base features.

     INPUTS:
      update_features (Feature Layer):
          The line features that will be compared to the base features.
      base_features (Feature Layer):
          The line features that will be compared to the update features for
          change detection.
      search_distance (Linear Unit):
          The distance that will be used to search for match candidates. A
          distance must be specified and it must be greater than zero. You can
          choose a preferred unit. The default is the feature unit.
      match_fields {Value Table}:
          The match fields from the update and base features. If specified, each
          pair of fields are compared for match candidates to help determine the
          right match.
      change_tolerance {Linear Unit}:
          The distance used to determine if there is a spatial change.
          All matched update features and base features are compared to this
          tolerance. If any portions of the update or the base features fall
          outside the zone around the matched feature, it is considered a
          spatial change. The value must be greater than the XY Tolerance of the
          input data so this process can be performed and the output will
          include theandfields. The default is 0, meaning this process is not
          performed. Any value between 0 and the data's XY Tolerance
          (inclusively) will make the process irrelevant and will be replaced by
          0. You can choose a unit; the default is the feature unit.
          LEN_PCTLEN_ABS
      compare_fields {Value Table}:
          The fields that will determine if there is an attribute change between
          the matched update and base features.
      compare_line_direction {Boolean}:
          Specifies whether line directions will be compared for matched
          features.NO_COMPARE_DIRECTION-Line directions will not be compared for
          matched
          features. This is the default.COMPARE_DIRECTION-Line directions will
          be compared for matched
          features.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output line feature class containing the change information. The
          output contains all participating update features (matched and
          unmatched) and any unmatched base features.
      out_match_table {Table}:
          The output table containing complete feature matching information.

        """