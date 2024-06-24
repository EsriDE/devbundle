# Generated documentation for module arcpy.sa.Functions


class CellStatistics(object):
    """
    Calculates a per-cell statistic from multiple rasters.
    """

    @property
    def description(self) -> str:
        return """

        CellStatistics_sa(in_rasters_or_constants;in_rasters_or_constants..., {statistics_type}, {ignore_nodata}, {process_as_multiband}, {percentile_value}, {percentile_interpolation_type})

        Calculates a per-cell statistic from multiple rasters.

     INPUTS:
      in_rasters_or_constants (Composite Geodataset):
          A list of input rasters for which a statistical operation will be
          calculated for each cell in the analysis window.A number can be used
          as an input; however, the cell size and extent
          must first be set in the environment.If the processing_as_multiband
          parameter is set to MULTI_BAND, all
          multiband inputs should have an equal number of bands.
      statistics_type {String}:
          Specifies the statistic type to be calculated.MEAN-The mean (average)
          of the inputs will be calculated. This is the
          default.MAJORITY-The majority (value that occurs most often) of the
          inputs
          will be determined.MAXIMUM-The maximum (largest value) of the inputs
          will be determined.MEDIAN-The median of the inputs will be
          calculated.MINIMUM-The minimum (smallest value) of the inputs will be
          determined.MINORITY-The minority (value that occurs least often) of
          the inputs
          will be determined.PERCENTILE-The percentile of the inputs will be
          calculated. The 90th
          percentile is calculated by default. You can specify other values
          (from 0 to 100) using the percentile_value parameter.RANGE-The range
          (difference between largest and smallest value) of the
          inputs will be calculated.STD-The standard deviation of the inputs
          will be calculated.SUM-The sum (total of all values) of the inputs
          will be calculated.VARIETY-The variety (number of unique values) of
          the inputs will be
          calculated.The default statistic type is MEAN.
      ignore_nodata {Boolean}:
          Specifies whether NoData values will be ignored by the statistic
          calculation.DATA-At the processing cell location, if any of the input
          rasters has
          NoData, that NoData value will be ignored. The statistics will be
          computed by only considering the cells with valid data. This is the
          default.NODATA-If the processing cell location for any of the input
          rasters is
          NoData, the output for that cell will be NoData.
      process_as_multiband {Boolean}:
          Specifies how the input multiband raster bands will be
          processed.SINGLE_BAND-Each band from a multiband raster input will be
          processed
          separately as a single band raster. This is the
          default.MULTI_BAND-Each multiband raster input will be processed as a
          multiband raster. The operation will be performed for each band from
          one input using the corresponding band number from the other inputs.
      percentile_value {Double}:
          The percentile value that will be calculated. The default is 90,
          indicating the 90th percentile.The value can range from 0 to 100. The
          0th percentile is essentially
          equivalent to the minimum statistic, and the 100th percentile is
          equivalent to the maximum statistic. A value of 50 will produce
          essentially the same result as the median statistic.This parameter is
          only supported if the statistics_type parameter is
          set to PERCENTILE.
      percentile_interpolation_type {String}:
          Specifies the method of interpolation that will be used when the
          specified percentile value is between two input cell
          values.AUTO_DETECT-If the input rasters are of integer pixel type, the
          NEAREST method will be used. If the input rasters are of floating
          point pixel type, the LINEAR method will be used. This is the
          default.NEAREST-The nearest available value to the desired percentile
          will be
          used. In this case, the output pixel type will be the same as that of
          the input rasters.LINEAR-The weighted average of the two surrounding
          values from the
          percentile will be used. In this case, the output pixel type will be
          floating point.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.For each cell, the value is determined by applying
          the specified
          statistic type to the input rasters at that location.

        """