# Generated documentation for module arcpy.sa.Functions


class ZonalFill(object):
    """
    Fills zones using the minimum cell value from a weight raster along the zone boundary.
    """

    @property
    def description(self) -> str:
        return """

        ZonalFill_sa(in_zone_raster, in_weight_raster)

        Fills zones using the minimum cell value from a weight raster along
        the zone boundary.

     INPUTS:
      in_zone_raster (Composite Geodataset):
          The input raster that defines the zones to be filled.
      in_weight_raster (Composite Geodataset):
          The weight, or value, to be assigned to each zone.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster for which the zones have been filled.

        """