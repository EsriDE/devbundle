# Generated documentation for module arcpy.md


class MakeNetCDFTableView(object):
    """
    Makes a table view from a netCDF file.
    """

    @property
    def description(self) -> str:
        return """

        MakeNetCDFTableView_md(in_netCDF_file, variable;variable..., out_table_view, {row_dimension;row_dimension...}, {dimension_values;dimension_values...}, {value_selection_method})

        Makes a table view from a netCDF file.

     INPUTS:
      in_netCDF_file (File):
          The input netCDF file.
      variable (String):
          The netCDF variable, or variables, used to create fields in the table
          view.
      row_dimension {String}:
          The netCDF dimension, or dimensions, used to create fields populated
          with unique values in the table view. The dimension, or dimensions,
          set here determine the number of rows in the table view and the fields
          that will be present.For instance, if stationID is a dimension in the
          netCDF file and has
          10 values, by setting stationID as the dimension to use, 10 rows will
          be created in the table view. If stationID and time are used and there
          are 3 time slices, 30 rows will be created in the table view.
      dimension_values {Value Table}:
          A set of dimension-value pairs used to specify a slice of a
          multidimensional variable.dimension-A netCDF dimension.{value}-The
          dimension value to use.
      value_selection_method {String}:
          Specifies the dimension value selection method that will be
          used.BY_VALUE-The input value will be matched with the actual
          dimension
          value.BY_INDEX-The input value will be matched with the position or
          index of
          a dimension value. The index is 0 based; that is, the position starts
          at 0.

     OUTPUTS:
      out_table_view (Table View):
          The name of the output table view.

        """