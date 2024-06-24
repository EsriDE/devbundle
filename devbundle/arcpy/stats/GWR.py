# Generated documentation for module arcpy.stats


class GWR(object):
    """
    Performs Geographically Weighted Regression, which is a local form of linear regression that is used to model spatially varying relationships.
    """

    @property
    def description(self) -> str:
        return """

        GWR_stats(in_features, dependent_variable, model_type, explanatory_variables;explanatory_variables..., output_features, neighborhood_type, neighborhood_selection_method, {minimum_number_of_neighbors}, {maximum_number_of_neighbors}, {minimum_search_distance}, {maximum_search_distance}, {number_of_neighbors_increment}, {search_distance_increment}, {number_of_increments}, {number_of_neighbors}, {distance_band}, {prediction_locations}, {explanatory_variables_to_match;explanatory_variables_to_match...}, {output_predicted_features}, {robust_prediction}, {local_weighting_scheme}, {coefficient_raster_workspace}, {scale})

        Performs Geographically Weighted Regression, which is a local form of
        linear regression that is used to model spatially varying
        relationships.

     INPUTS:
      in_features (Feature Layer):
          The feature class containing the dependent and explanatory variables.
      dependent_variable (Field):
          The numeric field containing the observed values that will be modeled.
      model_type (String):
          Specifies the type of data that will be modeled.CONTINUOUS-The
          dependent_variable value is continuous. The Gaussian
          model will be used, and the tool will perform ordinary least squares
          regression.BINARY-The dependent_variable value represents presence or
          absence.
          This can be either conventional 1s and 0s or continuous data that has
          been coded based on a threshold value. The Logistic regression model
          will be used.COUNT-The dependent_variable value is discrete and
          represents events,
          such as crime counts, disease incidents, or traffic accidents. The
          Poisson regression model will be used.
      explanatory_variables (Field):
          A list of fields representing independent explanatory variables in the
          regression model.
      neighborhood_type (String):
          Specifies whether the neighborhood used is constructed as a fixed
          distance or allowed to vary in spatial extent depending on the density
          of the features.NUMBER_OF_NEIGHBORS-The neighborhood size is a
          function of a
          specified number of neighbors included in calculations for each
          feature. Where features are dense, the spatial extent of the
          neighborhood is smaller; where features are sparse, the spatial extent
          of the neighborhood is larger.DISTANCE_BAND-The neighborhood size is a
          constant or fixed distance
          for each feature.
      neighborhood_selection_method (String):
          Specifies how the neighborhood size will be determined. The
          neighborhood selected with the GOLDEN_SEARCH and MANUAL_INTERVALS
          options is based on minimizing the AICc value.GOLDEN_SEARCH-The tool
          will identify an optimal distance or number of
          neighbors based on the characteristics of the data using the golden
          section search method.MANUAL_INTERVALS-The neighborhoods tested will
          be defined by the
          values specified in the minimum_number_of_neighbors and
          number_of_neighbors_increment parameters when NUMBER_OF_NEIGHBORS is
          chosen for the neighborhood_type parameter, or the
          minimum_search_distance and search_distance_increment parameters when
          DISTANCE_BAND is chosen for the neighborhood_type parameter, as well
          as the number_of_increments parameter.USER_DEFINED-The neighborhood
          size will be specified by either the
          number_of_neighbors parameter or the distance_band parameter.
      minimum_number_of_neighbors {Long}:
          The minimum number of neighbors each feature will include in its
          calculations. It is recommended that you use at least 30 neighbors.
      maximum_number_of_neighbors {Long}:
          The maximum number of neighbors (up to 1000) each feature will include
          in its calculations.
      minimum_search_distance {Linear Unit}:
          The minimum neighborhood search distance. It is recommended that you
          use a distance at which each feature has at least 30 neighbors.
      maximum_search_distance {Linear Unit}:
          The maximum neighborhood search distance. If a distance results in
          features with more than 1000 neighbors, the tool will use the first
          1000 in calculations for the target feature.
      number_of_neighbors_increment {Long}:
          The number of neighbors by which manual intervals will increase for
          each neighborhood test.
      search_distance_increment {Linear Unit}:
          The distance by which manual intervals will increase for each
          neighborhood test.
      number_of_increments {Long}:
          The number of neighborhood sizes that will be tested starting with the
          minimum_number_of_neighbors or minimum_search_distance parameter
          value.
      number_of_neighbors {Long}:
          The closest number of neighbors (up to 1000) that will be considered
          for each feature. The number must be an integer between 2 and 1000.
      distance_band {Linear Unit}:
          The spatial extent of the neighborhood.
      prediction_locations {Feature Layer}:
          A feature class containing features representing locations where
          estimates will be computed. Each feature in this dataset should
          contain values for all the explanatory variables specified. The
          dependent variable for these features will be estimated using the
          model calibrated for the input feature class data. To be predicted,
          these feature locations should be within the same study area as the
          in_features parameter value or be close (within the extent plus 15
          percent). A feature class containing features representing
          locations
          where estimates will be computed. Each feature in this dataset should
          contain values for all the explanatory variables specified. The
          dependent variable for these features will be estimated using the
          model calibrated for the input feature class data. To be predicted,
          these feature locations should be within the same study area as
          theparameter value or be close (within the extent plus 15 percent).
          Input Features
      explanatory_variables_to_match {Value Table}:
          The explanatory variables from the prediction_locations parameter that
          match corresponding explanatory variables from the in_features
          parameter. [["LandCover2000", "LandCover2010"], ["Income",
          "PerCapitaIncome"]] are examples.
      robust_prediction {Boolean}:
          Specifies the features that will be used in prediction
          calculations.ROBUST-Features with values more than three standard
          deviations from
          the mean (value outliers) and features with weights of 0 (spatial
          outliers) will be excluded from prediction calculations but will
          receive predictions in the output feature class. This is the
          default.NON_ROBUST-All features will be used in prediction
          calculations
      local_weighting_scheme {String}:
          Specifies the kernel type that will be used to provide the spatial
          weighting in the model. The kernel defines how each feature is related
          to other features within its neighborhood.BISQUARE-A weight of 0 will
          be assigned to any feature outside the
          neighborhood specified. This is the default.GAUSSIAN-All features will
          receive weights, but weights become
          exponentially smaller the farther away they are from the target
          feature.
      coefficient_raster_workspace {Workspace}:
          The workspace where the coefficient rasters will be created. When this
          workspace is provided, rasters are created for the intercept and every
          explanatory variable. This parameter is only available with a Desktop
          Advanced license.
      scale {Boolean}:
          Specifies whether the values of the explanatory and dependent
          variables will be scaled to have mean zero and standard deviation one
          before fitting the model.SCALE_DATA-The values of the variables will
          be scaled. The results
          will contain scaled and unscaled versions of the explanatory variable
          coefficients.NO_SCALE_DATA-The values of the variables will not be
          scaled. All
          coefficients will be unscaled and in original data units.

     OUTPUTS:
      output_features (Feature Class):
          The new feature class containing the dependent variable estimates and
          residuals.
      output_predicted_features {Feature Class}:
          The output feature class that will receive dependent variable
          estimates for each prediction_location value.

        """