# Generated documentation for module arcpy.management


class EncodeField(object):
    """
    Converts categorical values (string, integer, or date) into multiple numerical fields, each representing a category. The encoded numerical fields can be used in most data science and statistical workflows including regression models.
    """

    @property
    def description(self) -> str:
        return """

        EncodeField_management(in_table, field, {method}, {time_step_interval}, {time_step_alignment}, {reference_time})

        Converts categorical values (string, integer, or date) into multiple
        numerical fields, each representing a category. The encoded numerical
        fields can be used in most data science and statistical workflows
        including regression models.

     INPUTS:
      in_table (Table View / Raster Layer / Mosaic Layer):
          The input table or feature class containing the field to be encoded.
          Fields will be added to the existing input table and will not create a
          new output table.
      field (Field):
          The field containing the categorical or temporal values to be encoded.
      method {String}:
          Specifies the method to use to encode the values contained in
          theparameter. Field to EncodeONEHOT-Each categorical value will
          be converted to a new field and the
          values 0 and 1 will be assigned, where 1 represents the presence of
          that categorical value. This is the default.ONECOLD-Each categorical
          value will be converted to a new field and
          the values 0 and 1 will be assigned, where 0 represents the presence
          of that categorical value. TEMPORAL-Each temporal value in
          theparameter will be
          converted to an integer based on the time step interval, time step
          alignment, and reference time specified. Field to Encode
      time_step_interval {Time Unit}:
          The number of seconds, minutes, hours, days, weeks, or years that will
          represent a single time step. The temporal value will be aggregated
          into a certain time step it is within. If no value is provided, the
          default time step interval is based on two algorithms that are used to
          determine the optimal number and width of the time step intervals. The
          smaller of the two results is used as the time step interval.
      time_step_alignment {String}:
          Specifies how aggregation will occur based on theparameter
          value. Time Step IntervalEND_TIME-Time steps will align to the
          last time event and aggregate
          back in time. This is the default.START_TIME-Time steps will align to
          the first time event and
          aggregate forward in time. REFERENCE_TIME-Time steps will
          align to the date and time
          specified in theparameter. Aggregation is performed forward and
          backward in time from the reference time until reaching the first and
          last temporal values. Reference Time
      reference_time {Date}:
          The date and time to which the time-step intervals will align. For
          example, to bin your data weekly from Monday to Sunday, set a
          reference time of Sunday at midnight to ensure that the time steps
          break between Sunday and Monday at midnight.The value can be a date
          and time or solely a date; it cannot be solely
          a time. The expected format is determined by the computer's regional
          time settings.

        """