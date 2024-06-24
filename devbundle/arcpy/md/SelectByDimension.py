# Generated documentation for module arcpy.md


class SelectByDimension(object):
    """
    Updates the netCDF layer display or netCDF table view based on the dimension value.
    """

    @property
    def description(self) -> str:
        return """

        SelectByDimension_md(in_layer_or_table, {dimension_values;dimension_values...}, {value_selection_method})

        Updates the netCDF layer display or netCDF table view based on the
        dimension value.

     INPUTS:
      in_layer_or_table (Raster Layer / Feature Layer / Table View / Mosaic Layer):
          The input netCDF raster layer, netCDF feature layer, netCDF table
          view, or mosaic layer. If the input is a mosaic layer, it must be
          multidimensional.
      dimension_values {Value Table}:
          A set of dimension-value pairs used to specify a slice of a
          multidimensional variable.dimension-A netCDF dimension.{value}-A
          dimension value that specifies
          a slice of a multidimensional
          variable.
      value_selection_method {String}:
          Specifies the dimension value selection method that will be
          used.BY_VALUE-The input value will be matched with the actual
          dimension
          value.BY_INDEX-The input value will be matched with the position or
          index of
          a dimension value. The index is 0 based; that is, the position starts
          at 0.

        """