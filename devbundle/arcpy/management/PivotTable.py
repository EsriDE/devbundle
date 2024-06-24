# Generated documentation for module arcpy.management


class PivotTable(object):
    """
    Creates a table from the input table by reducing redundancy in records and flattening one-to-many relationships.
    """

    @property
    def description(self) -> str:
        return """

        PivotTable_management(in_table, fields;fields..., pivot_field, value_field, out_table)

        Creates a table from the input table by reducing redundancy in records
        and flattening one-to-many relationships.

     INPUTS:
      in_table (Table View):
          The table containing the records that will be pivoted.
      fields (Field):
          The fields that define the records that will be included in the output
          table.
      pivot_field (Field):
          The field whose record values will be used to generate the field names
          in the output table.
      value_field (Field):
          The field whose values will populate the pivoted fields in the output
          table.

     OUTPUTS:
      out_table (Table):
          The table that will be created containing the pivoted records.

        """