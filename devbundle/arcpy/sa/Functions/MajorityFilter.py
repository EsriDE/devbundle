# Generated documentation for module arcpy.sa.Functions


class MajorityFilter(object):
    """
    Replaces cells in a raster based on the majority of their contiguous neighboring cells.
    """

    @property
    def description(self) -> str:
        return """

        MajorityFilter_sa(in_raster, {number_neighbors}, {majority_definition})

        Replaces cells in a raster based on the majority of their contiguous
        neighboring cells.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster to be filtered based on the majority of contiguous
          neighboring cells.It must be of integer type.
      number_neighbors {String}:
          Determines the number of neighboring cells to use in the kernel of the
          filter.FOUR-The kernel of the filter will be the four direct
          (orthogonal)
          neighbors to the present cell. This is the default.EIGHT-The kernel of
          the filter will be the eight nearest neighbors (a
          three-by-three window) to the present cell.
      majority_definition {String}:
          Specifies the number of contiguous (spatially connected) cells that
          must be of the same value before a replacement will occur.MAJORITY-A
          majority of cells must have the same value and be
          contiguous. Three out of four or five out of eight connected cells
          must have the same value.HALF-Half of the cells must have the same
          value and be contiguous. Two
          out of four or four out of eight connected cells must have the same
          value. This option will have a more smoothing effect than the other.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output filtered raster.The output is always of integer type.

        """