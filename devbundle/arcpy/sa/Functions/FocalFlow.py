# Generated documentation for module arcpy.sa.Functions


class FocalFlow(object):
    """
    Determines the flow of the values in the input raster within each cell's immediate neighborhood.
    """

    @property
    def description(self) -> str:
        return """

        FocalFlow_sa(in_surface_raster, {threshold_value})

        Determines the flow of the values in the input raster within each
        cell's immediate neighborhood.

     INPUTS:
      in_surface_raster (Composite Geodataset):
          The input surface raster for which to calculate the focal flow.The
          eight immediate neighbors of each cell are evaluated to determine
          the flow.The input raster can be integer or floating-point.
      threshold_value {Double}:
          Defines a value that constitutes the threshold, which must be equaled
          or exceeded before flow can occur.The threshold value can be either an
          integer or floating-point value.If the difference between the value at
          a neighboring cell location and
          the value of the processing cell is less than or equal to the
          threshold value, the output will be 0 (or no flow).

     OUTPUTS:
      out_raster (Raster Dataset):
          The output focal flow raster.The output raster is always of integer
          type.

        """