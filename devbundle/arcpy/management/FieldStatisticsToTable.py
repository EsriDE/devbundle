# Generated documentation for module arcpy.management


class FieldStatisticsToTable(object):
    """
    Creates a table of descriptive statistics for one or more input fields in a table or feature class.
    """

    @property
    def description(self) -> str:
        return """

        FieldStatisticsToTable_management(in_table, in_fields;in_fields..., out_location, out_tables;out_tables..., {group_by_field}, {out_statistics;out_statistics...})

        Creates a table of descriptive statistics for one or more input fields
        in a table or feature class.

     INPUTS:
      in_table (Table View):
          The input table containing the fields that will be used to create the
          statistics table.
      in_fields (Field):
          The fields containing the values that will be used to calculate the
          statistics.
      out_location (Workspace):
          The location where the output tables will be created. The location can
          be a geodatabase, folder, or feature dataset.
      out_tables (Value Table):
          The output tables containing the statistics. The field_type column
          specifies the field types that will be included in each output table,
          and the name of each output table is provided in the output_name
          column. For example, you can create a single table with summaries of
          all field types, or you can create separate tables for summaries of
          Numeric, Text, and Date field types. The following options are
          available for the field_type column:
          NUMERIC-A table summarizing numeric fields of the input (Short, Long,
          Big Integer, Float, and Double types) will be created.TEXT-A table
          summarizing text fields of the input (Text type) will be
          created.DATE-A table summarizing date fields of the input (Date, Date
          Only,
          Time Only and Timestamp Offset types) will be created.ALL-A table
          summarizing all numeric, text, and date fields of the
          input will be created. Output fields containing statistics that apply
          to multiple field types will be saved as type Text. Output statistics
          that do not apply to Text and Date type fields will be empty.
      group_by_field {Field}:
          The field that will be used to group rows into categories. If a group
          by field is provided, each field of the input will appear as a row in
          the output table once per unique value in the group by field.
      out_statistics {Value Table}:
          Specifies the statistics that will be summarized and the names of the
          output fields containing the statistics. The statistic is provided in
          the out_statistic column, and the name of the output field is provided
          in the output_name column. If no values are provided, all applicable
          statistics will be calculated for all input fields. The
          following options are available for the out_statistic
          column (only statistics applicable to the input fields will be
          available):        FIELDNAME-The name of the field.ALIAS-The alias of
          the
          field.FIELDTYPE-The field type of the field (Short, Long, Double,
          Float,
          Text, or Date).NULLS-The number of records containing null values of
          the field.MINIMUM-The smallest value in the field.MAXIMUM-The largest
          value in the field.MEAN-The mean (sum divided by total count) of all
          values in the field.
          To calculate the mean date for date fields, each date is converted to
          a number by calculating the difference between the date and a
          reference date (for example, 1900-01-01), calculated in
          milliseconds.STANDARDDEVIATION-The standard deviation of the values in
          the field.
          It is calculated as the square root of the variance, in which the
          variance is the average squared difference of each value from the mean
          of the field.MEDIAN-The median for all values in the field. The median
          is the
          middle value in the sorted list of values. If there is an even number
          of values, the median is the mean of the two middle values in the
          distribution.COUNT-The number of nonnull values in the
          field.NUMBEROFUNIQUEVALUES-The number of unique values in the
          field.MODE-The most frequently occurring value in the
          field.LEASTCOMMON-The least common value in the field.OUTLIERS-The
          number of records with outlier values in the field.
          Outliers are values that are more than 1.5 times the interquartile
          range above the third quartile or below the first quartile of the
          values of the field.SUM-The sum of all values in the field.RANGE-The
          difference between the largest and smallest values in the
          field.INTERQUARTILERANGE-The range between the first quartile and the
          third
          quartile of the values in the field. This represents the range of the
          middle half of the data.FIRSTQUARTILE-The value of the first quartile
          of the field. Quartiles
          divide the sorted list of values into four groups containing equal
          numbers of values. The first quartile is the upper limit of the first
          group in ascending order.THIRDQUARTILE-The value of the third quartile
          of the field. Quartiles
          divide the sorted list of values into four groups containing equal
          numbers of values. The third quartile is the upper limit of the third
          group in ascending order.COEFFICIENTOFVARIATION-The coefficient of
          variation of the values in
          the field. The coefficient of variation is a measure of the relative
          spread of the values. It is calculated as the standard deviation
          divided by the mean of the field.SKEWNESS-The skewness of the values
          in the field. Skewness measures
          the symmetry of the distribution. The skewness is calculated as the
          third moment (the average of the cubed data values) divided by the
          cubed standard deviation.KURTOSIS-The kurtosis of the values in the
          field. Kurtosis describes
          the heaviness of the tails of a distribution compared to the normal
          distribution, helping identify the frequency of extreme values. The
          kurtosis is calculated as the fourth moment (the average of the data
          values taken to the fourth power) divided by the fourth power of the
          standard deviation.

        """