# Generated documentation for module arcpy.sa.Functions


class IsNull(object):
    """
    Determines which values from the input raster are NoData on a cell-by- cell basis.
    """

    @property
    def description(self) -> str:
        return """

        IsNull_sa(in_raster)

        Determines which values from the input raster are NoData on a cell-by-
        cell basis.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster being tested to identify the cells that are NoData
          (null).The input can be either integer or floating-point type.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The output identifies with an integer value of 1
          which cells in the
          input are NoData. If the input is any other value, the output is 0.

        """