# Generated documentation for module arcpy.stats


class SimilaritySearch(object):
    """
    Identifies which candidate features are most similar or most dissimilar to one or more input features based on feature attributes.
    """

    @property
    def description(self) -> str:
        return """

        SimilaritySearch_stats(Input_Features_To_Match, Candidate_Features, Output_Features, Collapse_Output_To_Points, Most_Or_Least_Similar, Match_Method, Number_Of_Results, Attributes_Of_Interest;Attributes_Of_Interest..., {Fields_To_Append_To_Output;Fields_To_Append_To_Output...})

        Identifies which candidate features are most similar or most
        dissimilar to one or more input features based on feature attributes.

     INPUTS:
      Input_Features_To_Match (Feature Layer):
          The layer, or a selection on a layer, containing the features you want
          to match; you are searching for other features that look like these
          features. When more than one feature is provided, matching is based on
          attribute averages. When theandvalues are from a single
          dataset layer, you can do
          the following:         Input Features To MatchCandidate Features
          Copy the layer to thepane, making a duplicate layer.
          ContentsRename the duplicate layer. On the renamed layer,
          make a selection or set a definition
          query for the reference features you want to match. Use the new layer
          created for theparameter. Input Features To Match
          Apply a selection or set a definition query on the original
          layer so it excludes the reference features. This will be the layer to
          use for theparameter. Candidate Features
      Candidate_Features (Feature Layer):
          The layer, or a selection on a layer, containing candidate matching
          features. The tool will check for features most similar (or most
          dissimilar) to the Input_Features_To_Match values among these
          candidates.
      Collapse_Output_To_Points (Boolean):
          Specifies whether the geometry for the Output_Features parameter will
          be collapsed to points or will match the original geometry (lines or
          polygons) of the input features if the Input_Features_To_Match and
          Candidate_Features parameter values are both either lines or polygons.
          This parameter is only available with an Desktop Advanced license.
          Choosing COLLAPSE will improve tool performance for large line and
          polygon datasets.COLLAPSE-The line and polygon features will be
          represented as feature
          centroids (points).NO_COLLAPSE-The output geometry will match the line
          or polygon
          geometry of the input features. This is the default.
      Most_Or_Least_Similar (String):
          Specifies whether features that are most similar or most dissimilar to
          the Input_Features_To_Match values will be
          identified.MOST_SIMILAR-Features that are most similar will be
          identified. This
          is the default.LEAST_SIMILAR-Features that are most dissimilar will be
          identified.BOTH-Features that are most similar and features that are
          most
          dissimilar will both be identified.
      Match_Method (String):
          Specifies whether matching will be based on values, ranks, or cosine
          relationships. ATTRIBUTE_VALUES-Matching will be based on the
          sum of squared
          standardized attribute value differences for all of thevalues. This is
          the default. Attributes Of Interest
          RANKED_ATTRIBUTE_VALUES-Matching will be based on the sum of
          squared rank differences for all of thevalues. Attributes Of
          Interest         ATTRIBUTE_PROFILES-Matching will be computed as a
          function of
          cosine similarity for all of thevalues. Attributes Of Interest
      Number_Of_Results (Long):
          The number of solution matches to find. Entering zero or a number
          larger than the total number of Candidate_Features values will return
          rankings for all the candidate features. The default is 10.
      Attributes_Of_Interest (Field):
          The numeric attributes representing the matching criteria.
      Fields_To_Append_To_Output {Field}:
          The fields to include with the Output_Features parameter. These fields
          are not used to determine similarity; they are only included in the
          Output_Features parameter for reference.

     OUTPUTS:
      Output_Features (Feature Class):
          The output feature class containing a record for each of the
          Input_Features_To_Match values and for all the solution-matching
          features found.

        """