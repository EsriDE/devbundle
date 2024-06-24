# Generated documentation for module arcpy.sa.Functions


class Corridor(object):
    """
    Calculates the sum of accumulative costs for two input accumulative cost rasters.
    """

    @property
    def description(self) -> str:
        return """

        Corridor_sa(in_distance_raster1, in_distance_raster2)

        Calculates the sum of accumulative costs for two input accumulative
        cost rasters.

     INPUTS:
      in_distance_raster1 (Composite Geodataset):
          The first input distance raster.It should be an accumulated cost
          distance output from a distance tool
          such as Cost Distance or Path Distance.
      in_distance_raster2 (Composite Geodataset):
          The second input distance raster.It should be an accumulated cost
          distance output from a distance tool
          such as Cost Distance or Path Distance.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output corridor raster.The output raster is of floating-point
          type.

        """