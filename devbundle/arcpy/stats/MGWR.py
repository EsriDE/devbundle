# Generated documentation for module arcpy.stats


class MGWR(object):
    """
    Performs Multiscale Geographically Weighted Regression (MGWR), which is a local form of linear regression that models spatially varying relationships.
    """

    @property
    def description(self) -> str:
        return """

        MGWR_stats(in_features, dependent_variable, model_type, explanatory_variables;explanatory_variables..., output_features, neighborhood_type, neighborhood_selection_method, {minimum_number_of_neighbors}, {maximum_number_of_neighbors}, {distance_unit}, {minimum_search_distance}, {maximum_search_distance}, {number_of_neighbors_increment}, {search_distance_increment}, {number_of_increments}, {number_of_neighbors}, {distance_band}, {number_of_neighbors_golden;number_of_neighbors_golden...}, {number_of_neighbors_manual;number_of_neighbors_manual...}, {number_of_neighbors_defined;number_of_neighbors_defined...}, {distance_golden;distance_golden...}, {distance_manual;distance_manual...}, {distance_defined;distance_defined...}, {prediction_locations}, {explanatory_variables_to_match;explanatory_variables_to_match...}, {output_predicted_features}, {robust_prediction}, {local_weighting_scheme}, {output_table}, {coefficient_raster_workspace}, {scale}, {number_of_neighbors_gradient;number_of_neighbors_gradient...}, {distance_gradient;distance_gradient...})

        Performs Multiscale Geographically Weighted Regression (MGWR), which
        is a local form of linear regression that models spatially varying
        relationships.

     INPUTS:
      in_features (Feature Layer):
          The feature class containing the dependent and explanatory variables.
      dependent_variable (Field):
          The numeric field containing the observed values that will be modeled.
      model_type (String):
          Specifies the regression model based on the values of the
          dependent variable. Currently, only continuous data is supported, and
          the parameter is hidden in thepane. Do not use categorical, count, or
          binary dependent variables. GeoprocessingCONTINUOUS-The
          dependent variable represents continuous values. This
          is the default.
      explanatory_variables (Field):
          A list of fields that will be used as independent explanatory
          variables in the regression model.
      neighborhood_type (String):
          Specifies whether the neighborhood will be a fixed distance or allowed
          to vary spatially depending on the density of the
          features.NUMBER_OF_NEIGHBORS-The neighborhood size will be a
          specified number
          of closest neighbors for each feature. Where features are dense, the
          spatial extent of the neighborhood will be smaller; where features are
          sparse, the spatial extent of the neighborhood will be
          larger.DISTANCE_BAND-The neighborhood size will be a constant or fixed
          distance for each feature.
      neighborhood_selection_method (String):
          Specifies how the neighborhood size will be
          determined.GOLDEN_SEARCH-An optimal distance or number of neighbors
          will be
          identified by minimizing the AICc value using the Golden Search
          algorithm. This option takes the longest time to calculate, especially
          for large or high-dimensional datasets.GRADIENT_SEARCH-An optimal
          distance or number of neighbors will be
          identified by minimizing the AICc value using the gradient-based
          optimization algorithm. This option runs the fastest and requires
          significantly less memory usage than Golden Search.MANUAL_INTERVALS-A
          distance or number of neighbors will be identified
          by testing a range of values and determining the value with the
          smallest AICc. If the neighborhood_type parameter is set to
          DISTANCE_BAND, the minimum value of this range is provided by the
          minimum_search_distance parameter. The minimum value is then
          incremented by the value specified in the search_distance_increment
          parameter. This is repeated the number of times specified by the
          number_of_increments parameter. If the neighborhood_type parameter is
          set to NUMBER_OF_NEIGHBORS, the minimum value, increment size, and
          number of increments are provided by the minimum_number_of_neighbors,
          number_of_neighbors_increment, and number_of_increments parameters,
          respectively.USER_DEFINED-The neighborhood size will be specified by
          either the
          number_of_neighbors parameter value or the distance_band parameter
          value.
      minimum_number_of_neighbors {Long}:
          The minimum number of neighbors that each feature will include in its
          calculation. It is recommended that you use at least 30 neighbors.
      maximum_number_of_neighbors {Long}:
          The maximum number of neighbors that each feature will include in its
          calculations.
      distance_unit {String}:
          Specifies the unit of distance that will be used to measure the
          distances between features.FEETINT-Distances will be measured in
          international
          feet.MILESINT-Distances will be measured in statute
          miles.FEET-Distances will be measured in US survey
          feet.METERS-Distances will be measured in meters.KILOMETERS-Distances
          will be measured in kilometers.MILES-Distances will be measured in US
          survey miles.
      minimum_search_distance {Double}:
          The minimum search distance that will be applied to every explanatory
          variable. It is recommended that you provide a minimum distance that
          includes at least 30 neighbors for each feature.
      maximum_search_distance {Double}:
          The maximum neighborhood search distance that will be applied to all
          variables.
      number_of_neighbors_increment {Long}:
          The number of neighbors by which manual intervals will increase for
          each neighborhood test.
      search_distance_increment {Double}:
          The distance by which manual intervals will increase for each
          neighborhood test.
      number_of_increments {Long}:
          The number of neighborhood sizes to test when using manual intervals.
          The first neighborhood size is the value of the
          minimum_number_of_neighbors or minimum_search_distance parameter.
      number_of_neighbors {Long}:
          The number of neighbors that will be used for the user-defined
          neighborhood type.
      distance_band {Double}:
          The size of the distance band that will be used for the user-defined
          neighborhood type. All features within this distance will be included
          as neighbors in the local models.
      number_of_neighbors_golden {Value Table}:
          The customized Golden Search options for individual explanatory
          variables. For each explanatory variable to be customized, provide the
          variable, the minimum number of neighbors, and the maximum number of
          neighbors in the columns.
      number_of_neighbors_manual {Value Table}:
          The customized manual intervals options for individual explanatory
          variables. For each explanatory variable to be customized, provide the
          minimum number of neighbors, number of neighbors increment, and number
          of increments in the columns.
      number_of_neighbors_defined {Value Table}:
          The customized user-defined options for individual explanatory
          variables. For each explanatory variable to be customized, provide the
          number of neighbors.
      distance_golden {Value Table}:
          The customized Golden Search options for individual explanatory
          variables. For each explanatory variable to be customized, provide the
          variable, the minimum search distance, and the maximum search distance
          in the columns.
      distance_manual {Value Table}:
          The customized manual intervals options for individual explanatory
          variables. For each variable to be customized, provide the variable,
          the minimum search distance, search distance increments, and number of
          increments in the columns.
      distance_defined {Value Table}:
          The customized user-defined options for individual explanatory
          variables. For each variable to be customized, provide the variable
          and the distance band in the columns.
      prediction_locations {Feature Layer}:
          A feature class with the locations where estimates will be computed.
          Each feature in this dataset should contain a value for every
          explanatory variables specified. The dependent variable for these
          features will be estimated using the model calibrated for the input
          feature class data. These feature locations should be close to (within
          115 percent of the extent) or within the same study area as the input
          features.
      explanatory_variables_to_match {Value Table}:
          The explanatory variables from the prediction locations that match
          corresponding explanatory variables from the input features.
      robust_prediction {Boolean}:
          Specifies the features that will be used in the prediction
          calculations.ROBUST-Features with values greater than three standard
          deviations
          from the mean (value outliers) and features with weights of 0 (spatial
          outliers) will be excluded from the prediction calculations but will
          receive predictions in the output feature class. This is the
          default.NON_ROBUST-Every feature will be used in the prediction
          calculations.
      local_weighting_scheme {String}:
          Specifies the kernel type that will be used to provide the spatial
          weighting in the model. The kernel defines how each feature is related
          to other features within its neighborhood.BISQUARE-A weight of zero
          will be assigned to any feature outside the
          neighborhood specified. This is the default.GAUSSIAN-All features will
          receive weights, but weights become
          exponentially smaller the farther away they are from the target
          feature.
      coefficient_raster_workspace {Workspace}:
          The workspace where the coefficient rasters will be created. When this
          workspace is provided, rasters are created for the intercept and every
          explanatory variable. This parameter is only available with a Desktop
          Advanced license. If a directory is provided, the rasters will be TIFF
          (.tif) raster type.
      scale {Boolean}:
          Specifies whether the values of the explanatory and dependent
          variables will be scaled to have mean zero and standard deviation one
          prior to fitting the model.SCALE_DATA-The values of the variables will
          be scaled. The results
          will contain scaled and unscaled versions of the explanatory variable
          coefficients.NO_SCALE_DATA-The values of the variables will not be
          scaled. All
          coefficients will be unscaled and in original data units.
      number_of_neighbors_gradient {Value Table}:
          The customized Gradient Search options for individual explanatory
          variables. For each explanatory variable to be customized, provide the
          variable, the minimum number of neighbors, and the maximum number of
          neighbors in the columns.
      distance_gradient {Value Table}:
          The customized Gradient Search options for individual explanatory
          variables. For each explanatory variable to be customized, provide the
          variable, the minimum search distance, and the maximum search distance
          in the columns.

     OUTPUTS:
      output_features (Feature Class):
          The new feature class containing the coefficients, residuals, and
          significance levels of the MGWR model.
      output_predicted_features {Feature Class}:
          The output feature class that will receive dependent variable
          estimates for every prediction location.
      output_table {Table}:
          A table containing the output statistics of the MGWR model. A bar
          chart of estimated bandwidths or numbers of neighbors will be included
          with the output.

        """