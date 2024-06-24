# Generated documentation for module arcpy.md


class MakeNetCDFRasterLayer(object):
    """
    Makes a raster layer from a netCDF file.
    """

    @property
    def description(self) -> str:
        return """

        MakeNetCDFRasterLayer_md(in_netCDF_file, variable, x_dimension, y_dimension, out_raster_layer, {band_dimension}, {dimension_values;dimension_values...}, {value_selection_method}, {cell_registration})

        Makes a raster layer from a netCDF file.

     INPUTS:
      in_netCDF_file (File):
          The input netCDF file.
      variable (String):
          The variable of the netCDF file used to assign cell values to the
          output raster. This is the variable that will be displayed, such as
          temperature or rainfall.
      x_dimension (String):
          A netCDF dimension used to define the x, or longitude, coordinates of
          the output layer.
      y_dimension (String):
          A netCDF dimension used to define the y, or latitude, coordinates of
          the output layer.
      band_dimension {String}:
          A netCDF dimension used to create bands in the output raster. Set this
          dimension if a multiband raster layer is required. For instance,
          altitude might be set as the band dimension to create a multiband
          raster where each band represents temperature at that altitude.
      dimension_values {Value Table}:
          The value (such as 01/30/05) of the dimension (such as time) or
          dimensions to use when displaying the variable in the output layer. By
          default, the first value of the dimension or dimensions will be
          used.dimension-A netCDF dimension.{value}-The dimension value to use.
      value_selection_method {String}:
          Specifies the dimension value selection method that will be
          used.BY_VALUE-The input value will be matched with the actual
          dimension
          value.BY_INDEX-The input value will be matched with the position or
          index of
          a dimension value. The index is 0 based; that is, the position starts
          at 0.
      cell_registration {String}:
          Specifies the location of the cell registration.CENTER-Cell
          registration at the center of the cell. This is the
          default.LOWER_LEFT-Cell registration at the lower left of the
          cell.UPPER_LEFT-Cell registration at the upper left of the cell.

     OUTPUTS:
      out_raster_layer (Raster Layer):
          The name of the output raster layer.

        """