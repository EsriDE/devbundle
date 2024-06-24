# Generated documentation for module arcpy.ra


class SummarizeRasterWithin(object):
    """
    Calculates statistics on values of a raster within the zones of another dataset.
    """

    @property
    def description(self) -> str:
        return """

        SummarizeRasterWithin_ra(inputZoneLayer, zoneField, inputRasterLayertoSummarize, outputName, {statisticType}, {ignoreMissingValues}, {processAsMultidimensional}, {percentileValue}, {percentileInterpolationType}, {circularCalculation}, {circularWrapValue})

        Calculates statistics on values of a raster within the zones of
        another dataset.

     INPUTS:
      inputZoneLayer (Image Service / Feature Layer / Raster Layer / String):
          The input that defines the zones.Both raster and feature data can be
          used for the zone input.
      zoneField (String):
          The field that defines each zone.It can be an integer or a string
          field of the zone dataset.
      inputRasterLayertoSummarize (Image Service / Raster Layer / String):
          The raster that contains the values on which to summarize a statistic.
      outputName (String):
          The name of the output raster service.If the image service layer
          already exists, you will be prompted to
          provide another name.
      statisticType {String}:
          Specifies the statistic type that will be calculated. The
          available options when the raster to summarize is of
          integer data type are,,,,,,,,,, and.
          AverageMajorityMaximumMedianMinimumMinorityPercentileRangeStandard
          deviationSumVariety        If the raster to summarize is of float data
          type, the options
          are,,,,,,, and.
          AverageMaximumMedianMinimumPercentileRangeStandard
          deviationSumMEAN-The average of all cells in the raster layer to be
          summarized
          that belong to the same zone as the output cell will be calculated.
          This is the default.MAJORITY-The value that occurs most often of all
          cells in the raster
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
          ValueRANGE-The difference between the largest and smallest value of
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
          be calculated.
      ignoreMissingValues {Boolean}:
          Specifies whether missing values in the raster layer to summarize will
          be ignored in the results of the zones that they fall
          within.DATA-Within any particular zone, only cells that have a value
          in the
          raster layer being summarized will be used in determining the output
          value for that zone. Missing or NoData cells will be ignored in the
          statistic calculation. This is the default.NODATA-Within any
          particular zone, if any cells in the raster layer
          being summarized do not have a value, they will not be ignored and
          their existence indicates that there is insufficient information to
          perform statistical calculations for all the cells in that zone.
          Consequently, the entire zone will receive the NoData value on the
          output raster.
      processAsMultidimensional {Boolean}:
          Specifies how the input rasters will be processed if they are
          multidimensional.CURRENT_SLICE-Statistics will be calculated from the
          current slice of
          the input multidimensional dataset. This is the
          default.ALL_SLICES-Statistics will be calculated for all dimensions of
          the
          input multidimensional dataset.
      percentileValue {Double}:
          The percentile that will be calculated. The default is 90, indicating
          the 90th percentile.The values can range from 0 to 100. The 0th
          percentile is essentially
          equivalent to the minimum statistic, and the 100th percentile is
          equivalent to maximum. A value of 50 will produce essentially the same
          result as the median statistic.This parameter is only available while
          calculating percentile.
      percentileInterpolationType {String}:
          Specifies the method of interpolation that will be used when the
          percentile value falls between two cell values from the input value
          raster.AUTO_DETECT-If the input value raster is of integer pixel type,
          the
          NEAREST method will be used. If the input value raster is of floating-
          point pixel type, the LINEAR method will be used. This is the
          default.NEAREST-The nearest available value to the desired percentile
          will be
          used. In this case, the output pixel type is the same as that of the
          input value raster.LINEAR-The weighted average of the two surrounding
          values from the
          desired percentile will be used. In this case, the output pixel type
          is floating point.
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