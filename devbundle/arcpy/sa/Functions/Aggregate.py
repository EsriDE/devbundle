# Generated documentation for module arcpy.sa.Functions


class Aggregate(object):
    """
    Generates a reduced-resolution version of a raster. Each output cell contains the Sum, Minimum, Maximum, Mean, or Median of the input cells that are encompassed by the extent of that cell.
    """

    @property
    def description(self) -> str:
        return """

        Aggregate_sa(in_raster, cell_factor, {aggregation_type}, {extent_handling}, {ignore_nodata})

        Generates a reduced-resolution version of a raster. Each output cell
        contains the Sum, Minimum, Maximum, Mean, or Median of the input cells
        that are encompassed by the extent of that cell.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster to be aggregated.It can be of integer or floating
          point type.
      cell_factor (Long):
          The factor by which the cell size of the input raster will be
          multiplied. The value must be an integer greater than 1.For example, a
          cell factor value of 3 results in an output cell size
          three times larger than that of the input raster.
      aggregation_type {String}:
          The method that will be used for aggregation.The values of the input
          cells encompassed by the coarser output cells
          are aggregated by one of the following statistics:SUM-The total of the
          input cell values. This is the
          default.MAXIMUM-The largest value of the input cells.MEAN-The average
          value of the input cells.MEDIAN-The median value of the input
          cells.MINIMUM-The smallest value of the input cells.
      extent_handling {Boolean}:
          Specifies whether the boundaries of the input raster will be expanded
          when its rows or columns are not a multiple of the cell factor.
          EXPAND-The top or right boundaries of the input raster will
          be expanded so the total number of cells in a row or column is a
          multiple of the cell factor. Those expanded cells are given a value of
          NoData when put into the calculation. With this option, the
          output raster can cover a larger spatial extent
          than the input raster. This is the default. TRUNCATE-The
          number of rows or columns will be reduced by 1
          in the output raster. This truncates the remaining cells on the top or
          right boundaries of the input raster, making the number of rows or
          columns in the input raster a multiple of the cell factor.
          With this option, the output raster can cover a smaller spatial extent
          than the input raster.If the number of rows and columns in the input
          raster is a multiple of
          the cell_factor, these keywords are not used.
      ignore_nodata {Boolean}:
          Denotes whether NoData values are ignored by the aggregation
          calculation. DATA-Specifies that if NoData values exist for
          any of the
          cells that fall within the spatial extent of a larger cell on the
          output raster, the NoData values will be ignored when determining the
          value for output cell locations. Only input cells within the extent of
          the output cell that have data values will be used in determining the
          value of the output cell. This is the default.
          NODATA-Specifies that if any cell that falls within the
          spatial extent of a larger cell on the output raster has a value of
          NoData, the value for that output cell location will be NoData.
          When this option is used, it is implied that when cells within an
          aggregation contain the NoData value, there is insufficient
          information to perform the specified calculations necessary to
          determine an output value.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output aggregated raster.It is a reduced-resolution version of the
          input raster.

        """