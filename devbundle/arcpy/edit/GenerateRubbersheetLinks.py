# Generated documentation for module arcpy.edit


class GenerateRubbersheetLinks(object):
    """
    Finds where the source line features spatially match the target line features and generates lines representing links from source locations to corresponding target locations for rubbersheeting.
    """

    @property
    def description(self) -> str:
        return """

        GenerateRubbersheetLinks_edit(source_features, target_features, out_feature_class, search_distance, {match_fields;match_fields...}, {out_match_table})

        Finds where the source line features spatially match the target line
        features and generates lines representing links from source locations
        to corresponding target locations for rubbersheeting.

     INPUTS:
      source_features (Feature Layer):
          The line features that will be used as source features for generating
          rubbersheet links. All links start at source features.
      target_features (Feature Layer):
          The line features that will be used as target features for generating
          rubbersheet links. All links end at matched target features.
      search_distance (Linear Unit):
          The distance that will be used to search for match candidates. A
          distance must be specified and it must be greater than zero. You can
          choose a preferred unit. The default is the feature unit.
      match_fields {Value Table}:
          Lists of fields from source and target features. If provided, each
          pair of fields are checked for match candidates to help determine the
          right match.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing lines representing regular
          rubbersheet links.
      out_match_table {Table}:
          The output table containing complete feature matching information.

        """