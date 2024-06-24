# Generated documentation for module arcpy.ia.Functions


class DetectChangeUsingChangeAnalysisRaster(object):
    """
    Generates a raster containing pixel change information using the output change analysis raster from the Analyze Changes Using CCDC tool or the Analyze Changes Using LandTrendr tool.
    """

    @property
    def description(self) -> str:
        return """

        DetectChangeUsingChangeAnalysisRaster_ia(in_change_analysis_raster, out_raster, change_type, {max_number_changes}, {segment_date}, {change_direction}, {filter_by_year}, {min_year}, {max_year}, {filter_by_duration}, {min_duration}, {max_duration}, {filter_by_magnitude}, {min_magnitude}, {max_magnitude}, {filter_by_start_value}, {min_start_value}, {max_start_value}, {filter_by_end_value}, {min_end_value}, {max_end_value})

        Generates a raster containing pixel change information using the
        output change analysis raster from the Analyze Changes Using CCDC tool
        or the Analyze Changes Using LandTrendr tool.

     INPUTS:
      in_change_analysis_raster (Raster Dataset / Raster Layer / Image Service):
          The change analysis raster generated from the Analyze Changes Using
          CCDC tool or the Analyze Changes Using LandTrendr tool.
      change_type (String):
          Specifies the change information that will be calculated for each
          pixel.TIME_OF_LATEST_CHANGE-Each pixel will contain the date of its
          most
          recent change in the time series. This is the
          default.TIME_OF_EARLIEST_CHANGE-Each pixel will contain the date of
          its
          earliest change in the time series.TIME_OF_LARGEST_CHANGE-Each pixel
          will contain the date of its most
          significant change in the time series.NUM_OF_CHANGES-Each pixel will
          contain the total number of times it
          changed in the time series.TIME_OF_LONGEST_CHANGE-Each pixel will
          contain the date of change at
          the beginning or end of the longest transition segment in the time
          series.TIME_OF_SHORTEST_CHANGE-Each pixel will contain the date of
          change at
          the beginning or end of the shortest transition segment in the time
          series.TIME_OF_FASTEST_CHANGE-Each pixel will contain the date of
          change at
          the beginning or end of the transition that occurred most
          quickly.TIME_OF_SLOWEST_CHANGE-Each pixel will contain the date of
          change at
          the beginning or end of the transition that occurred most slowly.
      max_number_changes {Long}:
          The maximum number of changes per pixel that will be calculated. This
          number corresponds to the number of bands in the output raster. The
          default is 1, meaning only one change date will be calculated, and the
          output raster will contain only one band.This parameter is not enabled
          when the change_type parameter is set to
          NUM_OF_CHANGES.
      segment_date {String}:
          Specifies whether the date at the beginning of a change segment will
          be extracted or at the end.This parameter is available only when the
          input change analysis raster
          is the output from the Analyze Changes Using LandTrendr
          tool.BEGINNING_OF_SEGMENT-The date at the beginning of a change
          segment
          will be extracted. This is the default.END_OF_SEGMENT-The date at the
          end of a change segment will be
          extracted.
      change_direction {String}:
          Specifies the direction of change that will be included in the
          analysis.This parameter is available only when the input change
          analysis raster
          is the output from the Analyze Changes Using LandTrendr tool.ALL-All
          change directions will be included in the output. This is the
          default.INCREASE-Only change in the positive or increasing direction
          will be
          included in the output.DECREASE-Only change in the negative or
          decreasing direction will be
          included in the output.
      filter_by_year {Boolean}:
          Specifies whether the output will be filtered by a range of
          years.FILTER_BY_YEAR-Results will be filtered so that only changes
          that
          occurred within a specific range of years will be included in the
          output.NO_FILTER_BY_YEAR-Results will not be filtered by year. This is
          the
          default.
      min_year {Long}:
          The earliest year that will be used to filter results. This parameter
          is required if the filter_by_year parameter is set to FILTER_BY_YEAR.
      max_year {Long}:
          The latest year that will be used to filter results.This parameter is
          required if the filter_by_year parameter is set to
          FILTER_BY_YEAR.
      filter_by_duration {Boolean}:
          Specifies whether results will be filtered by the change duration.This
          parameter is enabled only when the input change analysis raster
          is the output from the Analyze Changes Using LandTrendr
          tool.FILTER_BY_DURATION-Results will be filtered by duration so that
          only
          the changes that lasted a given amount of time will be included in the
          output.NO_FILTER_BY_DURATION-Results will not be filtered by duration.
          This
          is the default.
      min_duration {Double}:
          The minimum number of consecutive years that will be included in the
          results.This parameter is required if the filter_by_duration parameter
          is set
          to FILTER_BY_DURATION.
      max_duration {Double}:
          The maximum number of consecutive years that will be included in the
          results.This parameter is required if the filter_by_duration parameter
          is set
          to FILTER_BY_DURATION.
      filter_by_magnitude {Boolean}:
          Specifies whether results will be filtered by change
          magnitude. Checked-Results will be filtered by magnitude so
          that only the changes
          of a given magnitude will be included in the output.Unchecked-Results
          will not be filtered by magnitude. This is the
          default.Specifies whether results will be filtered by change
          magnitude.FILTER_BY_MAGNITUDE-Results will be filtered by magnitude so
          that only
          the changes of a given magnitude will be included in the
          output.NO_FILTER_BY_MAGNITUDE-Results will not be filtered by
          magnitude. This
          is the default.
      min_magnitude {Double}:
          The minimum magnitude that will be included in the results.This
          parameter is required if the filter_by_magnitude parameter is set
          to FILTER_BY_MAGNITUDE.
      max_magnitude {Double}:
          The maximum magnitude that will be included in the results.This
          parameter is required if the filter_by_magnitude parameter is set
          to FILTER_BY_MAGNITUDE.
      filter_by_start_value {Boolean}:
          Specifies whether results will be filtered by start value.This
          parameter is enabled only when the input change analysis raster
          is the output from the Analyze Changes Using LandTrendr
          tool.FILTER_BY_START_VALUE-Results will be filtered by start value so
          that
          only the changes of a given start value will be included in the
          output.NO_FILTER_BY_START_VALUE-Results will not be filtered by start
          value.
          This is the default.
      min_start_value {Double}:
          The minimum start value that will be included in the results.This
          parameter is required if the filter_by_start_value parameter is
          set to FILTER_BY_START_VALUE.
      max_start_value {Double}:
          The maximum start value that will be included in the results.This
          parameter is required if the filter_by_start_value parameter is
          set to FILTER_BY_START_VALUE.
      filter_by_end_value {Boolean}:
          Specifies whether results will be filtered by end value.This parameter
          is enabled only when the input change analysis raster
          is the output from the Analyze Changes Using LandTrendr
          tool.FILTER_BY_END_VALUE-Results will be filtered by end value so that
          only
          the changes of a given end value will be included in the
          output.NO_FILTER_BY_END_VALUE-Results will not be filtered by end
          value. This
          is the default.
      min_end_value {Double}:
          The minimum end value that will be included in the results.This
          parameter is required if the filter_by_end_value parameter is set
          to FILTER_BY_END_VALUE.
      max_end_value {Double}:
          The maximum end value that will be included in the results.This
          parameter is required if the filter_by_end_value parameter is set
          to FILTER_BY_END_VALUE.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster containing the detected change information.

        """