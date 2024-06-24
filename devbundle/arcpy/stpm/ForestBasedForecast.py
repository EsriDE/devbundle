# Generated documentation for module arcpy.stpm


class ForestBasedForecast(object):
    """
    Forecasts the values of each location of a space-time cube using an adaptation of the random forest algorithm, which is a supervised machine learning method developed by Leo Breiman and Adele Cutler. The forest regression model is trained using time windows on each location of the space-time cube.
    """

    @property
    def description(self) -> str:
        return """

        ForestBasedForecast_stpm(in_cube, analysis_variable, output_features, {output_cube}, {number_of_time_steps_to_forecast}, {time_window}, {number_for_validation}, {number_of_trees}, {minimum_leaf_size}, {maximum_depth}, {sample_size}, {forecast_approach}, {outlier_option}, {level_of_confidence}, {maximum_number_of_outliers}, {other_variables;other_variables...}, {importance_threshold}, {output_importance_table}, {model_scale}, {cluster_variable})

        Forecasts the values of each location of a space-time cube using an
        adaptation of  the random forest algorithm, which is a supervised
        machine learning method developed by Leo Breiman and Adele Cutler. The
        forest regression model is trained using time windows on each location
        of the space-time cube.

     INPUTS:
      in_cube (File):
          The netCDF cube containing the variable to forecast to future time
          steps. This file must have an .nc file extension and must have been
          created using the Create Space Time Cube By Aggregating Points, Create
          Space Time Cube From Defined Locations, or Create Space Time Cube From
          Multidimensional Raster Layer tool.
      analysis_variable (String):
          The numeric variable in the netCDF file that will be forecasted to
          future time steps.
      number_of_time_steps_to_forecast {Long}:
          A positive integer specifying the number of time steps to forecast.
          This value cannot be larger than 50 percent of the total time steps in
          the input space-time cube. The default value is one time step.
      time_window {Long}:
          The number of previous time steps that will be used when training the
          model. If the data displays seasonality (repeating cycles), provide
          the number of time steps corresponding to one season. This value
          cannot be larger than one-third of the number of time steps in the
          input space-time cube. When using individual location model scale, if
          no value is provided, a time window is estimated for each location
          using a spectral density function. When using entire cube or time
          series cluster model scales, if no value is provided, one-fourth of
          the number of time steps will be used.
      number_for_validation {Long}:
          The number of time steps at the end of each time series to exclude for
          validation. The default value is 10 percent (rounded down) of the
          number of input time steps, and this value cannot be larger than 25
          percent of the number of time steps. Provide the value 0 to not
          exclude any time steps.
      number_of_trees {Long}:
          The number of trees that will be created in the forest model. More
          trees generally result in more accurate model prediction, but the
          model will take longer to calculate. The default number of trees is
          100, and the value must be at least 1 and not greater than 1,000.
      minimum_leaf_size {Long}:
          The minimum number of observations that are required to keep a leaf
          (that is, the terminal node on a tree without further splits). For
          very large data, increasing this number will decrease the run time of
          the tool.
      maximum_depth {Long}:
          The maximum number of splits that will be made down a tree. Using a
          large maximum depth, more splits will be created, which may increase
          the chance of overfitting the model. If no value is provided, a value
          will be identified by the tool based on the number of trees created by
          the model and the size of the time step window.
      sample_size {Long}:
          The percent of training data that will be used to fit the forecast
          model. The training data consists of associated explanatory and
          dependent variables constructed using time windows. All remaining
          training data will be used to optimize the parameters of the forecast
          model. The default is 100 percent.
      forecast_approach {String}:
          Specifies how the explanatory and dependent variables will be
          represented when training the forest model at each location.To train
          the forest model that will be used to forecast, sets of
          explanatory and dependent variables must be created using time
          windows. Use this parameter to specify whether these variables will be
          linearly detrended and whether the dependent variable will be
          represented by its raw value or by the residual of a linear regression
          model. This linear regression model uses all time steps within a time
          window as explanatory variables and uses the following time step as
          the dependent variable. The residual is calculated by subtracting the
          predicted value based on linear regression from the raw value of the
          dependent variable. If any variables are provided in
          theparameter or iforis
          specified for theparameter, theoption will be the only available
          forecast approach. Other VariablesEntire cubeTime series
          clusterModel ScaleValueVALUE-Values within the time window will not
          be detrended and the
          dependent variable will be represented by its raw value. If any other
          variables are provided or if the model scale is not individual
          location, this will be the only available forecast approach and will
          be the default.VALUE_DETREND-Values within the time window will be
          linearly
          detrended, and the dependent variable will be represented by its
          detrended value. This is the default.RESIDUAL-Values within the time
          window will not be detrended, and the
          dependent variable will be represented by the residual of a linear
          regression model using the values within the time window as
          explanatory variables.RESIDUAL_DETREND-Values within the time window
          will be linearly
          detrended, and the dependent variable will be represented by the
          residual of a linear regression model using the detrended values
          within the time window as explanatory variables.
      outlier_option {String}:
          Specifies whether statistically significant time series outliers will
          be identified.NONE-Outliers will not be identified. This is the
          default.IDENTIFY-Outliers will be identified using the Generalized ESD
          test.
      level_of_confidence {String}:
          Specifies the confidence level for the test for time series
          outliers.90%-The confidence level for the test is 90 percent. This is
          the
          default.95%-The confidence level for the test is 95 percent.99%-The
          confidence level for the test is 99 percent.
      maximum_number_of_outliers {Long}:
          The maximum number of time steps that can be declared outliers for
          each location. The default value corresponds to 5 percent (rounded
          down) of the number of time steps of the input space-time cube (a
          value of at least 1 will always be used). This value cannot exceed 20
          percent of the number of time steps.
      other_variables {String}:
          Other variables of the input space-time cube that will be used as
          explanatory variables to improve the forecasts.
      importance_threshold {Long}:
          The percent of factors deemed most important for forecasting the
          analysis variable. For example, if the value is 20, the top 20 percent
          of factors for each location will be included in the importance table.
          Each variable (the analysis variable and each explanatory variable) is
          represented as a factor once for each time step in the time step
          window, so the number of factors at each location is the length of the
          time window multiplied by the number of variables. The number of
          factors is multiplied by the importance threshold to determine the
          number of important factors for each forecast model. The default is
          10, and the value must be an integer between 1 and 100.
      model_scale {String}:
          Specifies the scale that will be used to estimate the forecast and
          validation models.INDIVIDUAL_LOCATION-A different forecast model and
          validation model
          will be estimated for each location. This is the default.ENTIRE_CUBE-A
          single forecast model and validation model will be
          estimated using all locations as training data.TIME_SERIES_CLUSTER-A
          forecast and validation model will be estimated
          for each cluster of a time series clustering result. Provide the
          variable with time series clustering results in the cluster_variable
          parameter.
      cluster_variable {String}:
          The variable that will be used to group the locations of the space-
          time cube into regions, and different forecast and validation models
          will be estimated for each region. The variable must have time series
          clustering results to be used. The cluster variable can be any
          variable of the space-time cube including the analysis variable.

     OUTPUTS:
      output_features (Feature Class):
          The output feature class of all locations in the space-time cube with
          forecasted values stored as fields. The layer displays the forecast
          for the final time step and contains pop-up charts showing the time
          series, forecasts, and 90 percent confidence bounds for each location.
      output_cube {File}:
          A new space-time cube (.nc file) containing the values of the input
          space-time cube with the forecasted time steps appended. The Visualize
          Space Time Cube in 3D tool can be used to see all of the observed and
          forecasted values simultaneously.
      output_importance_table {Table}:
          The output table that will contain the most important factors at each
          location. For individual location model scale, each important factor
          at each location of the space-time cube will be represented as a row
          in the table with fields containing the name of the variable and
          associated time lag. For entire cube and time series cluster model
          scales, all important factors in the entire cube or cluster model will
          be represented by a row .The table will include a chart displaying the
          most important factors across all locations separated by time lag. The
          chart allows you to visualize lagged effects between the explanatory
          variables and the variable being forecasted.

        """