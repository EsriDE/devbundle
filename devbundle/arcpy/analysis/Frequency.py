# Generated documentation for module arcpy.analysis


class Frequency(object):
    """
    Reads a table and a set of fields and creates a new table containing unique field values and the number of occurrences of each unique field value.
    """

    @property
    def description(self) -> str:
        return """

        Frequency_analysis(in_table, out_table, frequency_fields;frequency_fields..., {summary_fields;summary_fields...})

        Reads a table and a set of fields and creates a new table containing
        unique field values and the number of occurrences of each unique field
        value.

     INPUTS:
      in_table (Table View / Raster Layer):
          The table containing the field(s) that will be used to calculate
          frequency statistics.
      frequency_fields (Field):
          The field(s) used to calculate frequency statistics. Each unique
          combination of field values will be included as a new row in the
          output table.
      summary_fields {Field}:
          The attribute field(s) to sum and add to the output table. Values will
          be summed for each unique combination of frequency fields. Null values
          are excluded from this calculation.

     OUTPUTS:
      out_table (Table):
          The output table that will store the frequency statistics.

        """