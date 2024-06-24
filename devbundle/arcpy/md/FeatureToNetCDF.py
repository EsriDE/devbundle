# Generated documentation for module arcpy.md


class FeatureToNetCDF(object):
    """
    Converts point features to a netCDF file.
    """

    @property
    def description(self) -> str:
        return """

        FeatureToNetCDF_md(in_features, fields_to_variables;fields_to_variables..., out_netCDF_file, {fields_to_dimensions;fields_to_dimensions...})

        Converts point features to a netCDF file.

     INPUTS:
      in_features (Feature Layer):
          The input point features.
      fields_to_variables (Value Table):
          The field or fields that will be used to create variables in the
          netCDF file.Four special fields-Shape.X, Shape.Y, Shape.Z, and
          Shape.M-can be used
          for exporting x-coordinates or longitude, y-coordinates or latitude,
          z-values, and m-values of input features, respectively.field-A field
          in the input feature attribute table.{variable}-The
          netCDF variable name{units}-The units of the data represented by the
          field
      fields_to_dimensions {Value Table}:
          The field or fields that will be used to create dimensions in the
          netCDF file.field-A field in the input feature attribute
          table.{dimension}-The
          netCDF dimension name{units}-The units of the data represented by the
          field

     OUTPUTS:
      out_netCDF_file (File):
          The output netCDF file. The file name must have an .nc extension.

        """