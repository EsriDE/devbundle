# Generated documentation for module arcpy.stats


class HotSpotAnalysisComparison(object):
    """
    Compares two hot spot analysis result layers and measures their similarity and association.
    """

    @property
    def description(self) -> str:
        return """

        HotSpotAnalysisComparison_stats(in_hot_spot_1, in_hot_spot_2, out_features, {num_neighbors}, {num_perms}, {weighting_method}, {similarity_weights;similarity_weights...}, {in_weights_table}, {exclude_nonsig_features})

        Compares two hot spot analysis result layers and measures their
        similarity and association.

     INPUTS:
      in_hot_spot_1 (Feature Layer):
          The first hot spot analysis result layer.
      in_hot_spot_2 (Feature Layer):
          The second hot spot analysis result layer.
      num_neighbors {Long}:
          The number of neighbors around each feature that will be used for
          distance weighting. Distance weighting is one component of the overall
          similarity, and any features with matching significance levels within
          the neighborhood will be considered partial matches when calculating
          similarity and association.
      num_perms {Long}:
          The number of permutations that will be used to estimate the expected
          similarity and kappa values. A larger number of simulations will
          increase the precision of the estimates but will also increase
          calculation time.99-The analysis will use 99 permutations.199-The
          analysis will use 199
          permutations.499-The analysis will use 499 permutations. This is the
          default.999-The analysis will use 999 permutations.9999-The analysis
          will use 9,999 permutations.
      weighting_method {String}:
          Specifies how similarity weights between significance level categories
          will be defined. Similarity weights are numbers between 0 and 1 that
          define the categories of one result that are expected to match the
          categories of the other result. A value of 1 indicates that the
          categories will be considered exactly the same, and a value of 0
          indicates that the categories will be considered completely different.
          Values between 0 and 1 indicate degrees of partial similarity between
          the categories. For example, 99% significant hot spots can be
          considered perfectly similar to other 99% hot spots, partially similar
          to 95% hot spots, and completely dissimilar to 99% cold
          spots.FUZZY-Similarity weights will be fuzzy (nonbinary) and
          determined by
          the closeness of significance levels. For example, 99% significant hot
          spots will be perfectly similar to other 99% significant hot spots
          (weight = 1), but they will be partially similar to 95% significant
          hot spots (weight=0.71) and 90% significant hot spots (weight = 0.55).
          The weight between 95% significant and 90% significant is 0.78. All
          hot spots will be completely dissimilar to all cold spots and
          nonsignificant features (weight = 0). This is the
          default.EXACT_MATCH-Features must have the same significance level to
          be
          considered similar. For example, 99% significant hot spots will be
          considered completely dissimilar to 95% and 90% significant hot
          spots.ABOVE_90-Features that are 90%, 95%, and 99% significant hot
          spots
          will be considered perfectly similar to each other, and all features
          that are 90%, 95%, and 99% significant cold spots will be considered
          perfectly similar to each other. This option treats all features at or
          above 90% significance as being the same (statistically significant)
          and all features below 90% confidence as being the same
          (nonsignificant). This option is recommended when the hot spot
          analyses were performed at a 90% significance level.ABOVE_95-Features
          that are 95% and 99% significant hot (or cold) spots
          will be considered perfectly similar, and features that are 95% and
          99% significant cold spots will be considered perfectly similar. For
          example, 90% significant hot and cold spots will be considered
          completely dissimilar to higher significance levels. This option
          treats all features at or above 95% confidence as being the same
          (statistically significant) and all features below 95% confidence as
          being the same (nonsignificant). This option is recommended when the
          hot spot analyses were performed at a 95% significance
          level.ABOVE_99-Only features that are 99% significant hot (or cold)
          spots
          will be considered perfectly similar to each other. This option treats
          all features below 99% significance as being nonsignificant. This
          option is recommended when the hot spot analyses were performed at a
          99% significance level.CUSTOM-Custom similarity weights provided in
          the similarity_weights
          parameter will be used.TABLE-Similarity weights between significance
          levels will be defined
          by an input table. Provide the table in the in_weights_table
          parameter.REVERSE-The default fuzzy weights will be used, but hot
          spots of the
          first hot spot result will be considered similar to the cold spots of
          the second hot spot result. For example, 99% significant hot spots in
          one result will be considered perfectly similar to 99% cold spots in
          the other result and partially similar to 95% and 90% cold spots in
          the other result. This option is recommended when the hot spot
          analysis variables have a negative relationship. For example, you can
          measure how closely hot spots of infant mortality correspond to cold
          spots of healthcare access.
      similarity_weights {Value Table}:
          The custom similarity weights between significance level categories.
          The weights are values between 0 and 1 and indicate how similar to
          consider the two categories. A value of 0 indicates the categories are
          completely dissimilar, a value of 1 indicates the values are perfectly
          similar, and values between 0 and 1 indicate the categories are
          partially similar.
      in_weights_table {Table View}:
          The table containing custom similarity weights for each
          combination of hot spot significance level categories. The table must
          contain,, andfields. Provide the significance level categories of the
          pair (thefield values of the input layers) in the category fields and
          the similarity weight between them in the weight field. If a
          combination is not provided in the table, the weight for the
          combination is assumed to be 0. CATEGORY1CATEGORY2WEIGHTGi_Bin
      exclude_nonsig_features {Boolean}:
          Specifies whether pairs of features will be excluded from the
          comparisons if both hot spot results are nonsignificant. If excluded,
          conditional similarity and kappa values will be calculated that
          compare only the statistically significant hot and cold spots.
          Excluding features is recommended when you are interested only in
          whether the hot and cold spots of the input layers align, not whether
          the nonsignificant areas align, such as comparing whether hot and cold
          spots of median income correspond to hot and cold spots of food
          access.EXCLUDE-Nonsignificant features will be excluded, and the
          comparisons
          will be conditional on statistically significant hot and cold
          spots.NO_EXCLUDE-Nonsignificant features will be included. This is the
          default.If any significance level categories are assigned a similarity
          weight
          of 1 to the nonsignificant category (indicating that the category will
          be treated the same as the nonsignificant category), features with
          that category will also be excluded from comparisons if they are
          paired with another nonsignificant feature.

     OUTPUTS:
      out_features (Feature Class):
          The output feature class that will contain the local measures of
          similarity and association.

        """