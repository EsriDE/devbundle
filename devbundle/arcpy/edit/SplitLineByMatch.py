# Generated documentation for module arcpy.edit


class SplitLineByMatch(object):
    """
    Splits features based on matching relationships to obtain better corresponding line segmentation.
    """

    @property
    def description(self) -> str:
        return """

        SplitLineByMatch_edit(in_features, matched_features, in_match_table, out_feature_class, search_distance, {in_features_as}, {out_point_feature_class}, {split_dangle}, {min_match_group_length}, {min_split_length}, {split_fields;split_fields...})

        Splits features based on matching relationships to obtain better
        corresponding line segmentation.

     INPUTS:
      in_features (Feature Layer):
          The input line features that will be split. They must be prematched
          with the matched features.
      matched_features (Feature Layer):
          The features that were prematched with the input features. Matched
          features are used as reference when splitting the input features.
      in_match_table (Table View):
          A table that includes matching information between input and matched
          features.
      search_distance (Linear Unit):
          The distance value that will be used to determine split locations. The
          value must be greater than 0. If units are not specified, the units of
          the input will be used.
      in_features_as {String}:
          Specifies whether the input features in the match table are source
          features or target features, so the correct features will be
          split.AS_SOURCE-The input features are stored as the source features
          in the
          match table. This is the default.AS_TARGET-The input features are
          stored as the target features in the
          match table.
      split_dangle {Boolean}:
          Specifies whether dangling lines will be split.SPLIT_DANGLE-Dangling
          lines will be split following the tool's split
          rules. This is the default.NO_SPLIT_DANGLE-Dangling lines will not be
          split.
      min_match_group_length {Linear Unit}:
          The minimum length a match group can be. A given match group will only
          participate in the splitting process if either the total length of the
          input features or the total length of the matched features are greater
          than the value provided.
      min_split_length {Linear Unit}:
          The minimum length a split piece can be. If a split will result in one
          or both of the split pieces being shorter than the value provided, the
          split will not occur.
      split_fields {Field}:
          A list of numeric fields from the input features. Their field values
          will be based on the proportions of the split lines.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing split lines and original lines
          that are not split.
      out_point_feature_class {Feature Class}:
          The output point feature class containing points that represent split
          locations.

        """