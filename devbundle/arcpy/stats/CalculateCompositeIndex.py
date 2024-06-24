# Generated documentation for module arcpy.stats


class CalculateCompositeIndex(object):
    """
    Combines multiple numeric variables to create a single index.
    """

    @property
    def description(self) -> str:
        return """

        CalculateCompositeIndex_stats(in_table, in_variables;in_variables..., {append_to_input}, {out_table}, {index_preset}, {preprocessing}, {pre_threshold_scaling}, {pre_custom_zscore;pre_custom_zscore...}, {pre_min_max;pre_min_max...}, {pre_thresholds;pre_thresholds...}, {index_method}, {index_weights;index_weights...}, {out_index_name}, {out_index_reverse}, {post_min_max;post_min_max...}, {post_reclass;post_reclass...}, {post_num_classes}, {post_custom_classes;post_custom_classes...})

        Combines multiple numeric variables to create a single index.

     INPUTS:
      in_table (Table View):
          The table or features containing the variables that will be combined
          into the index.
      in_variables (Value Table):
          A list of numeric fields representing the variables that will be
          combined as an index. The Reverse Direction column reverses the values
          of the variables. This means that the feature or record that
          originally had the highest value will have the lowest value, and vice
          versa. Values will be reversed after scaling.
      append_to_input {Boolean}:
          Specifies whether the results will be appended to the input data or
          provided as an output feature class or table.APPEND_TO_INPUT-The
          results will be appended to the input data. This
          option modifies the input data.NEW_FEATURES-An output feature class
          or table will be created
          containing the results. This is the default.
      index_preset {String}:
          Specifies the workflow that will be used when creating the index. The
          options represent common index creation workflows; each option sets
          default values for the preprocessing and index_method
          parameters.MEAN_SCALED-An index will be created by scaling the input
          variables
          between 0 and 1 and averaging the scaled values. This method is useful
          for creating an index that is easy to interpret. The shape of the
          distribution and outliers in the input variables will impact the
          index. This is the default.MEAN_PCTL-An index will be created by
          scaling the ranks of the input
          variables between 0 and 1 and averaging the scaled ranks. This option
          is useful when the rankings of the variable values are more important
          than the differences between values. The shape of the distribution and
          outliers in the input variables will not impact the
          index.GEOMEAN_SCALED-An index will be created by scaling the input
          variables
          between 0 and 1 and calculating the geometric average of the scaled
          values. High values will not cancel low values, so this option is
          useful for creating an index in which higher index values will occur
          only when there are high values in multiple variables.
          SUM_FLAGSPCTL-An index will be created that counts the number
          of input variables with values greater than or equal to the
          90percentile. This method is useful for identifying locations that may
          be considered the most extreme or the most in need.
          thCUSTOM-An index will be created using customized variable scaling
          and
          combination options.
      preprocessing {String}:
          Specifies the method that will be used to convert the input variables
          to a common scale.MINMAX-Variables will be scaled between 0 and 1
          using the minimum and
          maximum values of each variable. This is the default.CUST_MINMAX-
          Variables will be scaled between 0 and 1 using the
          possible minimum and possible maximum values for each variable,
          specified by the pre_min_max parameter. This method has many uses,
          including specifying the minimum and maximum based on a benchmark, on
          a reference statistic, or on theoretical values. For example, if ozone
          recordings for a single day range between 5 and 27 parts per million
          (ppm), you can use the theoretical minimum and maximum based on prior
          observation and domain expertise to ensure that the index can be
          compared across multiple daysPERCENTILE-Variables will be converted to
          percentiles between 0 and 1
          by calculating the percent of data values less than the data value.
          This option is useful when you want to ignore absolute differences
          between the data values, such as with outliers or skewed
          distributions.RANK-Variables will be ranked. The smallest value is
          assigned rank
          value 1, the next value is assigned rank value 2, and so on. Ties are
          assigned the average of their ranks.ZSCORE-Each variable will be
          standardized by subtracting the mean
          value and dividing by the standard deviation (called a z-score). The
          z-score is the number of standard deviations above or below the mean
          value. This option is useful when the means of the variables are
          important comparison points. Values above the mean will receive
          positive z-scores, and values below the mean will receive negative
          z-scores.CUST_ZSCORE-Each variable will be standardized by subtracting
          a custom
          mean value and dividing by a custom standard deviation. Provide the
          custom values in the pre_custom_zscore parameter. This option is
          useful when the means and standard deviations of the variables are
          known from previous research.BINARY-Variables will be identified when
          they are above or below a
          defined threshold. The resulting field contains binary (0 or 1) values
          indicating whether the threshold was exceeded. You can also use the
          pre_threshold_scaling parameter to scale the input variable values
          before defining the threshold, and use the pre_thresholds parameter to
          specify the threshold values. This method is useful when the values of
          the variables are less important than whether they exceed a particular
          threshold, such as a safety limit of a pollutant.RAW-The original
          values of the variables will be used. Use this method
          only when all variables are measured on a comparable scale, such as
          percentages or rates, or when the variables have been standardized
          before using this tool.
      pre_threshold_scaling {String}:
          Specifies the method that will be used to convert the input variables
          to a common scale prior to setting
          thresholds.THRESHOLD_MINMAX-Variables between 0 and 1 will be scaled
          using the
          minimum and maximum values of each
          variable.THRESHOLD_CUST_MINMAX-Variables between 0 and 1 will be
          scaled using
          the possible minimum and possible maximum values for each
          variable.THRESHOLD_PERCENTILE-Variables will be converted to
          percentiles
          between 0 and 1.THRESHOLD_ZSCORE-Each variable will be standardized by
          subtracting the
          mean value and dividing by the standard
          deviation.THRESHOLD_CUST_ZSCORE-Each variable will be standardized by
          subtracting a custom mean value and dividing by a custom standard
          deviation.THRESHOLD_RAW-The values of the variables will be used
          without
          change. This is the default.
      pre_custom_zscore {Value Table}:
          The custom mean value and custom standard deviation that will
          be used when standardizing each input variable. For each variable,
          provide the custom mean in thecolumn and the custom standard deviation
          in thecolumn. MeanStandard Deviation
      pre_min_max {Value Table}:
          The possible minimum and maximum values that will be used in the units
          of the variables. Each variable will be scaled between 0 and 1 based
          on the possible minimum and maximum values.
      pre_thresholds {Value Table}:
          The threshold that determines whether a feature will be flagged.
          Specify the value in the units of the scaled variables and specify
          whether values above or below the threshold value will be flagged.
      index_method {String}:
          Specifies the method that will be used to combine the scaled variables
          into a single value.SUM-The values will be added.MEAN-The arithmetic
          (additive) mean of
          the values will be calculated.
          This is the default.PRODUCT-The values will be multiplied. All scaled
          values must be
          greater than or equal to zero.GEOMETRIC_MEAN-The geometric
          (multiplicative) mean of the values will
          be calculated. All scaled values must be greater than or equal to
          zero.You cannot multiply or calculate a geometric mean when any
          variables
          are scaled using z-scores, because z-scores always contain negative
          values.
      index_weights {Value Table}:
          The weights that will set the relative influence of each input
          variable on the index. Each weight has a default value of 1, meaning
          that each variable has equal contribution. Increase or decrease the
          weights to reflect the relative importance of the variables. For
          example, if a variable is twice as important as another, use a weight
          value of 2. Using weight values larger than 1 while multiplying to
          combine scaled values can result in indices with very large values.
      out_index_name {String}:
          The name of the index. The value is used in the visualization of the
          outputs, such as field aliases and chart labels. The value is not used
          when the output (or appended input) is a shapefile.
      out_index_reverse {Boolean}:
          Specifies whether the output index values will be reversed in
          direction (for example, to treat high index values as low
          values).REVERSE-The index values will be reversed in
          direction.NO_REVERSE-
          The index values will not be reversed in direction. This
          is the default.
      post_min_max {Value Table}:
          The minimum and maximum of the output index values. This scaling is
          applied after combining the scaled variables. If no values are
          provided, the output index is not scaled.
      post_reclass {String}:
          Specifies the method that will be used to classify the output index.
          An additional output field will be provided for each selected
          option.EQINTERVAL-Classes will be created by dividing the range of
          values
          into equally sized intervalsQUANTILE-Classes will be created in which
          each class includes an equal
          number of records.STDDEV-Classes will be created corresponding to the
          number of standard
          deviations above and below the average of the index. The resulting
          values will be between -3 and 3.CUST-Class breaks and class values
          will be specified using the
          post_custom_classes parameter.
      post_num_classes {Long}:
          The number of classes that will be used for the equal interval and
          quantile classification methods.
      post_custom_classes {Value Table}:
          The upper bounds and class values for the custom classification
          method. For example, you can use this variable to classify an index
          containing values between 0 and 100 into classes representing low,
          medium, and high values based on custom break values.

     OUTPUTS:
      out_table {Feature Class / Table}:
          The output features or table that will include the results.

        """