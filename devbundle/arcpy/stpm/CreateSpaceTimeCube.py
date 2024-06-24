# Generated documentation for module arcpy.stpm


class CreateSpaceTimeCube(object):
    """
    Summarizes a set of points into a netCDF data structure by aggregating them into space-time bins. Within each bin, the points are counted, and specified attributes are aggregated. For all bin locations, the trend for counts and summary field values are evaluated.
    """

    @property
    def description(self) -> str:
        return """

        CreateSpaceTimeCube_stpm(in_features, output_cube, time_field, {template_cube}, {time_step_interval}, {time_step_alignment}, {reference_time}, {distance_interval}, {summary_fields;summary_fields...}, {aggregation_shape_type}, {defined_polygon_locations}, {location_id})

        Summarizes a set of points into a netCDF data structure by aggregating
        them into space-time bins. Within each bin, the points are counted,
        and specified attributes are aggregated. For all bin locations, the
        trend for counts and summary field values are evaluated.

     INPUTS:
      in_features (Feature Layer):
          The input point feature class to be aggregated into space-time bins.
      time_field (Field):
          The field containing the date and time (timestamp) for each point.
          This field must be of type Date.
      template_cube {File}:
          A reference space-time cube used to define the output_cube extent of
          analysis, bin dimensions, and bin alignment. The time_step_interval,
          distance_interval, and reference_time values are also obtained from
          the template cube. This template cube must be a netCDF (.nc) file that
          has been created using this tool.A space-time cube created by
          aggregating into DEFINED_LOCATIONS cannot
          be used as a template_cube.
      time_step_interval {Time Unit}:
          The number of seconds, minutes, hours, days, weeks, or years that will
          represent a single time step. All points within the same
          time_step_interval and distance_interval will be aggregated. (When a
          template_cube is provided, this parameter is ignored, and the
          time_step_interval value is obtained from the template cube). Examples
          of valid entries for this parameter are 1 Weeks, 13 Days, or 1 Months.
      time_step_alignment {String}:
          Specifies how aggregation will occur based on a given
          time_step_interval. If a template_cube is provided, the
          time_step_alignment associated with the template_cube overrides this
          parameter setting and the time_step_alignment of the template_cube is
          used.END_TIME-Time steps align to the last time event and aggregate
          back in
          time.START_TIME-Time steps align to the first time event and aggregate
          forward in time.REFERENCE_TIME-Time steps align to a particular
          date/time that you
          specify. If all points in the input features have a timestamp larger
          than the reference time you provide (or it falls exactly on the start
          time of the input features), the time-step interval will begin with
          that reference time and aggregate forward in time (as occurs with a
          START_TIME alignment). If all points in the input features have a
          timestamp smaller than the reference time you provide (or it falls
          exactly on the end time of the input features), the time-step interval
          will end with that reference time and aggregate backward in time (as
          occurs with an END_TIME alignment). If the reference time you provide
          is in the middle of the time extent of your data, a time-step interval
          will be created ending with the reference time provided (as occurs
          with an END_TIME alignment); additional intervals will be created both
          before and after the reference time until the full time extent of your
          data is covered.
      reference_time {Date}:
          The date/time to use to align the time-step intervals. If you want to
          bin your data weekly from Monday to Sunday, for example, you could set
          a reference time of Sunday at midnight to ensure bins break between
          Sunday and Monday at midnight. (When a template_cube is provided, this
          parameter is ignored and the reference_time is based on the
          template_cube.)
      distance_interval {Linear Unit}:
          The size of the bins used to aggregate the in_features. All points
          that fall within the same distance_interval and time_step_interval
          will be aggregated. When aggregating into a hexagon grid, this
          distance is used as the height to construct the hexagon polygons.
          (When a template_cube is provided, this parameter is ignored and the
          distance interval value will be based on the template_cube.)
      summary_fields {Value Table}:
          The numeric field containing attribute values used to calculate the
          specified statistic when aggregating into a space-time cube. Multiple
          statistic and field combinations can be specified. Null values in any
          of the fields specified will result in that feature being dropped from
          the output cube. If there are null values present in your input
          features, it is highly recommended that you run the Fill Missing
          Values tool before creating a space-time cube. Available
          statistic types are:        SUM-Adds the total value
          for the specified field within each
          bin.MEAN-Calculates the average for the specified field within each
          bin.MIN-Finds the smallest value for all records of the specified
          field
          within each bin.MAX-Finds the largest value for all records of the
          specified field
          within each bin.STD-Finds the standard deviation on values in the
          specified field
          within each bin.MEDIAN-Finds the sorted middle value of all records of
          the specified
          field within each bin. Available fill types are:
          ZEROS-Fills empty bins with
          zeros.SPATIAL_NEIGHBORS-Fills empty bins
          with the average value of spatial
          neighborsSPACE_TIME_NEIGHBORS-Fills empty bins with the average value
          of space
          time neighbors.TEMPORAL_TREND-Fills empty bins using an interpolated
          univariate
          spline algorithm. Null values present in any of the summary
          field records will
          result in those features being excluded from the output cube. If there
          are null values present in your, it is highly recommended that you run
          the Fill Missing Values tool first. If, after running thetool, there
          are still null values present and having the count of points in each
          bin is part of your analysis strategy, you may want to consider
          creating separate cubes, one for the count (without) and one for. If
          the set of null values is different for each summary field, you may
          also consider creating a separate cube for each summary field.
          Input FeaturesFill Missing ValuesSummary FieldsSummary Fields
      aggregation_shape_type {String}:
          Specifies the shape of the polygon mesh into which the input feature
          point data will be aggregated.FISHNET_GRID-The input features will be
          aggregated into a grid of
          square (fishnet) cells.HEXAGON_GRID-The input features will be
          aggregated into a grid of
          hexagonal cells.DEFINED_LOCATIONS-The input features will be
          aggregated into the
          locations provided.
      defined_polygon_locations {Feature Layer}:
          The polygon features into which the input point data will be
          aggregated. These can represent county boundaries, police beats, or
          sales territories for example.
      location_id {Field}:
          The field containing the ID number for each unique location.

     OUTPUTS:
      output_cube (File):
          The output netCDF data cube that will be created to contain counts and
          summaries of the input feature point data.

        """