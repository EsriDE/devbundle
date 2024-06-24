# Generated documentation for module arcpy.analysis


class Statistics(object):
    """
    Calculates summary statistics for fields in a table.
    """

    @property
    def description(self) -> str:
        return """

        Statistics_analysis(in_table, out_table, statistics_fields;statistics_fields..., {case_field;case_field...}, {concatenation_separator})

        Calculates summary statistics for fields in a table.

     INPUTS:
      in_table (Table View / Raster Layer):
          The input table containing the fields that will be used to calculate
          statistics.
      statistics_fields (Value Table):
          Specifies the field or fields containing the attribute values that
          will be used to calculate the specified statistic. Multiple statistic
          and field combinations can be specified. Null values are excluded from
          all calculations.Text attribute fields can be summarized using first
          and last
          statistics. Numeric attribute fields can be summarized using any
          statistic. Date, Date only, and Timestamp offset attribute fields can
          be summarized only with the mean, minimum, maximum, count, first,
          last, unique, and concatenate statistics.Available statistics types
          are as follows:SUM-The values for the specified field will be added
          together.MEAN-The
          average for the specified field will be calculated.MIN-The smallest
          value for all records of the specified field will be
          identified.MAX-The largest value for all records of the specified
          field will be
          identified.RANGE-The range of values (maximum minus minimum) for the
          specified
          field will be calculated.STD-The standard deviation of values for the
          specified field will be
          calculated.COUNT-The number of values included in the calculations
          will be
          identified. Each value will be counted except null values. To
          determine the number of null values in a field, create a count on the
          field in question, create a count on a different field that does not
          contain null values (for example, the OID if present), and subtract
          the two values.FIRST-The specified field value of the first record in
          the input will
          be used.LAST-The specified field value of the last record in the input
          will be
          used.MEDIAN-The median for all records of the specified field will be
          calculated.VARIANCE-The variance for all records of the specified
          field will be
          calculated.UNIQUE-The number of unique values of the specified field
          will be
          counted.CONCATENATE-The values for the specified field will be
          concatenated.
          The values can be separated using the concatenation_separator
          parameter.
      case_field {Field}:
          The field or fields in the input that will be used to calculate
          statistics separately for each unique attribute value (or combination
          of attribute values when multiple fields are specified).
      concatenation_separator {String}:
          A character or characters that will be used to concatenate values when
          the CONCATENATION option is used for the statistics_fields parameter.
          By default, the tool will concatenate values without a separator.

     OUTPUTS:
      out_table (Table):
          The output table that will store the calculated statistics.

        """