# Generated documentation for module arcpy.stpm


class CreateSpaceTimeCubeDefinedLocations(object):
    """
    Structures panel data or station data (defined locations where geography does not change but attributes are changing over time) into a netCDF data format by creating space-time bins. For all locations, the trend for variables or summary fields is evaluated.
    """

    @property
    def description(self) -> str:
        return """

        CreateSpaceTimeCubeDefinedLocations_stpm(in_features, output_cube, location_id, temporal_aggregation, time_field, time_step_interval, {time_step_alignment}, {reference_time}, {variables;variables...}, {summary_fields;summary_fields...}, {in_related_table}, {related_location_id})

        Structures panel data or station data (defined locations where
        geography does not change but attributes are changing over time) into
        a netCDF data format by creating space-time bins. For all locations,
        the trend for variables or summary fields is evaluated.

     INPUTS:
      in_features (Feature Layer):
          The input point or polygon feature class that will be converted to a
          space-time cube.
      location_id (Field):
          An integer or text field containing the ID number for each unique
          location.
      temporal_aggregation (Boolean):
          APPLY_TEMPORAL_AGGREGATION-The space-time cube will aggregate the
          features temporally based on the time-step interval provided. For
          example, the data has been collected daily and you want to create a
          cube with a weekly time-step interval.NO_TEMPORAL_AGGREGATION-The
          space-time cube will be created using the
          existing temporal structure of the input features. For example, you
          have yearly data and want to create a cube with a yearly time-step
          interval. This is the default.
      time_field (Field):
          The field containing the time stamp for each row in the dataset. This
          field must be of type date.
      time_step_interval (Time Unit):
          The number of seconds, minutes, hours, days, weeks, or years that will
          represent a single time step. Examples of valid entries for this
          parameter are 1 Weeks, 13 Days, or 1 Months.If you do not apply
          temporal aggregation (temporal_aggregation = "NO
          TEMPORAL_AGGREGATION"), set this parameter to the existing temporal
          structure of the data.If you apply temporal aggregation
          (temporal_aggregation = "APPLY
          TEMPORAL_AGGREGATION"), set this parameter to the time-step interval
          you want to create. All features within the same time-step interval
          will be aggregated.
      time_step_alignment {String}:
          Specifies how the cube structure will align based on a given
          time_step_interval value.END_TIME-Time steps will align to the last
          time event and aggregate
          back in time. This is the default.START_TIME-Time steps will align to
          the first time event and aggregate
          forward in time.REFERENCE_TIME-Time steps will align to the specified
          date and time.
          If all points in the input features have a time stamp larger than the
          reference time provided (or it falls exactly on the start time of the
          input features), the time-step interval will begin with that reference
          time and aggregate forward in time (as occurs with a start time
          alignment). If all points in the input features have a time stamp
          smaller than the reference time provided (or it falls exactly on the
          end time of the input features), the time-step interval will end with
          that reference time and aggregate backward in time (as occurs with an
          end time alignment). If the reference time provided is in the middle
          of the time extent of the data, a time-step interval will be created
          ending with the reference time provided (as occurs with an end time
          alignment). Additional intervals will be created both before and after
          the reference time until the full time extent of the data is covered.
      reference_time {Date}:
          The date and time that will be used to align the time-step intervals.
          To bin the data weekly from Monday to Sunday, for example, set a
          reference time of Sunday at midnight to ensure that bins break between
          Sunday and Monday at midnight.
      variables {Value Table}:
          The numeric field containing attribute values that will be brought
          into the space-time cube. The following are the available fill
          types:
          DROP_LOCATIONS-Locations with missing data for any of the variables
          will be excluded from the output space-time cube.ZEROS-Empty bins will
          be filled with zeros.SPATIAL_NEIGHBORS-Empty bins will be filled with
          the average value of
          spatial neighbors.SPACE_TIME_NEIGHBORS-Empty bins will be filled with
          the average value
          of space-time neighbors.TEMPORAL_TREND-Empty bins will be filled using
          an interpolated
          univariate spline algorithm.Null values in any of the variable records
          will result in an empty
          bin. If null values are present in the input features, it is
          recommended that you run the Fill Missing Values tool first.
      summary_fields {Value Table}:
          The numeric field containing attribute values that will be used to
          calculate the specified statistic when aggregating into a space-time
          cube. Multiple statistic and field combinations can be specified. Null
          values in any of the fields specified will result in that feature
          being excluded from the output cube. If null values are present in the
          input features, it is recommended that you run the Fill Missing Values
          tool before creating a space-time cube. The following are the
          available statistic types:
          SUM-The total value for the specified field within each bin will be
          calculated.MEAN-The average for the specified field within each bin
          will be
          calculated.MIN-The smallest value for all records of the specified
          field within
          each bin will be identified.MAX-The largest value for all records of
          the specified field within
          each bin will be identified.STD-The standard deviation for values in
          the specified field within
          each bin will be calculated.MEDIAN-The sorted middle value of all
          records of the specified field
          within each bin will be calculated. The following are the
          available fill types:        ZEROS-Empty
          bins will be filled with zeros.SPATIAL_NEIGHBORS-Empty
          bins will be filled with the average value of
          spatial neighborsSPACE_TIME_NEIGHBORS-Empty bins will be filled with
          the average value
          of space-time neighbors.TEMPORAL_TREND-Empty bins will be filled using
          an interpolated
          univariate spline algorithm.Null values in any of the summary field
          records will result in those
          features being excluded from the output cube. If null values are
          present in the input features, it is recommended that you run the Fill
          Missing Values tool first. If, after running the Fill Missing Values
          tool, null values are still present and having the count of points in
          each bin is part of your analysis strategy, consider creating separate
          cubes: one for the count (without summary fields) and one for the
          summary fields. If the set of null values is different for each
          summary field, you can create a separate cube for each summary field.
      in_related_table {Table View}:
          The table or table view to be related to the input features.
      related_location_id {Field}:
          An integer or text field in the related table that contains the
          location ID on which the relate will be based.

     OUTPUTS:
      output_cube (File):
          The output netCDF data cube that will be created.

        """