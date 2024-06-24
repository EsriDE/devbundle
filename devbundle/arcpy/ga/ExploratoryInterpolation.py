# Generated documentation for module arcpy.ga


class ExploratoryInterpolation(object):
    """
    Generates various interpolation results from input point features and a field. The interpolation results are then compared and ranked using customizable criteria based on cross validation statistics.
    """

    @property
    def description(self) -> str:
        return """

        ExploratoryInterpolation_ga(in_features, value_field, out_cv_table, {out_geostat_layer}, {interp_methods;interp_methods...}, {comparison_method}, {criterion}, {criteria_hierarchy;criteria_hierarchy...}, {weighted_criteria;weighted_criteria...}, {exclusion_criteria;exclusion_criteria...})

        Generates various interpolation results from input point features and
        a field. The interpolation results are then compared and ranked using
        customizable criteria based on cross validation statistics.

     INPUTS:
      in_features (Feature Layer):
          The input points representing locations of points to be interpolated.
      value_field (Field):
          The field containing the values to be interpolated.
      interp_methods {String}:
          Specifies the interpolation methods that will be performed on the
          input features and value field. For each method specified, 1 to 5
          interpolation results will be generated. By default, all methods will
          be generated except inverse distance weighting, radial basis
          functions, and global polynomial (because these methods cannot create
          standard errors of predictions). By default, 11 interpolation results
          will be generated. If all options are specified, 20 interpolation
          results will be generated.SIMPLE_KRIGING-Four simple kriging results
          will be generated: default,
          optimized, trend removal, and transformation with trend
          removal.ORDINARY_KRIGING-Two ordinary kriging results will be
          generated:
          default and optimized.UNIVERSAL_KRIGING-Two universal kriging results
          will be generated:
          default and optimized.EBK-Two empirical Bayesian kriging results will
          be generated: default
          and advanced.KERNEL_INTERPOLATION-One default kernel (local
          polynomial)
          interpolation result will be generated.IDW-Two inverse distance
          weighting results will be generated: default
          and optimized.RBF-Five radial basis functions results will be
          generated, one for
          each of the five kernel functions.GPI-Two global polynomial
          interpolation results will be generated:
          linear (first order) and quadratic (second order) trend.
      comparison_method {String}:
          Specifies the method that will be used to compare and rank the
          interpolation results.SINGLE-A single cross validation statistic will
          be used to compare and
          rank results, such as highest prediction accuracy or lowest bias. The
          criterion from the criterion parameter is used.SORTING-Hierarchical
          sorting will be used to compare results. Multiple
          criteria are specified in priority order (highest priority first) in
          the criteria_hierarchy parameter. The interpolation results are ranked
          by the first criterion, and any ties are broken by the second
          criterion. Ties in the second criterion are broken by the third
          criterion, and so on. Cross validation statistics are continuous
          values and generally do not have exact ties, so tolerances (percent or
          absolute) can be specified to create ties in each of the
          criteria.AVERAGE_RANK-The weighted average rank of multiple criteria
          will be
          used to compare results. Multiple criteria and associated weights are
          specified in the weighted_criteria parameter. The interpolation
          results are ranked independently by each of the criteria, and a
          weighted average of the ranks is used to determine the final ranks.
          Criteria with larger weights will have more influence on the final
          ranks, so weights can be used to indicate preference for certain
          criteria over others.
      criterion {String}:
          Specifies the criterion that will be used to rank the interpolation
          results.ACCURACY-Results will be ranked by lowest root mean square
          error. This
          option measures how closely the cross validation predictions match the
          true values, on average. This is the default.BIAS-Results will be
          ranked by mean error closest to zero. This option
          measures how much the cross validation predictions overpredict or
          underpredict the true values, on average. Interpolation results with
          positive mean errors systematically overpredict the true values
          (positive bias), and results with negative mean errors systematically
          underpredict the true values (negative bias).WORST_CASE-Results will
          be ranked by lowest maximum absolute error.
          This option measures only the single least accurate cross validation
          prediction (positive or negative). This is useful when you are most
          concerned about worst-case scenarios rather than the accuracy in
          typical conditions.STANDARD_ERROR-Results will be ranked by root mean
          square
          standardized error closest to one. This option measures how closely
          the variability of the cross validation predictions match the
          estimated standard errors. This is useful if you intend to create
          confidence intervals or margins of error for the
          predictions.PRECISION-Results will be ranked by lowest average
          standard error.
          When creating confidence intervals or margins of error for the
          predicted values, results with higher precision will have narrower
          intervals around the predictions. It does not measure whether the
          standard errors are estimated accurately, only that the standard
          errors are small. When using this option, it is recommended that you
          include minimum and maximum root mean square standardized error values
          as exclusion criteria to ensure that the standard errors are both
          accurate and precise.
      criteria_hierarchy {Value Table}:
          The hierarchy of criteria that will be used for hierarchical sorting
          with tolerances. Provide multiple criteria in priority order with the
          first being most important. The interpolation results are ranked by
          the first criterion, and any ties are broken by the second criterion.
          Ties in the second criterion are broken by the third criterion, and so
          on. Cross validation statistics are continuous values and generally do
          not have exact ties, so tolerances are used to induce ties in the
          criteria. For each row, specify a criterion in the first column, a
          tolerance type (percent or absolute) in the second column, and a
          tolerance value in the third column. If no tolerance value is
          provided, no tolerance will be used; this is most useful for the final
          row so that there will be no ties for the interpolation result with
          highest rank. For each row (level of the hierarchy), the
          following criteria
          are available:        ACCURACY-Results will be ranked by highest
          accuracy.BIAS-Results will
          be ranked by lowest bias.WORST_CASE-Results will be ranked by lowest
          worst-case error.STANDARD_ERROR-Results will be ranked by highest
          standard error
          accuracy.PRECISION-Results will be ranked by highest precision.For
          example, you can specify an ACCURACY value with a 5 percent
          tolerance in the first row and a BIAS value with no tolerance in the
          second row. These options will first rank the interpolation results by
          lowest root mean square error (highest prediction accuracy), and all
          interpolation results whose root mean square error values are within 5
          percent of the most accurate result will be considered ties by
          prediction accuracy. Among the tying results, the result with a mean
          error closest to zero (lowest bias) will receive the highest rank.
      weighted_criteria {Value Table}:
          The multiple criteria with weights that will be used to rank
          interpolation results. For each row, provide a criterion and a weight.
          The interpolation results will be ranked independently by each of the
          criteria, and a weighted average of the ranks will be used to
          determine the final ranks of the interpolation results.
          ACCURACY-Results will be ranked by lowest root mean square
          error.BIAS-Results will be ranked by mean error closest to
          zero.WORST_CASE-Results will be ranked by lowest maximum absolute
          error.STANDARD_ERROR-Results will be ranked by root mean square
          standardized
          error closest to one.PRECISION-Results will be ranked by lowest
          average standard error.
      exclusion_criteria {Value Table}:
          The criteria and associated values that will be used to
          exclude interpolation results from the comparison. Excluded results
          will not receive ranks and will have the value No in thefield of the
          output cross validation table. IncludedMAX_RMSE-Results will be
          excluded if the root mean square error
          exceeds the specified value. The value cannot be negative. This option
          measures prediction accuracy.MAX_WORST_CASE-Results will be excluded
          if the maximum absolute error
          exceeds the specified value. The value cannot be negative. This option
          measures the worst-case error.MAX_STD_RMSE-Results will be excluded if
          the root mean square standard
          error exceeds the specified value. The value must be greater than or
          equal to 1. This option measures standard error
          accuracy.MIN_STD_RMSE-Results will be excluded if the root mean square
          standardized error does not exceed the specified value. The value must
          be between 0 and 1. This option measures standard error
          accuracy.MAX_MEAN_ERROR-Results will be excluded if the mean error
          exceeds the
          specified value. The value cannot be negative. This option measures
          bias.MIN_MEAN_ERROR-Results will be excluded if the mean error does
          not
          exceed the specified value. The value cannot be positive. This option
          measures bias.MAX_ASE-Results will be excluded if the average standard
          square error
          exceeds the specified value. The value cannot be negative. This option
          measures precision.MIN_PERC_ERROR-Results will be excluded if the
          interpolation result is
          not sufficiently more accurate than a baseline nonspatial model that
          predicts the global average value at all locations in the map. This
          relative accuracy is measured by comparing the root mean square error
          value to the standard deviation of the values of the points being
          interpolated, and the root mean square error must be at least the
          specified percent less than the standard deviation to be included in
          the comparison. For example, a value of 10 means that the root mean
          square error must be at least 10 percent lower than the standard
          deviation to be included in the comparison and ranking. The value must
          be between 0 and 100. This option measures prediction accuracy.

     OUTPUTS:
      out_cv_table (Table):
          The output table containing cross validation statistics and
          ranks for each interpolation result. The final ranks of the
          interpolation results are stored in thefield. RANK
      out_geostat_layer {Geostatistical Layer}:
          The output geostatistical layer of the interpolation result
          with highest rank. This interpolation result will have the value 1 in
          thefield of the output cross validation table. If there are ties for
          the interpolation result with highest rank or all results are excluded
          by exclusion criteria, the layer will not be created even if a value
          is provided. Warning messages will be returned by the tool if this
          occurs. RANK

        """