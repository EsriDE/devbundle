# Generated documentation for module arcpy.ia.Functions


class DimensionalMovingStatistics(object):
    """
    Calculates statistics over a moving window on multidimensional data along a specified dimension.
    """

    @property
    def description(self) -> str:
        return """

        DimensionalMovingStatistics_ia(in_raster, {dimension}, {backward_window}, {forward_window}, {nodata_handling}, {statistics_type}, {percentile_value}, {percentile_interpolation_type}, {circular_wrap_value})

        Calculates statistics over a moving window on multidimensional data
        along a specified dimension.

     INPUTS:
      in_raster (Raster Layer):
          The input raster can only be a multidimensional raster in Cloud Raster
          Format (.crf file).
      dimension {String}:
          The name of the dimension along which the window will move.The default
          value is the first dimension other than x,y found in the
          input multidimensional raster.
      backward_window {Long}:
          The value of how many slices before or above to be included in the
          defined window. The value must be a positive integer from 1 to 100.
          The default value is 1.The unit of this parameter is slice.
      forward_window {Long}:
          The value of how many slices after or below to be included in the
          defined window. The value must be a positive integer from 1 to 100.
          The default value is 1.The unit of this parameter is slice.
      nodata_handling {String}:
          Specifies how NoData values will be handled by the statistic
          calculation.DATA-NoData values in the value input will be ignored in
          the results
          of the defined window that they fall within. This is the
          default.NODATA-Output values will be NoData if any NoData values are
          found in
          the input within the defined window.FILL_NODATA-NoData cell values
          will be replaced using the selected
          statistic on the values within the defined window.
      statistics_type {String}:
          Specifies the statistic type to be calculated.MEAN-The mean (average
          value) of the cells in the defined window will
          be calculated. This is the default.CIRCULAR_MEAN-The mean for angles
          or other cyclic quantities-such as
          compass direction in degrees, daytimes, or fractional parts of real
          numbers-will be calculated. When this statistics type is selected, use
          the circular_wrap_value parameter to designate a wrap
          value.MAJORITY-The majority (value that occurs most often) of the
          cells in
          the defined window will be identified.MAXIMUM-The maximum (largest
          value) of the cells in the defined window
          will be identified.MEDIAN-The median of the cells in the defined
          window will be
          identified.MINIMUM-The minimum (smallest value) of the cells in the
          defined
          window will be identified.PERCENTILE-A percentile of the cells in the
          defined window will be
          calculated. The 90th percentile is calculated by default. When this
          statistics type is selected, use the percentile_value and
          percentile_interpolation_type parameters to designate the percentile
          to calculate and choose the interpolation type to use, respectively.
      percentile_value {Double}:
          The percentile value that will be calculated. The default is 90, for
          the 90th percentile.The value can range from 0 to 100. The 0th
          percentile is essentially
          equivalent to the minimum statistic, and the 100th percentile is
          equivalent to the maximum statistic. A value of 50 will produce
          essentially the same result as the median statistic.This parameter is
          only supported if the statistics_type parameter is
          set to PERCENTILE. If any other statistic type is specified, this
          parameter will be ignored.
      percentile_interpolation_type {String}:
          Specifies the method of interpolation that will be used when the
          percentile value falls between two cell values.This parameter is only
          supported if the statistics_type parameter is
          set to MEDIAN or PERCENTILE. If any other statistic type is specified,
          this parameter will be ignored.AUTO_DETECT-If the input raster is of
          integer pixel type, the NEAREST
          method will be used. If the input raster is of float pixel type, the
          LINEAR method will be used.NEAREST-The nearest available value to the
          percentile will be used. In
          this case, the output pixel type will be the same as that of the input
          raster.LINEAR-The weighted average of the two surrounding values from
          the
          percentile will be used. In this case, the output pixel type will be
          floating point.
      circular_wrap_value {Double}:
          The value that will be used to convert a linear value to the range of
          a given circular mean. Its value must be positive. The default value
          is 360 degrees.This parameter is only supported if the statistics_type
          parameter is
          set to CIRCULAR_MEAN. If any other statistic type is specified, this
          parameter will be ignored.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster can only be a multidimensional raster in Cloud
          Raster Format (.crf file).

        """