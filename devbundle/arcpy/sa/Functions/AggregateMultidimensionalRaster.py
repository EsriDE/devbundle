# Generated documentation for module arcpy.sa.Functions


class AggregateMultidimensionalRaster(object):
    """
    Generates a multidimensional raster dataset by combining existing multidimensional raster variables along a dimension.
    """

    @property
    def description(self) -> str:
        return """

        AggregateMultidimensionalRaster_sa(in_multidimensional_raster, dimension, {aggregation_method}, {variables;variables...}, {aggregation_def}, {interval_keyword}, {interval_value}, {interval_unit}, {interval_ranges;interval_ranges...}, {aggregation_function}, {ignore_nodata}, {dimensionless}, {percentile_value}, {percentile_interpolation_type})

        Generates a multidimensional raster dataset by combining existing
        multidimensional raster variables along a dimension.

     INPUTS:
      in_multidimensional_raster (Raster Dataset / Mosaic Dataset / Raster Layer / Mosaic Layer / Image Service):
          The input multidimensional raster dataset.
      dimension (String):
          The aggregation dimension. This is the dimension along which the
          variables will be aggregated.
      aggregation_method {String}:
          Specifies the mathematical method that will be used to combine the
          aggregated slices in an interval.MEAN-The mean of a pixel's values
          will be calculated across all slices
          in the interval. This is the default.MAXIMUM-The maximum value of a
          pixel will be calculated across all
          slices in the interval.MAJORITY-The pixel value that occurred most
          frequently will be
          calculated across all slices in the interval.MINIMUM-The minimum value
          of a pixel will be calculated across all
          slices in the interval.MINORITY-The pixel value that occurred least
          frequently will be
          calculated across all slices in the interval.MEDIAN-The median value
          of a pixel will be calculated across all
          slices in the interval. PERCENTILE-The percentile of values
          for a pixel will be
          calculated across all slices in the interval. The 90th percentile is
          calculated by default. You can specify other values (from 0 to 100)
          using theparameter. Percentile valueRANGE-The range of values
          for a pixel will be calculated across all
          slices in the interval.STD-The standard deviation of a pixel's values
          will be calculated
          across all slices in the interval.SUM-The sum of a pixel's values will
          be calculated across all slices
          in the interval.VARIETY-The number of unique pixel values will be
          calculated across
          all slices in the interval.CUSTOM-The pixel value will be calculated
          based on a custom raster
          function.When aggregation_method is set to CUSTOM, the
          aggregation_function
          parameter becomes enabled.
      variables {String}:
          The variable or variables that will be aggregated along the given
          dimension. If no variable is specified, all variables with the
          selected dimension will be aggregated.For example, to aggregate daily
          temperature data into monthly average
          values, specify temperature as the variable to be aggregated. If you
          do not specify any variables and you have both daily temperature and
          daily precipitation variables, both variables will be aggregated into
          monthly averages and the output multidimensional raster will include
          both variables.
      aggregation_def {String}:
          Specifies the dimension interval for which the data will be
          aggregated.ALL-The data values will be aggregated across all slices.
          This is the
          default.INTERVAL_KEYWORD-The variable data will be aggregated using a
          commonly
          known interval.INTERVAL_VALUE-The variable data will be aggregated
          using a user-
          specified interval and unit.INTERVAL_RANGES-The variable data will be
          aggregated between specified
          pairs of values or dates.
      interval_keyword {String}:
          Specifies the keyword interval that will be used when aggregating
          along the dimension. This parameter is required when the
          aggregation_def parameter is set to INTERVAL_KEYWORD and the
          aggregation must be across time.HOURLY-The data values will be
          aggregated into hourly time steps, and
          the result will include every hour in the time series.DAILY-The data
          values will be aggregated into daily time steps, and
          the result will include every day in the time series.WEEKLY-The data
          values will be aggregated into weekly time steps, and
          the result will include every week in the time series.DEKADLY-The data
          values will be aggregated into 3 periods of 10 days
          each. The last period can contain more or fewer than 10 days. The
          output will include 3 slices for each month.PENTADLY-The data values
          will be aggregated into 6 periods of 5 days
          each. The last period can contain more or fewer than 5 days. The
          output will include 6 slices for each month.MONTHLY-The data values
          will be aggregated into monthly time steps,
          and the result will include every month in the time
          series.QUARTERLY-The data values will be aggregated into quarterly
          time
          steps, and the result will include every quarter in the time
          series.YEARLY-The data values will be aggregated into yearly time
          steps, and
          the result will include every year in the time
          series.RECURRING_DAILY-The data values will be aggregated into daily
          time
          steps, and the result will include one aggregated value per Julian
          day. The output will include, at most, 366 daily time
          slices.RECURRING_WEEKLY-The data values will be aggregated into weekly
          time
          steps, and the result will include one aggregated value per week. The
          output will include, at most, 53 weekly time
          slices.RECURRING_MONTHLY-The data values will be aggregated into
          monthly time
          steps, and the result will include one aggregated value per month. The
          output will include, at most, 12 monthly time
          slices.RECURRING_QUARTERLY-The data values will be aggregated into
          quarterly
          time steps, and the result will include one aggregated value per
          quarter. The output will include, at most, 4 quarterly time slices.
      interval_value {Double}:
          The size of the interval that will be used for the aggregation. This
          parameter is required when the aggregation_def parameter is set to
          INTERVAL_VALUE.For example, to aggregate 30 years of monthly
          temperature data into
          5-year increments, enter 5 as the interval_value, and specify
          interval_unit as YEARS.
      interval_unit {String}:
          The unit that will be used for the interval_value parameter. This
          parameter is required when the dimension parameter is set to a time
          field and the aggregation_def parameter is set to INTERVAL_VALUE.If
          you are aggregating anything other than time, this option will not
          be available and the unit for the interval value will match the
          variable unit of the input multidimensional raster data.HOURS-The data
          values will be aggregated into hourly time slices at
          the interval provided.DAYS-The data values will be aggregated into
          daily time slices at the
          interval provided.WEEKS-The data values will be aggregated into weekly
          time slices at
          the interval provided.MONTHS-The data values will be aggregated into
          monthly time slices at
          the interval provided.YEARS-The data values will be aggregated into
          yearly time slices at
          the interval provided.
      interval_ranges {Value Table}:
          Interval ranges specified in a value table will be used to aggregate
          groups of values. The value table consists of pairs of minimum and
          maximum range values, with data type Double or Date.This parameter is
          required when the aggregation_def parameter is set
          to INTERVAL_RANGE.
      aggregation_function {File / String}:
          A custom raster function that will be used to compute the pixel values
          of the aggregated rasters. The input is a raster function JSON object
          or an .rft.xml file created from a function chain or a custom Python
          raster function.This parameter is required when the aggregation_method
          parameter is
          set to CUSTOM.
      ignore_nodata {Boolean}:
          Specifies whether NoData values will be ignored in the
          analysis.DATA-The analysis will include all valid pixels along a given
          dimension and ignore NoData pixels. This is the default.NODATA-The
          analysis will result in NoData if there are NoData values
          for the pixels along the given dimension.
      dimensionless {Boolean}:
          Specifies whether the layer will have dimension values. This parameter
          is only enabled if a single slice is selected to create a
          layer.NO_DIMENSIONS-The layer will not have dimension
          values.DIMENSIONS-The
          layer will have dimension values. This is the default.
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
          Specifies the method of percentile interpolation that will be used
          when there is an even number of values from the input raster to be
          calculated.NEAREST-The nearest available value to the desired
          percentile will be
          used. In this case, the output pixel type will be the same as that of
          the input value raster.LINEAR-The weighted average of the two
          surrounding values from the
          desired percentile will be used. In this case, the output pixel type
          will be floating point.

     OUTPUTS:
      out_multidimensional_raster (Raster Dataset):
          The output Cloud Raster Format (CRF) multidimensional raster dataset.

        """