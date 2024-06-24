# Generated documentation for module arcpy.ia.Functions


class PredictUsingTrendRaster(object):
    """
    Computes a forecasted multidimensional raster using the output trend raster from the Generate Trend Raster tool.
    """

    @property
    def description(self) -> str:
        return """

        PredictUsingTrendRaster_ia(in_multidimensional_raster, {variables;variables...}, {dimension_def}, {dimension_values;dimension_values...}, {start}, {end}, {interval_value}, {interval_unit})

        Computes a forecasted multidimensional raster using the output trend
        raster from the Generate Trend Raster tool.

     INPUTS:
      in_multidimensional_raster (Raster Dataset / Mosaic Dataset / Raster Layer / Mosaic Layer / Image Service):
          The input multidimensional trend raster from the Generate Trend Raster
          tool.
      variables {String}:
          The variable or variables that will be predicted in the analysis. If
          no variables are specified, all variables will be used.
      dimension_def {String}:
          Specifies the method used to provide prediction dimension values.
          BY_VALUE-The prediction will be calculated for a single
          dimension value or a list of dimension values defined by theparameter
          (dimension_values in Python). This is the default. ValuesFor
          example, you want to predict yearly precipitation for the years
          2050, 2100, and 2150. BY_INTERVAL-The prediction will be
          calculated for an interval
          of the dimension defined by a start and an end value. For
          example, you want to predict yearly precipitation for every year
          between 2050 and 2150.
      dimension_values {String}:
          The dimension value or values to be used in the prediction.The format
          of the time, depth, and height values must match the format
          of the dimension values used to generate the trend raster. If the
          trend raster was generated for the StdTime dimension, the format would
          be YYYY-MM-DDTHH:MM:SS, for example 2050-01-01T00:00:00. Multiple
          values are separated with a semicolon.This parameter is required when
          the dimension_def parameter is set to
          BY_VALUE.
      start {String}:
          The start date, height, or depth of the dimension interval to be used
          in the prediction.
      end {String}:
          The end date, height, or depth of the dimension interval to be used in
          the prediction.
      interval_value {Double}:
          The number of steps between two dimension values to be included in the
          prediction. The default value is 1.For example, to predict temperature
          values every five years, use a
          value of 5.
      interval_unit {String}:
          Specifies the unit that will be used for the interval value. This
          parameter only applies when the dimension of analysis is a time
          dimension.HOURS-The prediction will be calculated for each hour in the
          range of
          time described by the start, end, and interval_value
          parameters.DAYS-The prediction will be calculated for each day in the
          range of
          time described by the start, end, and interval_value
          parameters.WEEKS-The prediction will be calculated for each week in
          the range of
          time described by the start, end, and interval_value
          parameters.MONTHS-The prediction will be calculated for each month in
          the range
          of time described by the start, end, and interval_value
          parameters.YEARS-The prediction will be calculated for each year in
          the range of
          time described by the start, end, and interval_value parameters.

     OUTPUTS:
      out_multidimensional_raster (Raster Dataset):
          The output Cloud Raster Format (CRF) multidimensional raster dataset.

        """