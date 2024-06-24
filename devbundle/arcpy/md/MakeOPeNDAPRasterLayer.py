# Generated documentation for module arcpy.md


class MakeOPeNDAPRasterLayer(object):
    """
    Creates a raster layer from data stored on an OPeNDAP server.
    """

    @property
    def description(self) -> str:
        return """

        MakeOPeNDAPRasterLayer_md(in_opendap_URL, variable, x_dimension, y_dimension, out_raster_layer, {extent}, {dimension_values;dimension_values...}, {value_selection_method}, {cell_registration})

        Creates a raster layer from data stored on an OPeNDAP server.

     INPUTS:
      in_opendap_URL (File / String):
          The URL that references the remote OPeNDAP dataset. The URL should
          resolve to the dataset level (for example, file name), not a directory
          name.
      variable (String):
          The variable from the OPeNDAP dataset that will be used to create the
          raster layer.
      x_dimension (String):
          The dimension of the OPeNDAP dataset used to define the x, or
          longitude, coordinates of the output raster layer.
      y_dimension (String):
          The dimension of the OPeNDAP dataset used to define the y, or
          latitude, coordinates of the output raster layer.
      extent {Envelope}:
          The output extent of the raster layer. Specify the extent coordinates
          in the units of the OPeNDAP data source (these could be latitude-
          longitude, projected coordinates, or some arbitrary grid coordinates).
          The purpose of this parameter is to allow subsetting to an area of
          interest or to reduce the size of the data that is transferred.
      dimension_values {Value Table}:
          The starting and ending values of the dimensions or dimensions used to
          constrain which data will be extracted from the remote OPeNDAP server.
          By default, the minimum and maximum values of the dimension or
          dimensions will be used.dimension-A netCDF dimension.{start_value}-The
          start value to use for
          the specified dimension.{end_value}-The end value to use.
      value_selection_method {String}:
          Specifies the dimension value selection method that will be
          used.BY_VALUE-The input value will be matched with the actual
          dimension
          value.BY_INDEX-The input value will be matched with the position or
          index of
          a dimension value. The index is 0 based; that is, the position starts
          at 0.
      cell_registration {String}:
          Specifies how the cells will be registered with respect to the x,y
          coordinate.CENTER-The x,y coordinate represents the center of the
          cell. This is
          the default.LOWER_LEFT-The x,y coordinate represents the lower left of
          the cell.UPPER_LEFT-The x,y coordinate represents the upper left of
          the cell.

     OUTPUTS:
      out_raster_layer (Raster Layer):
          The name of the output raster layer.

        """