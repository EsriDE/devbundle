# Generated documentation for module arcpy.md


class TableToNetCDF(object):
    """
    Converts a table to a netCDF file.
    """

    @property
    def description(self) -> str:
        return """

        TableToNetCDF_md(in_table, fields_to_variables;fields_to_variables..., out_netCDF_file, {fields_to_dimensions;fields_to_dimensions...})

        Converts a table to a netCDF file.

     INPUTS:
      in_table (Table View):
          The input table.
      fields_to_variables (Value Table):
          The field or fields that will be used to create variables in the
          netCDF file.field-A field in the input feature attribute
          table.{variable}-The
          netCDF variable name{units}-The units of the data represented by the
          field
      fields_to_dimensions {Value Table}:
          The field or fields that will be used to create dimensions in the
          netCDF file.field-A field in the input table.{dimension}-The netCDF
          dimension
          name{units}-The units of the data represented by the field

     OUTPUTS:
      out_netCDF_file (File):
          The output netCDF file. The file name must have an .nc extension.

        """