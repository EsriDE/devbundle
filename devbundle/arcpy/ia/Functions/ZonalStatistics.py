# Generated documentation for module arcpy.ia.Functions


class ZonalStatistics(object):
    """
    Summarizes the values of a raster within the zones of another dataset.
    """

    @property
    def description(self) -> str:
        return """

        ZonalStatistics_ia(in_zone_data, zone_field, in_value_raster, {statistics_type}, {ignore_nodata}, {process_as_multidimensional}, {percentile_value}, {percentile_interpolation_type}, {circular_calculation}, {circular_wrap_value})

        Summarizes the values of a raster within the zones of another dataset.

     INPUTS:
      in_zone_data (Composite Geodataset):
          The dataset that defines the zones.The zones can be defined by an
          integer raster or a feature layer.
      zone_field (Field):
          The field that contains the values that define each zone.It can be an
          integer or a string field of the zone dataset.
      in_value_raster (Composite Geodataset):
          The raster that contains the values for which a statistic will be
          calculated.
      statistics_type {String}:
          Specifies the statistic type to be calculated. MEAN-The
          average of all cells in the value raster that belong
          to the same zone as the output cell will be calculated. This
          is the default.MAJORITY-The value that occurs most often for all cells
          in the value
          raster that belong to the same zone as the output cell will be
          calculated.MAJORITY_COUNT-The frequency of all cells that contain the
          majority
          value in the value raster that belong to the same zone as the output
          cell will be calculated.MAJORITY_PERCENT-The percentage of cells that
          contain the majority
          value in the value raster that belong to the same zone as the output
          cell will be calculated.MAXIMUM-The largest value of all cells in the
          value raster that belong
          to the same zone as the output cell will be calculated.MEDIAN-The
          median value of all cells in the value raster that belong
          to the same zone as the output cell will be calculated.MINIMUM-The
          smallest value of all cells in the value raster that
          belong to the same zone as the output cell will be
          calculated.MINORITY-The value that occurs least often for all cells in
          the value
          raster that belong to the same zone as the output cell will be
          calculated.MINORITY_COUNT-The frequency of all cells that contain the
          minority
          value in the value raster that belong to the same zone as the output
          cell will be calculated.MINORITY_PERCENT-The percentage of cells that
          contain the minority
          value in the value raster that belong to the same zone as the output
          cell will be calculated. PERCENTILE-The percentile of all
          cells in the value raster
          that belong to the same zone as the output cell will be calculated.
          The 90th percentile is calculated by default. You can specify other
          values (from 0 to 100) using theparameter. Percentile
          ValueRANGE-The difference between the largest and smallest value of
          all
          cells in the value raster that belong to the same zone as the output
          cell will be calculated.STD-The standard deviation of all cells in the
          value raster that
          belong to the same zone as the output cell will be calculated.SUM-The
          total value of all cells in the value raster that belong to
          the same zone as the output cell will be calculated.VARIETY-The number
          of unique values for all cells in the value raster
          that belong to the same zone as the output cell will be calculated.
      ignore_nodata {Boolean}:
          Specifies whether NoData values in the value input will be ignored in
          the results of the zone that they fall within.DATA-Within any
          particular zone, only cells that have a value in the
          input value raster will be used in determining the output value for
          that zone. NoData cells in the value raster will be ignored in the
          statistic calculation. This is the default.NODATA-Within any
          particular zone, if NoData cells exist in the value
          raster, they will not be ignored and their existence indicates that
          there is insufficient information to perform statistical calculations
          for all the cells in that zone. Consequently, the entire zone will
          receive the NoData value on the output raster.
      process_as_multidimensional {Boolean}:
          Specifies how the input rasters will be calculated if they are
          multidimensional.CURRENT_SLICE-Statistics will be calculated from the
          current slice of
          the input multidimensional dataset. This is the
          default.ALL_SLICES-Statistics will be calculated for all dimensions of
          the
          input multidimensional dataset.
      percentile_value {Double}:
          The percentile that will be calculated. The default is 90, indicating
          the 90th percentile.The values can range from 0 to 100. The 0th
          percentile is essentially
          equivalent to the minimum statistic, and the 100th percentile is
          equivalent to maximum. A value of 50 will produce essentially the same
          result as the median statistic.This parameter is only supported if the
          statistics_type parameter is
          set to PERCENTILE.
      percentile_interpolation_type {String}:
          Specifies the method of interpolation that will be used when the
          percentile value falls between two cell values from the input value
          raster.AUTO_DETECT-If the input value raster is of integer pixel type,
          the
          NEAREST method will be used. If the input value raster is of floating
          point pixel type, the LINEAR method will be used. This is the
          default.NEAREST-The nearest available value to the desired percentile
          is used.
          In this case, the output pixel type is the same as that of the input
          value raster.LINEAR-The weighted average of the two surrounding values
          from the
          desired percentile is used. In this case, the output pixel type is
          floating point.
      circular_calculation {Boolean}:
          Specifies how the input raster will be processed for circular
          data.ARITHMETIC-Ordinary linear statistics will be calculated. This is
          the
          default.CIRCULAR-The statistics for angles or other cyclic quantities,
          such as
          compass direction in degrees, daytimes, and fractional parts of real
          numbers, will be calculated.
      circular_wrap_value {Double}:
          The value that will be used to round a linear value to the range of a
          given circular statistic. Its value must be a positive integer or a
          floating-point value. The default value is 360 degrees.This parameter
          is only supported if the  circular_calculation
          parameter is set to CIRCULAR.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output zonal statistics raster.

        """