# Generated documentation for module arcpy.management


class BatchUpdateFields(object):
    """
    Transforms fields in a table or feature class based on schema defined in the definition table and creates a new table or feature class.
    """

    @property
    def description(self) -> str:
        return """

        BatchUpdateFields_management(in_table, out_table, field_definition_table, {script_file}, {output_field_name}, {source_field_name}, {output_field_type}, {output_field_decimals_or_length}, {output_field_alias}, {output_field_script})

        Transforms fields in a table or feature class based on schema defined
        in the definition table and creates a new table or feature class.

     INPUTS:
      in_table (Table View):
          The input table or feature class.
      field_definition_table (Table View):
          A table containing the field definitions and calculations that will be
          used to create the output.
      script_file {File}:
          A Python file that stores multiple line Python functions to perform
          calculations for the out_table parameter fields.
      output_field_name {Field}:
          The field name from the definition table that contains the target
          field names for the output table.
      source_field_name {Field}:
          The field name from the definition table that contains the source
          field names from the input table.
      output_field_type {Field}:
          The field in theparameter value that defines the data types
          for the output table. The field is expected to be of Text type.
          Output Schema Definition TableThe field in the field_definition_table
          that defines the data types
          for the output table. The field is expected to be of Text type.The
          following values are supported:BigInteger-64-bit IntegerBlob-Binary
          Large
          ObjectDate-DateDateOnly-Date OnlyDouble-Double-precision floating-
          point numberGlobalID-Global IDGUID-Globally Unique IdentifierInteger
          (or Long)-32-bit IntegerRaster-RasterFloat (or Single)-Single-
          precision floating-point numberShort (or SmallInteger)-16-bit
          IntegerText (or String)-Character stringTimeOnly-Time
          OnlyTimestampOffset-Timestamp Offset
      output_field_decimals_or_length {Field}:
          The field name from the definition table that defines the number of
          decimals or the length of the field for the output fields.
      output_field_alias {Field}:
          The field name from the definition table that defines the alias names
          for the fields of the output table.
      output_field_script {Field}:
          The field name from the definition table that defines the calculations
          for the output fields.

     OUTPUTS:
      out_table (Feature Class / Table):
          The output table or feature class containing the updated fields.

        """