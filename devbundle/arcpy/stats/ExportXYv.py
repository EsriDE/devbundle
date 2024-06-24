# Generated documentation for module arcpy.stats


class ExportXYv(object):
    """
    Exports feature class coordinates and attribute values to a space-, comma-, tab-, or semicolon-delimited ASCII text file.
    """

    @property
    def description(self) -> str:
        return """

        ExportXYv_stats(Input_Feature_Class, Value_Field;Value_Field..., Delimiter, Output_ASCII_File, Add_Field_Names_to_Output)

        Exports feature class coordinates and attribute values to a space-,
        comma-, tab-, or semicolon-delimited ASCII text file.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class from which the feature coordinates and attribute
          values will be exported.
      Value_Field (Field):
          The field or fields in the input feature class containing the values
          to export to an ASCII text file.
      Delimiter (String):
          Specifies how feature coordinates and attribute values will be
          separated in the output ASCII file.SPACE-Feature coordinates and
          attribute values will be separated by a
          space in the output. This is the default.COMMA-Feature coordinates and
          attribute values will be separated by a
          comma in the output.SEMI-COLON-Feature coordinates and attribute
          values will be separated
          by a semicolon in the output.TAB-Feature coordinates and attribute
          values will be separated by a
          tab in the output.
      Add_Field_Names_to_Output (Boolean):
          Specifies whether field names will be included as the first line in
          the output text file.ADD_FIELD_NAMES-Field names will be written to
          the output text
          file.NO_FIELD_NAMES-Field names will not be written to the output text
          file. This is the default.

     OUTPUTS:
      Output_ASCII_File (File):
          The ASCII text file that will contain the feature coordinates and
          attribute values.

        """