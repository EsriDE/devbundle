# Generated documentation for module arcpy.stats


class ColocationAnalysis(object):
    """
    Measures local patterns of spatial association, or colocation, between two categories of point features using the colocation quotient statistic.
    """

    @property
    def description(self) -> str:
        return """

        ColocationAnalysis_stats(input_type, in_features_of_interest, output_features, {field_of_interest}, {time_field_of_interest}, {category_of_interest}, {input_feature_for_comparison}, {field_for_comparison}, {time_field_for_comparison}, {category_for_comparison}, {neighborhood_type}, {number_of_neighbors}, {distance_band}, {weights_matrix_file}, {temporal_relationship_type}, {time_step_interval}, {number_of_permutations}, {local_weighting_scheme}, {output_table})

        Measures local patterns of spatial association, or colocation, between
        two categories of point features using the colocation quotient
        statistic.

     INPUTS:
      input_type (String):
          Specifies whether the in_features_of_interest parameter values will
          come from the same dataset with specified categories, different
          datasets with specified categories, or different datasets that will be
          treated as their own category (for example, one dataset with all
          points representing cheetahs and a second dataset in which all points
          represent gazelles).SINGLE_DATASET-The categories to be analyzed exist
          in a field in a
          single dataset.TWO_DATASETS-The categories to be analyzed exist in
          fields of separate
          datasets.DATASETS_WITHOUT_CATEGORIES-Two separate datasets
          representing two
          categories will be analyzed.
      in_features_of_interest (Feature Layer):
          The feature class containing points with representative categories.
      field_of_interest {Field}:
          The field containing the category or categories to be analyzed.
      time_field_of_interest {Field}:
          A date field with an optional time stamp for each feature to analyze
          points using a space-time window. Features near each other in space
          and time will be considered neighbors and will be analyzed together.
      category_of_interest {String}:
          The base category for the analysis. The tool will identify, for each
          category_of_interest value, the degree to which the base category is
          attracted to or colocated with the neighboring_category parameter
          value.
      input_feature_for_comparison {Feature Layer}:
          The input feature class containing the points with the categories that
          will be compared.
      field_for_comparison {Field}:
          The field from the input_feature_for_comparison parameter containing
          the category to be compared.
      time_field_for_comparison {Field}:
          A date field with a time stamp for each feature to analyze your points
          using a space-time window. Features near each other in space and time
          will be considered neighbors and will be analyzed together.
      category_for_comparison {String}:
          The neighboring category for the analysis. The tool will identify the
          degree to which the category_of_interest parameter value is attracted
          to or isolated from the category_for_comparison value.
      neighborhood_type {String}:
          Specifies how the spatial relationships among features will be
          defined.DISTANCE_BAND-Each feature will be analyzed within the context
          of
          neighboring features. Neighboring features inside the specified
          critical distance specified by the distance_band parameter receive a
          weight of one and exert influence on computations for the target
          feature. Neighboring features outside the critical distance receive a
          weight of zero and have no influence on a target feature's
          computations.K_NEAREST_NEIGHBORS-The closest k features will be
          included in the
          analysis as neighbors. The number of neighbors is specified by the
          number_of_neighbors parameter. The neighbor's influence in the
          analysis is weighted based on the distance to the farthest neighbor.
          This is the default.GET_SPATIAL_WEIGHTS_FROM_FILE-When SINGLE_DATASET
          is used as the
          input_type, spatial relationships will be defined by a specified
          spatial weights matrix file. The neighbor's influence in the analysis
          is weighted based on the distance to the farthest neighbor. The path
          to the spatial weights file is specified by the weights_matrix_file
          parameter.
      number_of_neighbors {Long}:
          The number of neighbors around each feature that will be used to test
          for local relationships between categories. If no value is provided,
          the default of 8 is used. The provided value must be large enough to
          detect the relationships between features but small enough to still
          identify local patterns.
      distance_band {Linear Unit}:
          The neighborhood size is a constant or fixed distance for each
          feature. All features within this distance will be used to test for
          local relationships between categories. If no value is provided, the
          distance used will be the average distance at which each feature has
          at least eight neighbors.
      weights_matrix_file {File}:
          The path to a file containing weights that define spatial, and
          potentially temporal, relationships among features.
      temporal_relationship_type {String}:
          Specifies how temporal relationships among features will be
          defined.BEFORE-The time window will extend back in time for each of
          the
          in_features_of_interest values. Neighboring features must have a
          date/time stamp that occurs before the date/time stamp of the feature
          of interest to be included in the analysis. This is the
          default.AFTER-The time window will extend forward in time for each of
          the
          in_features_of_interest values. Neighboring features must have a
          date/time stamp that occurs after the date/time stamp of the feature
          of interest to be included in the analysis.SPAN-The time window will
          extend both back and forward in time for
          each of the in_features_of_interest values. Neighboring features that
          have a date/time stamp that occurs within the time_step_interval value
          before or after the date/time stamp of the feature of interest will be
          included in the analysis. For example, if the time_step_interval
          parameter is set to 1 week, the window will look 1 week before and 1
          week after the target feature.
      time_step_interval {Time Unit}:
          An integer and unit of measurement representing the number of time
          units composing the time window.
      number_of_permutations {Long}:
          The number of permutations that will be used to create a reference
          distribution. Choosing the number of permutations is a balance between
          precision and increased processing time. Choose your preference of
          speed versus precision. More robust and precise results take longer to
          calculate.99-The analysis will use 99 permutations. With 99
          permutations, the
          smallest possible pseudo p-value is 0.02 and all other pseudo p-values
          will be multiples of this value. This is the default.199-The analysis
          will use 199 permutations. With 199 permutations, the
          smallest possible pseudo p-value is 0.01 and all other pseudo p-values
          will be even multiples of this value.499-The analysis will use 499
          permutations. With 499 permutations, the
          smallest possible pseudo p-value is 0.004 and all other pseudo
          p-values will be even multiples of this value.999-The analysis will
          use 999 permutations. With 999 permutations, the
          smallest possible pseudo p-value is 0.002 and all other pseudo
          p-values will be even multiples of this value.9999-The analysis will
          use 9,999 permutations. With 9,999
          permutations, the smallest possible pseudo p-value is 0.0002 and all
          other pseudo p-values will be even multiples of this value.
      local_weighting_scheme {String}:
          Specifies the kernel type that will be used to provide the spatial
          weighting. The kernel defines how each feature is related to other
          features within its neighborhood.BISQUARE-Features will be weighted
          based on the distance to the
          farthest neighbor or the edge of the distance band, and a weight of 0
          will be assigned to any feature outside the neighborhood specified.
          GAUSSIAN-Features will be weighted based on the distance to
          the farthest neighbor or the edge of the distance band but drop off
          more quickly than theoption. A weight of 0 will be assigned to any
          feature outside the neighborhood specified. This is the default.
          BisquareNONE-No weighting scheme will be applied, and all features
          within the
          neighborhood will be given a weight of 1 and contribute equally. All
          features outside the neighborhood will be given a weight of 0.

     OUTPUTS:
      output_features (Feature Class):
          The output feature class containing all the in_features parameter
          values with fields representing the local colocation quotient scores
          and p-values.
      output_table {Table}:
          A table that includes the global colocation quotients between
          all the categories in theparameter and all the categories in
          theparameter. This table can help you determine the local categories
          to analyze. Field of InterestField Containing Neighboring
          Category        Ifis used as theparameter value, global colocation
          quotients
          will be calculated for each dataset and between each dataset.
          Datasets without categoriesInput Type

        """