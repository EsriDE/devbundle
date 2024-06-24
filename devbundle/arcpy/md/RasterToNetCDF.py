# Generated documentation for module arcpy.md


class RasterToNetCDF(object):
    """
    Converts a raster dataset to a netCDF file.
    """

    @property
    def description(self) -> str:
        return """

        RasterToNetCDF_md(in_raster, out_netCDF_file, {variable}, {variable_units}, {x_dimension}, {y_dimension}, {band_dimension}, {fields_to_dimensions;fields_to_dimensions...}, {compression_level})

        Converts a raster dataset to a netCDF file.

     INPUTS:
      in_raster (Raster Layer):
          The input raster dataset.
      variable {String}:
          The netCDF variable name that will be used in the output netCDF file.
          This variable will contain the values of cells in the input raster.
      variable_units {String}:
          The units of the data contained within the variable. The
          variable name is specified in theparameter. Variable
      x_dimension {String}:
          The netCDF dimension name that will be used to specify x, or
          longitude, coordinates.
      y_dimension {String}:
          The netCDF dimension name that will be used to specify y, or latitude,
          coordinates.
      band_dimension {String}:
          The netCDF dimension name that will be used to specify bands.
      fields_to_dimensions {Value Table}:
          The field or fields that will be used to create dimensions in the
          netCDF file.field-A field in the input raster attribute
          table.{dimension}-The
          netCDF dimension name{units}-The units of the data represented by the
          field
      compression_level {Long}:
          The level at which the output netCDF file will be compressed. The
          default value is 0, which implies no compression. A value of 9
          represents maximum compression.

     OUTPUTS:
      out_netCDF_file (File):
          The output netCDF file. The file name must have an .nc extension.

        """