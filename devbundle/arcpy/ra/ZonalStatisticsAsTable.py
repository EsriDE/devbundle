# Generated documentation for module arcpy.ra


class ZonalStatisticsAsTable(object):
    """
    Calculates the values of a raster within the zones of another dataset and reports the results to a table.
    """

    @property
    def description(self) -> str:
        return """

        ZonalStatisticsAsTable_ra(inputZoneRasterOrFeatures, inputValueRaster, outputTableName, zoneField, {ignoreNodata}, {statisticType}, {percentileValues;percentileValues...}, {processAsMultidimensional}, {percentileInterpolationType}, {circularCalculation}, {circularWrapValue})

        Calculates the values of a raster within the zones of another dataset
        and reports the results to a table.

     INPUTS:
      inputZoneRasterOrFeatures (Image Service / Feature Layer / Raster Layer / String):
          The input that defines the zones.Both raster and feature data can be
          used for the zone input.
      inputValueRaster (Image Service / Raster Layer / String):
          The raster that contains the values on which to summarize a statistic.
      outputTableName (String):
          The name of the output table.If it's an existing table, you will be
          prompted to provide another
          name.
      zoneField (String):
          The field that defines each zone.It can be an integer or a string
          field of the zone dataset.
      ignoreNodata {Boolean}:
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
      statisticType {String}:
          Specifies the statistic type that will be calculated. The
          available options when the value raster is integer
          are,,,,,,,,,,,,,, and.
          AllMeanMajorityMaximumMedianMinimumMinorityPercentileRangeStandard
          deviationSumVarietyMinimum and MaximumMean and Standard
          deviationMinimum, Maximum and Mean        If the value raster is
          float, the options are,,,,,,,, and.
          AllMeanMaximumMedianPercentileMinimumRangeStandard deviationSum
          ALL-All of the statistics will be calculated for an integer
          type value raster. All statistics exceptandwill be calculated for a
          floating-point type value raster. This is the default.
          MedianPercentileMEAN-The mean of all cells in the raster layer to be
          summarized that
          belong to the same zone as the output cell will be
          calculated.MAJORITY-The value that occurs most often of all cells in
          the raster
          layer to be summarized that belong to the same zone as the output cell
          will be calculated.MAXIMUM-The largest value of all cells in the
          raster layer to be
          summarized that belong to the same zone as the output cell will be
          calculated.MEDIAN-The median value of all cells in the raster layer to
          be
          summarized that belong to the same zone as the output cell will be
          calculated.MINIMUM-The smallest value of all cells in the raster layer
          to be
          summarized that belong to the same zone as the output cell will be
          calculated.MINORITY-The value that occurs least often of all cells in
          the raster
          layer to be summarized that belong to the same zone as the output cell
          will be calculated. PERCENTILE-The percentile of all cells in
          the value raster
          that belong to the same zone as the output cell will be calculated.
          The 90th percentile is calculated by default. You can specify other
          values (from 0 to 100) using theparameter. Percentile
          ValuesRANGE-The difference between the largest and smallest value of
          all
          cells in the raster layer to be summarized that belong to the same
          zone as the output cell will be calculated.STD-The standard deviation
          of all cells in the raster layer to be
          summarized that belong to the same zone as the output cell will be
          calculated.SUM-The total value of all cells in the raster layer to be
          summarized
          that belong to the same zone as the output cell will be
          calculated.VARIETY-The number of unique values for all cells in the
          raster layer
          to be summarized that belong to the same zone as the output cell will
          be calculated.MIN_MAX-Both the minimum and maximum statistics will be
          calculated.MEAN_STD-Both the mean and standard deviation statistics
          will be
          calculated.MIN_MAX_MEAN-The minimum, maximum, and mean statistics will
          be
          calculated.
      percentileValues {Double}:
          The percentile that will be calculated. The default is 90, indicating
          the 90th percentile.The values can range from 0 to 100. The 0th
          percentile is essentially
          equivalent to the minimum statistic, and the 100th percentile is
          equivalent to maximum. A value of 50 will produce essentially the same
          result as the median statistic.This parameter is only available while
          calculating percentile.
      processAsMultidimensional {Boolean}:
          Specifies how the input rasters will be processed if they are
          multidimensional.CURRENT_SLICE-Statistics will be calculated from the
          current slice of
          the input multidimensional dataset. This is the
          default.ALL_SLICES-Statistics will be calculated for all dimensions of
          the
          input multidimensional dataset.
      percentileInterpolationType {String}:
          Specifies the method of interpolation that will be used when the
          percentile value falls between two cell values from the input value
          raster.AUTO_DETECT-If the input value raster is of integer pixel type,
          the
          NEAREST method will be used. If the input value raster is of floating-
          point pixel type, the LINEAR method will be used. This is the
          default.NEAREST-The nearest available value to the desired percentile
          will be
          used.LINEAR-The weighted average of the two surrounding values from
          the
          desired percentile will be used.
      circularCalculation {Boolean}:
          Specifies how the statistics type will be
          calculated.ARITHMETIC-Arithmetic statistics will be calculated. This
          is the
          default.CIRCULAR-Circular statistics that are appropriate for cyclic
          quantities will be calculated, such as compass direction in degrees,
          daytimes, and fractional parts of real numbers.
      circularWrapValue {Double}:
          The highest possible value (upper bound) in the cyclic data. It is a
          positive number, with a default value of 360. This value also
          represents the same quantity as the lowest possible value (lower
          bound).This parameter is only applicable when circular statistics are
          calculated.

        """