# Generated documentation for module arcpy.gapro


class SummarizeAttributes(object):
    """
    Calculates summary statistics for fields in a feature class.
    """

    @property
    def description(self) -> str:
        return """

        SummarizeAttributes_gapro(input_layer, out_table, {fields;fields...}, {summary_fields;summary_fields...}, {time_step_interval}, {time_step_repeat}, {time_step_reference})

        Calculates summary statistics for fields in a feature class.

     INPUTS:
      input_layer (Table View):
          The point, polyline, or polygon layer to be summarized.
      fields {Field}:
          A field or fields used to summarize similar features. For
          example, if you choose a single field calledwith the values of
          commercial and residential, all of the fields with the value
          residential fields will be summarized together, with summary
          statistics calculated, and all of the fields with the value commercial
          will be summarized together. This example will results in two rows in
          the output, one for commercial, and one for residential summary
          values. PropertyTypeYou can optionally select no fields and
          summarize all features in a
          single summary result.
      summary_fields {Value Table}:
          The statistics that will be calculated on specified fields.COUNT-The
          number of nonnull values. It can be used on numeric fields
          or strings. The count of [null, 0, 2] is 2.SUM-The sum of numeric
          values in a field. The sum of [null, null, 3]
          is 3.MEAN-The mean of numeric values. The mean of [0,2, null] is
          1.MIN-The minimum value of a numeric field. The minimum of [0, 2,
          null]
          is 0.MAX-The maximum value of a numeric field. The maximum value of
          [0, 2,
          null] is 2.STDDEV-The standard deviation of a numeric field. The
          standard
          deviation of [1] is null. The standard deviation of [null, 1,1,1] is
          null.VAR-The variance of a numeric field in a track. The variance of
          [1] is
          null. The variance of [null, 1,1,1] is null.RANGE-The range of a
          numeric field. This is calculated as the minimum
          value subtracted from the maximum value. The range of [0, null, 1] is
          1. The range of [null, 4] is 0.ANY-A sample string from a field of
          type string.
      time_step_interval {Time Unit}:
          A value that specifies the duration of the time step. This parameter
          is only available if the input points are time enabled and represent
          an instant in time.Time stepping can only be applied if time is
          enabled on the input.
      time_step_repeat {Time Unit}:
          A value that specifies how often the time-step interval occurs. This
          parameter is only available if the input points are time enabled and
          represent an instant in time.
      time_step_reference {Date}:
          A date that specifies the reference time with which to align the time
          steps. The default is January 1, 1970, at 12:00 a.m. This parameter is
          only available if the input points are time enabled and represent an
          instant in time.

     OUTPUTS:
      out_table (Table):
          A new table with the summarized attributes.

        """