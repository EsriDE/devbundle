# Generated documentation for module arcpy.geoai


class ForecastUsingTimeSeriesModel(object):
    """
    Predicts the values of each location of a space-time cube using a deep learning-based time series forecasting model that has been trained using the Train Time Series Forecasting Model tool.
    """

    @property
    def description(self) -> str:
        return """

        ForecastUsingTimeSeriesModel_geoai(in_cube, in_model_definition, out_features, number_of_timesteps_to_forecast, {match_explanatory_variables;match_explanatory_variables...}, {out_cube}, {outlier_option}, {level_of_confidence}, {maximum_number_of_outliers})

        Predicts the values of each location of a space-time cube using a deep
        learning-based time series forecasting model that has been trained
        using the Train Time Series Forecasting Model tool.

     INPUTS:
      in_cube (File):
          The netCDF cube containing the variable that will be used to forecast
          to future time steps. This file must have an .nc file extension and
          must have been created using the Create Space Time Cube By Aggregating
          Points, Create Space Time Cube From Defined Locations, or Create Space
          Time Cube From Multidimensional Raster Layer tool.
      in_model_definition (File):
          The trained deep learning model file (.dlpk or .emd) that will be used
          to make the predictions. The model can be trained using the Train Time
          Series Forecasting Model tool.
      number_of_timesteps_to_forecast (Long):
          A positive integer specifying the number of time steps that will be
          used to forecast the analysis variable. The default value is 2. This
          value cannot be larger than 50 percent of the total time steps in the
          input space-time cube for one-step forecasting, and it cannot be
          larger than 50 percent of the sequence_length parameter value in the
          Train Time Series Forecasting Model tool for multistep forecasting.
      match_explanatory_variables {Value Table}:
          The mapping of field names from the prediction set to the training
          set. Use this parameter if the field names of the training and
          prediction sets are different. The values are the field names in the
          prediction dataset that match the field names in the input time series
          data.
      outlier_option {String}:
          Specifies whether statistically significant time series outliers will
          be identified.NONE-Outliers will not be identified. This is the
          default.IDENTIFY-Outliers will be identified using the Generalized ESD
          test.
      level_of_confidence {String}:
          Specifies the confidence level that will be used for the test for time
          series outliers.90%-The confidence level for the test will be 90
          percent. This is the
          default.95%-The confidence level for the test will be 95
          percent.99%-The confidence level for the test will be 99 percent.
      maximum_number_of_outliers {Long}:
          The maximum number of time steps that can be declared outliers for
          each location. The default value corresponds to 5 percent (rounded
          down) of the number of time steps of the input space-time cube (a
          value of at least 1 will always be used). The value cannot exceed 20
          percent of the number of time steps.

     OUTPUTS:
      out_features (Feature Class):
          The output feature class of all locations in the space-time cube with
          forecasted values stored as fields. The layer displays the forecast
          for the final time step and contains pop-up charts showing the time
          series and forecasts for each location.
      out_cube {File}:
          An output space-time cube (.nc file) containing the values of the
          input space-time cube with the forecasted time steps appended. Use the
          Visualize Space Time Cube in 3D tool to see all of the observed and
          forecasted values simultaneously.

        """