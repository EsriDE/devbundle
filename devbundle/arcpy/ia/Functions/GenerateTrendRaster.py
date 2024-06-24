# Generated documentation for module arcpy.ia.Functions


class GenerateTrendRaster(object):
    """
    Estimates the trend for each pixel along a dimension for one or more variables in a multidimensional raster.
    """

    @property
    def description(self) -> str:
        return """

        GenerateTrendRaster_ia(in_multidimensional_raster, dimension, {variables;variables...}, {line_type}, {frequency}, {ignore_nodata}, {cycle_length}, {cycle_unit}, {rmse}, {r2}, {slope_p_value}, {seasonal_period})

        Estimates the trend for each pixel along a dimension for one or more
        variables in a multidimensional raster.

     INPUTS:
      in_multidimensional_raster (Raster Dataset / Mosaic Dataset / Raster Layer / Mosaic Layer / Image Service):
          The input multidimensional raster dataset.
      dimension (String):
          The dimension along which a trend will be extracted for the variable
          or variables selected in the analysis.
      variables {String}:
          The variable or variables for which trends will be calculated. If no
          variable is specified, the first variable in the multidimensional
          raster will be analyzed.
      line_type {String}:
          Specifies the type of trend analysis to perform to pixel values along
          a dimension.LINEAR-Variable pixel values will be fitted along a linear
          trend line.
          This is the default.POLYNOMIAL-Variable pixel values will be fitted
          along a second order
          polynomial trend line.HARMONIC-Variable pixel values will be fitted
          along a harmonic trend
          line.MANN-KENDALL-Variable pixel values will be evaluated using the
          Mann-
          Kendall trend test.SEASONAL-KENDALL-Variable pixel values will be
          evaluated using the
          Seasonal-Kendall trend test.
      frequency {Long}:
          The frequency or the polynomial order number to use in the trend
          fitting. If the trend type is polynomial, this parameter specifies the
          polynomial order. If the trend type is harmonic, this parameter
          specifies the number of models to use to fit the trend.This parameter
          is only included in the trend analysis when the
          dimension being analyzed is time.If the line_type parameter is
          HARMONIC, the default value is 1,
          meaning a first order harmonic curve is used to fit the model.If the
          line_type parameter is POLYNOMIAL, the default value is 2, or
          second order polynomial.
      ignore_nodata {Boolean}:
          Specifies whether NoData values will be ignored in the
          analysis.DATA-The analysis will include all valid pixels along a given
          dimension and ignore NoData pixels. This is the default.NODATA-The
          analysis will result in NoData if there are NoData values
          for the pixels along the given dimension.
      cycle_length {Double}:
          The length of periodic variation to model. This parameter is required
          when line_type is set to HARMONIC. For example, leaf greenness often
          has one strong cycle of variation in a single year, so the cycle
          length is 1 year. Hourly temperature data has one strong cycle of
          variation throughout a single day, so the cycle length is 1 day.The
          default length is 1 year for data that varies on an annual cycle.
      cycle_unit {String}:
          Specifies the time unit to be used for the length of a harmonic
          cycle.DAYS-The unit for the length of the harmonic cycle is
          days.YEARS-The
          unit for the length of the harmonic cycle is years. This is
          the default.
      rmse {Boolean}:
          Specifies whether the root mean square error (RMSE) of the trend fit
          line will be calculated.RMSE-The RMSE will be calculated. This is the
          default.NO_RMSE-The RMSE
          will not be calculated.
      r2 {Boolean}:
          Specifies whether the R-squared goodness-of-fit statistic for the
          trend fit line will be calculated.R2-The R-squared value will be
          calculated.NO_R2-The R-squared value
          will not be calculated. This is the default.
      slope_p_value {Boolean}:
          Specifies whether the p-value statistic for the slope coefficient of
          the trend line will be calculated.SLOPEPVALUE-The p-value will be
          calculated.NO_SLOPEPVALUE-The p-value
          will not be calculated. This is the
          default.
      seasonal_period {String}:
          Specifies the time unit to be used for the length of a seasonal period
          when performing the Seasonal-Kendall test.DAYS-The unit for the length
          of the seasonal period is days. This is
          the default.MONTHS-The unit for the length of the seasonal period is
          months.

     OUTPUTS:
      out_multidimensional_raster (Raster Dataset):
          The output Cloud Raster Format (CRF) multidimensional raster dataset.

        """