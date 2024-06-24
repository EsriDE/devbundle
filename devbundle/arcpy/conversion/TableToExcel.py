# Generated documentation for module arcpy.conversion


class TableToExcel(object):
    """
    Converts a table to a Microsoft Excel file (.xls or .xlsx).
    """

    @property
    def description(self) -> str:
        return """

        TableToExcel_conversion(Input_Table;Input_Table..., Output_Excel_File, {Use_field_alias_as_column_header}, {Use_domain_and_subtype_description})

        Converts a table to a Microsoft Excel file (.xls or .xlsx).

     INPUTS:
      Input_Table (Table View):
          The table or tables to be converted to an Excel file.
      Use_field_alias_as_column_header {Boolean}:
          Specifies whether input field names or field aliases will be used as
          the output column names.NAME-Column headers will be set using the
          input field names. This is
          the default.ALIAS-Column headers will be set using the input
          geodatabase table's
          field aliases. If the input is a layer in a map, the value set on the
          layer's field alias is ignored.
      Use_domain_and_subtype_description {Boolean}:
          Specifies whether values from subtype fields or fields with a coded
          value domain will be transferred to the output.CODE-All field values
          will be used as they are stored in the table.
          This is the default.DESCRIPTION-For subtype fields, the subtype
          description will be used.
          For fields with a coded value domain, the coded value descriptions
          will be used.

     OUTPUTS:
      Output_Excel_File (File):
          The output Excel file. Specify the format of the Excel file using the
          .xls or .xlsx file extension.

        """