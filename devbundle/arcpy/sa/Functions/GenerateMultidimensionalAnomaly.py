# Generated documentation for module arcpy.sa.Functions


class GenerateMultidimensionalAnomaly(object):
    """
    Computes the anomaly for each slice in an existing multidimensional raster to generate a new multidimensional raster.
    """

    @property
    def description(self) -> str:
        return """

        GenerateMultidimensionalAnomaly_sa(in_multidimensional_raster, {variables;variables...}, {method}, {calculation_interval}, {ignore_nodata}, {reference_mean_raster})

        Computes the anomaly for each slice in an existing multidimensional
        raster to generate a new multidimensional raster.

     INPUTS:
      in_multidimensional_raster (Raster Dataset / Mosaic Dataset / Raster Layer / Mosaic Layer / Image Service):
          The input multidimensional raster dataset.
      variables {String}:
          The variable or variables for which anomalies will be calculated. If
          no variable is specified, all variables with a time dimension will be
          analyzed.
      method {String}:
          Specifies the method that will be used to calculate the
          anomaly.DIFFERENCE_FROM_MEAN-The difference between a pixel's value
          and the
          mean of that pixel's values across slices defined by the interval will
          be calculated. This is the default.PERCENT_DIFFERENCE_FROM_MEAN-The
          percent difference between a pixel's
          value and the mean of that pixel's values across slices defined by the
          interval will be calculated.PERCENT_OF_MEAN-The percent of the mean
          will be calculated.Z_SCORE-The z-score for each pixel will be
          calculated. A z-score of 0
          indicates the pixel's value is identical to the mean. A z-score of 1
          indicates the pixel's value is 1 standard deviation from the mean. If
          a z-score is 2, the pixel's value is 2 standard deviations from the
          mean, and so on.DIFFERENCE_FROM_MEDIAN-The difference between a
          pixel's value and the
          mathematical median of that pixel's values across slices defined by
          the interval will be calculated.PERCENT_DIFFERENCE_FROM_MEDIAN-The
          percent difference between a
          pixel's value and the mathematical median of that pixel's values
          across slices defined by the interval will be
          calculated.PERCENT_OF_MEDIAN-The percent of the mathematical median
          will be
          calculated.
      calculation_interval {String}:
          Specifies the temporal interval that will be used to calculate the
          mean.ALL-The mean is calculated across all slices for each
          pixel.YEARLY-The
          yearly mean is calculated for each pixel.RECURRING_MONTHLY-The monthly
          mean is calculated for each pixel.RECURRING_WEEKLY-The weekly mean is
          calculated for each pixel.RECURRING_DAILY-The daily mean is calculated
          for each pixel.HOURLY-The hourly mean is calculated for each
          pixel.EXTERNAL_RASTER-An existing raster dataset that contains the
          mean or
          median value for each pixel is referenced.
      ignore_nodata {Boolean}:
          Specifies whether NoData values will be ignored in the
          analysis.DATA-The analysis will include all valid pixels along a given
          dimension and ignore NoData pixels. This is the default.NODATA-The
          analysis will result in NoData if there are NoData values
          for the pixels along the given dimension.
      reference_mean_raster {Raster Layer / Raster Dataset / Mosaic Layer / Mosaic Dataset}:
          The reference raster dataset that contains a previously calculated
          mean for each pixel. The anomalies will be calculated in comparison to
          this mean.

     OUTPUTS:
      out_multidimensional_raster (Raster Dataset):
          The output Cloud Raster Format (CRF) multidimensional raster dataset.

        """