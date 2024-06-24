# Generated documentation for module arcpy.geoanalytics


class CreateSpaceTimeCube(object):
    """
    Summarizes a set of points into a netCDF data structure by aggregating them into space-time bins. Within each bin, the points are counted, and specified attributes are aggregated. For all bin locations, the trend for counts and summary field values are evaluated.
    """

    @property
    def description(self) -> str:
        return """

        CreateSpaceTimeCube_geoanalytics(point_layer, output_name, distance_interval, time_step_interval, {time_step_interval_alignment}, {reference_time}, {summary_fields;summary_fields...})

        Summarizes a set of points into a netCDF data structure by aggregating
        them into space-time bins. Within each bin, the points are counted,
        and specified attributes are aggregated. For all bin locations, the
        trend for counts and summary field values are evaluated.

     INPUTS:
      point_layer (Feature Set):
          The input point feature class that will be aggregated into space-time
          bins.
      output_name (String):
          The output netCDF data cube that will be created to contain counts and
          summaries of the input feature point data.
      distance_interval (Linear Unit):
          The distance that will determine the bin size.The size of the bins
          will be used to aggregate the point_layer. All
          points that fall within the same distance_interval and
          time_step_interval will be aggregated.
      time_step_interval (Time Unit):
          The number of seconds, minutes, hours, days, weeks, or years that will
          represent a single time step. All points within the same
          time_step_interval and distance_interval will be aggregated. Examples
          of valid entries for this parameter are 1 Weeks, 13 Days, or 1 Months.
      time_step_interval_alignment {String}:
          Specifies how aggregation will occur based on
          the(time_step_interval in Python) parameter. Time
          IntervalEND_TIME-Time steps will align to the last time event and
          aggregate
          back in time.START_TIME-Time steps will align to the first time event
          and aggregate
          forward in time. REFERENCE_TIME-Time steps will align to a
          specified date or
          time. If all points in the input features have a time stamp larger
          than the specified reference time (or it falls exactly on the start
          time of the input features), the time-step interval will begin with
          that reference time and aggregate forward in time (as occurs with
          thealignment). If all points in the input features have a time stamp
          smaller than the specified reference time (or it falls exactly on the
          end time of the input features), the time-step interval will end with
          that reference time and aggregate backward in time (as occurs with
          thealignment). If the specified reference time is in the middle of the
          time extent of the data, a time-step interval will be created ending
          with the reference time provided (as occurs with thealignment);
          additional intervals will be created both before and after the
          reference time until the full time extent of the data is covered.
          Start timeEnd timeEnd time
      reference_time {Date}:
          The date or time that will be used to align the time-step intervals.
          For example, to bin the data weekly, Monday to Sunday, set a reference
          time of Sunday at midnight to ensure that bins break between Sunday
          and Monday at midnight.
      summary_fields {Value Table}:
          The numeric field containing attribute values that will be used to
          calculate the specified statistic when aggregating into a space time
          cube. Multiple statistic and field combinations can be specified. Null
          values are excluded from all statistical calculations.
          Available statistic types are the following:        Sum-Adds
          the total value for the specified field within each
          bin.Mean-Calculates the average for the specified field within each
          bin.Minimum-Finds the smallest value for all records of the specified
          field within each bin.Maximum-Finds the largest value for all records
          of the specified field
          within each bin.Standard deviation-Finds the standard deviation on
          values in the
          specified field within each bin. Available fill types are the
          following:        Zeros-Fills
          empty bins with zeros.Spatial_Neighbors-Fills empty bins
          with the average value of spatial
          neighbors.Space Time Neighbors-Fills empty bins with the average value
          of space-
          time neighbors.Temporal Trend-Fills empty bins using an interpolated
          univariate
          spline algorithm. Null values present in any of the summary
          fields will result
          in those features being excluded from the analysis. If count of points
          in each bin is part of your analysis strategy, consider creating
          separate cubes, one for the count (without summary fields) and one for
          summary fields. If the set of null values is different for each
          summary field, consider creating a separate cube for each summary
          field.

        """