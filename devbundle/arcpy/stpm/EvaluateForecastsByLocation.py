# Generated documentation for module arcpy.stpm


class EvaluateForecastsByLocation(object):
    """
    Selects the most accurate among multiple forecasting results for each location of a space-time cube. This allows you to use multiple tools in the Time Series Forecasting toolset with the same time series data and select the best forecast for each location.
    """

    @property
    def description(self) -> str:
        return """

        EvaluateForecastsByLocation_stpm(in_cubes;in_cubes..., output_features, {output_cube}, {evaluate_using_validation_results})

        Selects the most accurate among multiple forecasting results for each
        location of a space-time cube. This allows you to use multiple tools
        in the Time Series Forecasting toolset with the same time series data
        and select the best forecast for each location.

     INPUTS:
      in_cubes (File):
          The input space-time cubes containing forecasts to be compared. To be
          compared, all forecast cubes must be created from the same original
          time series data.
      evaluate_using_validation_results {Boolean}:
          Specifies whether the forecast method for a location will be
          determined using the smallest Validation RMSE or smallest Forecast
          RMSE.USE_VALIDATION-The forecast method will be determined using the
          smallest Validation RMSE. This is the default.NO_VALIDATION-The
          forecast method will be determined using the
          smallest Forecast RMSE.

     OUTPUTS:
      output_features (Feature Class):
          The new output feature class representing the locations of the space-
          time cube and fields containing the forecast values of the selected
          method at each location. The pop-ups of the features display charts of
          the original time series data and the forecasts of all methods.
      output_cube {File}:
          The output space-time cube (.nc file) containing the original time
          series data with the forecasts of the selected method at each
          location. The Visualize Space Time Cube in 3D tool can be used to view
          the original and forecasted values simultaneously.

        """