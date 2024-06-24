# Generated documentation for module arcpy.edit


class AlignFeatures(object):
    """
    Identifies inconsistent portions of the input features compared to target features within a search distance and aligns them with the target features.
    """

    @property
    def description(self) -> str:
        return """

        AlignFeatures_edit(in_features, target_features, search_distance, {match_fields;match_fields...})

        Identifies inconsistent portions of the input features compared to
        target features within a search distance and aligns them with the
        target features.

     INPUTS:
      in_features (Feature Layer):
          The input line or polygon features that will be adjusted.
      target_features (Feature Layer):
          The input lines or polygons to which the input features will be
          aligned.
      search_distance (Linear Unit):
          The distance that will be used to search for match candidates. A
          distance must be specified and it must be greater than zero. You can
          choose a preferred unit. The default is the feature unit.
      match_fields {Value Table}:
          The fields from the input and target features. If provided, each pair
          of fields will be checked for match candidates to help determine the
          right match.

        """