# Generated documentation for module arcpy.management


class UnsplitLine(object):
    """
    Aggregates line features that have coincident endpoints and, optionally, common attribute values.
    """

    @property
    def description(self) -> str:
        return """

        UnsplitLine_management(in_features, out_feature_class, {dissolve_field;dissolve_field...}, {statistics_fields;statistics_fields...}, {concatenation_separator})

        Aggregates line features that have coincident endpoints and,
        optionally, common attribute values.

     INPUTS:
      in_features (Feature Layer):
          The line features to be aggregated.
      dissolve_field {Field}:
          The field or fields on which features will be aggregated. If no fields
          are specified, the tool will dissolve all features together.
      statistics_fields {Value Table}:
          Specifies the field or fields containing the attribute values that
          will be used to calculate the specified statistic. Multiple statistic
          and field combinations can be specified. Null values are excluded from
          all calculations.By default, the tool will not calculate any
          statistics.Text attribute fields can be summarized using first and
          last
          statistics. Numeric attribute fields can be summarized using any
          statistic.Available statistics types are as follows:SUM-The values for
          the specified field will be added together.MEAN-The
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
      concatenation_separator {String}:
          A character or characters that will be used to concatenate values when
          the CONCATENATION option is used for the statistics_fields parameter.
          By default, the tool will concatenate values without a separator.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class to be created that will contain the aggregated
          features.

        """