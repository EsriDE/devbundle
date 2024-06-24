# Generated documentation for module arcpy.edit


class GenerateEdgematchLinks(object):
    """
    Finds matching but disconnected line features along the edges of the source data's area and its adjacent data's area, and generates edgematch links from the source lines to the matched adjacent lines.
    """

    @property
    def description(self) -> str:
        return """

        GenerateEdgematchLinks_edit(source_features, adjacent_features, out_feature_class, search_distance, {match_fields;match_fields...})

        Finds matching but disconnected line features along the edges of the
        source data's area and its adjacent data's area, and generates
        edgematch links from the source lines to the matched adjacent lines.

     INPUTS:
      source_features (Feature Layer):
          The line features that will be used as edgematching source features.
          All edgematch links start at source features.
      adjacent_features (Feature Layer):
          The line features that are adjacent to the source features. All
          edgematch links end at matched adjacent features.
      search_distance (Linear Unit):
          The distance that will be used to search for match candidates. A
          distance must be specified and it must be greater than zero. You can
          choose a preferred unit. The default is the feature unit.
      match_fields {Value Table}:
          The fields from the source and target features in which the target
          fields are from the adjacent features. If provided, each pair of
          fields will be checked for match candidates to help determine the
          right match.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing lines representing edgematch
          links.

        """