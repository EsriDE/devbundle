# Generated documentation for module arcpy.ia.Functions


class FindArgumentStatistics(object):
    """
    Extracts the dimension value or band index at which a given statistic is attained for each pixel in a multidimensional or multiband raster.
    """

    @property
    def description(self) -> str:
        return """

        FindArgumentStatistics_ia(in_raster, {dimension}, {dimension_def}, {interval_keyword}, {variables;variables...}, {statistics_type}, {min}, {max}, {multiple_occurrence}, {ignore_nodata}, {value}, {comparison}, {occurrence})

        Extracts the dimension value or band index at which a given statistic
        is attained for each pixel in a multidimensional or multiband raster.

     INPUTS:
      in_raster (Raster Dataset / Mosaic Dataset / Raster Layer / Mosaic Layer / Image Service):
          The input multidimensional or multiband raster to be analyzed.
      dimension {String}:
          The dimension from which the statistic will be extracted. If the input
          raster is not a multidimensional raster, this parameter is not
          required.
      dimension_def {String}:
          Specifies how the statistic will be extracted from the
          dimension.ALL-The statistic will be extracted across all dimensions.
          This is the
          default.INTERVAL_KEYWORD-The statistic will be extracted from the time
          dimension according to the interval keyword.
      interval_keyword {String}:
          The unit of time for which the statistic will be extracted. For
          example, you have five years of daily sea surface
          temperature data and you want to know the year in which the maximum
          temperature was observed. Setto, setto, and setto. Statistics
          TypeArgument of the maximumDimension DefinitionInterval KeywordKeyword
          IntervalYearly        Alternatively, if you want to know the month in
          which the
          maximum temperature was consistently observed, setto, setto, and
          setto. This will generate a raster in which each pixel contains the
          month in which the statistic was reached across the five-year record
          (for example, 08/18/2018, 08/25/2016, 08/07/2013). Statistics
          TypeArgument of the maximumDimension DefinitionInterval KeywordKeyword
          IntervalRecurring MonthlyThis parameter is required when the dimension
          parameter is set to
          StdTime and the dimension_def parameter is set to
          INTERVAL_KEYWORD.RECURRING_DAILY-The statistic will be extracted
          across
          days.RECURRING_WEEKLY-The statistic will be extracted across
          weeks.RECURRING_MONTHLY-The statistic will be extracted across
          months.RECURRING_QUARTERLY-The statistic will be extracted across
          quarters.HOURLY-The statistic will be extracted for the hour in which
          the
          statistic was reached.DAILY-The statistic will be extracted for the
          day in which the
          statistic was reached.WEEKLY-The statistic will be extracted for the
          week in which the
          statistic was reached.MONTHLY-The statistic will be extracted for the
          month in which the
          statistic was reached.QUARTERLY-The statistic will be extracted for
          the quarter in which the
          statistic was reached.YEARLY-The statistic will be extracted for the
          year in which the
          statistic was reached.
      variables {String}:
          The variable or variables to be analyzed. If the input raster is not
          multidimensional, the pixel values of the multiband raster are
          considered the variable. If the input raster is multidimensional and
          no variable is specified, all variables with the selected dimension
          will be analyzed.For example, to find the years in which temperature
          values were
          highest, specify temperature as the variable to be analyzed. If you do
          not specify any variables and you have both temperature and
          precipitation variables, both variables will be analyzed, and the
          output multidimensional raster will include both variables.
      statistics_type {String}:
          Specifies the statistic to extract from the variable or variables
          along the given dimension.ARGUMENT_MIN-The dimension value at which
          the minimum variable value
          is reached will be extracted. This is the default.ARGUMENT_MAX-The
          dimension value at which the maximum variable value
          is reached will be extracted.ARGUMENT_MEDIAN-The dimension value at
          which the median variable value
          is reached will be extracted.DURATION-The longest dimension duration
          value between the minimum and
          maximum variable values will be extracted.ARGUMENT_VALUE-The dimension
          value at which the specified variable
          value is reached will be extracted.
      min {Double}:
          The minimum variable value to be used to extract the duration.This
          parameter is required when the statistics_type parameter is set
          to DURATION.
      max {Double}:
          The maximum variable value to be used to extract the duration.This
          parameter is required when the statistics_type parameter is set
          to DURATION.
      multiple_occurrence {Long}:
          The pixel value to use to indicate that a given argument statistic was
          reached more than once in the input raster dataset. If not specified,
          the pixel value will be the value of the dimension as specified by the
          occurrence parameter, either the first or last occurrence.
      ignore_nodata {Boolean}:
          Specifies whether NoData values will be ignored in the
          analysis.DATA-The analysis will include all valid pixels along a given
          dimension and ignore NoData pixels. This is the default.NODATA-The
          analysis will result in NoData if there are NoData values
          for the pixels along the given dimension.
      value {Double}:
          The value at which a comparison will be made to extract the dimension
          value. This parameter is required when theparameter is set to.
          Statistics TypeArgument of the value
      comparison {String}:
          Specifies the comparison type that will be used to extract the
          dimension value.EQUAL_TO-The extracted dimension is equal to the
          specified value. This
          is the default.GREATER_THAN-The extracted dimension is greater than
          the specified
          value.SMALLER_THAN-The extracted dimension is smaller than the
          specified
          value.
      occurrence {String}:
          Specifies whether the value of the dimension will be returned the
          first time or last time the argument statistic is
          reached.FIRST_OCCURRENCE-The value of the dimension will be returned
          the first
          time the argument statistic is reached. This is the
          default.LAST_OCCURRENCE-The value of the dimension will be returned
          the last
          time the argument statistic is reached.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster dataset.

        """