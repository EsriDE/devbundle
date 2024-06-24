# Generated documentation for module arcpy.stats


class LocalBivariateRelationships(object):
    """
    Analyzes two variables for statistically significant relationships using local entropy. Each feature is classified into one of six categories based on the type of relationship. The output can be used to visualize areas where the variables are related and explore how their relationship changes across the study area.
    """

    @property
    def description(self) -> str:
        return """

        LocalBivariateRelationships_stats(in_features, dependent_variable, explanatory_variable, output_features, {number_of_neighbors}, {number_of_permutations}, {enable_local_scatterplot_popups}, {level_of_confidence}, {apply_false_discovery_rate_fdr_correction}, {scaling_factor})

        Analyzes two variables for statistically significant relationships
        using local entropy. Each feature is classified into one of six
        categories based on the type of relationship. The output can be used
        to visualize areas where the variables are related and explore how
        their relationship changes across the study area.

     INPUTS:
      in_features (Feature Layer):
          The feature class containing fields representing the
          dependent_variable and explanatory_variable values.
      dependent_variable (Field):
          The numeric field representing the values of the dependent variable.
          When categorizing the relationships, the explanatory_variable value is
          used to predict the dependent_variable value.
      explanatory_variable (Field):
          The numeric field representing the values of the explanatory variable.
          When categorizing the relationships, the explanatory_variable value is
          used to predict the dependent_variable value.
      number_of_neighbors {Long}:
          The number of neighbors around each feature (including the feature)
          that will be used to test for a local relationship between the
          variables. The number of neighbors must be between 30 and 1,000, and
          the default is 30. The provided value should be large enough to detect
          the relationship between features, but small enough to still identify
          local patterns.
      number_of_permutations {Long}:
          Specifies the number of permutations that will be used to calculate
          the pseudo p-value for each feature. Choosing a number of permutations
          is a balance between precision in the pseudo p-value and increased
          processing time.99-With 99 permutations, the smallest possible pseudo
          p-value is 0.01,
          and all other pseudo p-values will be multiples of this value.199-With
          199 permutations, the smallest possible pseudo p-value is
          0.005, and all other pseudo p-values will be multiples of this value.
          This is the default.499-With 499 permutations, the smallest possible
          pseudo p-value is
          0.002, and all other pseudo p-values will be multiples of this
          value.999-With 999 permutations, the smallest possible pseudo p-value
          is
          0.001, and all other pseudo p-values will be multiples of this value.
      enable_local_scatterplot_popups {Boolean}:
          Specifies whether scatterplot pop-ups will be generated for each
          output feature. Each scatterplot displays the values of the
          explanatory (horizontal axis) and dependent (vertical axis) variables
          in the local neighborhood along with a fitted line or curve
          visualizing the form of the relationship. Scatterplot charts are not
          supported for shapefile outputs.CREATE_POPUP-Local scatterplot pop-ups
          will be generated for each
          feature in the dataset. This is the default.NO_POPUP-Local scatterplot
          pop-ups will not be generated.
      level_of_confidence {String}:
          Specifies a confidence level of the hypothesis test for significant
          relationships.90%-The confidence level is 90 percent. This is the
          default.95%-The
          confidence level is 95 percent.99%-The confidence level is 99 percent.
      apply_false_discovery_rate_fdr_correction {Boolean}:
          Specifies whether False Discover Rate (FDR) correction will be applied
          to the pseudo p-values.APPLY_FDR-Statistical significance will be
          based on the FDR
          correction. This is the default.NO_FDR-Statistical significance will
          be based on the pseudo p-value.
      scaling_factor {Double}:
          The level of sensitivity to subtle relationships between the
          variables. Larger values (closer to one) can detect relatively weak
          relationships, while smaller values (closer to zero) will only detect
          strong relationships. Smaller values are also more robust to outliers.
          The value must be between 0.01 and 1, and the default is 0.5.

     OUTPUTS:
      output_features (Feature Class):
          The output feature class containing all input features with fields
          representing the dependent_variable value, explanatory_variable value,
          entropy score, pseudo p-value, level of significance, type of
          categorized relationship, and diagnostics related to the
          categorization.

        """