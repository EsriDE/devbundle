# Generated documentation for module arcpy.stpm


class CurveFitForecast(object):
    """
    Forecasts the values of each location of a space-time cube using curve fitting.
    """

    @property
    def description(self) -> str:
        return """

        CurveFitForecast_stpm(in_cube, analysis_variable, output_features, {output_cube}, {number_of_time_steps_to_forecast}, {curve_type}, {number_for_validation}, {outlier_option}, {level_of_confidence}, {maximum_number_of_outliers})

        Forecasts the values of each location of a space-time cube using curve
        fitting.

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
      curve_type {String}:
          Specifies the curve type that will be used to forecast the values of
          the input space-time cube.LINEAR-The time series increases or
          decreases linearly over
          time.PARABOLIC-The time series follows a parabola or quadratic curve
          over
          time.EXPONENTIAL-The time series increases or decreases exponentially
          over
          time.GOMPERTZ-The time series increases or decreases following the
          shape of
          an S over time.AUTO_DETECT-All four curve types are run for each
          location and the
          model is provided the smallest Validation RMSE. If no time slices are
          excluded for validation, the model with the smallest Forecast RMSE is
          used. This is the default.
      number_for_validation {Long}:
          The number of time steps at the end of each time series to exclude for
          validation. The default value is 10 percent (rounded down) of the
          number of input time steps, and this value cannot be larger than 25
          percent of the number of time steps. Provide the value 0 to not
          exclude any time steps.
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

     OUTPUTS:
      output_features (Feature Class):
          The output feature class of all locations in the space-time cube with
          forecasted values stored as fields. The layer displays the forecast
          for the final time step and contains pop-ups charts showing the time
          series and forecasts for each location.
      output_cube {File}:
          A new space-time cube (.nc file) containing the values of the input
          space-time cube with the forecasted time steps appended. The Visualize
          Space Time Cube in 3D tool can be used to see all of the observed and
          forecasted values simultaneously.

        """