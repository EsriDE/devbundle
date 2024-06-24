# Generated documentation for module arcpy.ia.Functions


class TrainRandomTreesRegressionModel(object):
    """
    Models the relationship between explanatory variables (independent variables) and a target dataset (dependent variable).
    """

    @property
    def description(self) -> str:
        return """

        TrainRandomTreesRegressionModel_ia(in_rasters;in_rasters..., in_target_data, out_regression_definition, {target_value_field}, {target_dimension_field}, {raster_dimension}, {out_importance_table}, {max_num_trees}, {max_tree_depth}, {max_samples}, {average_points_per_cell}, {percent_testing}, {out_scatterplots}, {out_sample_features})

        Models the relationship between explanatory variables (independent
        variables) and a target dataset (dependent variable).

     INPUTS:
      in_rasters (Mosaic Dataset / Mosaic Layer / Raster Dataset / Raster Layer / Image Service / String):
          The single-band, multidimensional, or multiband raster datasets, or
          mosaic datasets containing explanatory variables.
      in_target_data (Feature Class / Feature Layer / Raster Dataset / Raster Layer / Mosaic Layer / Image Service):
          The raster or point feature class containing the target variable
          (dependant variable) data.
      target_value_field {Field}:
          The field name of the information to model in the target point feature
          class or raster dataset.
      target_dimension_field {Field}:
          A date field or numeric field in the input point feature class that
          defines the dimension values.
      raster_dimension {String}:
          The dimension name of the input multidimensional raster (explanatory
          variables) that links to the dimension in the target data.
      max_num_trees {Long}:
          The maximum number of trees in the forest. Increasing the number of
          trees will lead to higher accuracy rates, although this improvement
          will level off. The number of trees increases the processing time
          linearly. The default is 50.
      max_tree_depth {Long}:
          The maximum depth of each tree in the forest. Depth determines the
          number of rules each tree can create, resulting in a decision. Trees
          will not grow any deeper than this setting. The default is 30.
      max_samples {Long}:
          The maximum number of samples that will be used for the regression
          analysis. A value that is less than or equal to 0 means that the
          system will use all the samples from the input target raster or point
          feature class to train the regression model. The default value is
          10,000.
      average_points_per_cell {Boolean}:
          Specifies whether the average will be calculated when multiple
          training points fall into one cell. This parameter is applicable only
          when the input target is a point feature class. Unchecked-All
          points will be used when multiple training points fall
          into a single cell. This is the default.Checked-The average value of
          the training points in a cell will be
          calculated.KEEP_ALL_POINTS-All points will be used when multiple
          training points
          fall into a single cell. This is the
          default.AVERAGE_POINTS_PER_CELL-The average value of the training
          points in a
          cell will be calculated.
      percent_testing {Double}:
          The percentage of test points that will be used for error checking.
          The tool checks for three types of errors: errors on training points,
          errors on test points, and errors on test location points. The default
          is 10.

     OUTPUTS:
      out_regression_definition (File):
          A JSON format file with an .ecd extension that contains attribute
          information, statistics, or other information for the classifier.
      out_importance_table {Table}:
          A table containing information describing the importance of each
          explanatory variable used in the model. A larger number indicates the
          corresponding variable is more correlated to the predicted variable
          and will contribute more in prediction. Values range between 0 and 1,
          and the sum of all the values equals 1.
      out_scatterplots {File}:
          The output scatter plots in PDF or HTML format. The output will
          include scatter plots of training data, test data, and location test
          data.
      out_sample_features {Feature Class}:
          The output feature class that will contain target values and predicted
          values for training points, test points, and location test points.

        """