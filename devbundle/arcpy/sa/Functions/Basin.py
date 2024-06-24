# Generated documentation for module arcpy.sa.Functions


class Basin(object):
    """
    Creates a raster delineating all drainage basins.
    """

    @property
    def description(self) -> str:
        return """

        Basin_sa(in_flow_direction_raster)

        Creates a raster delineating all drainage basins.

     INPUTS:
      in_flow_direction_raster (Composite Geodataset):
          The input raster that shows the direction of flow out of each cell.A
          flow direction raster can be created with the Flow Direction tool,
          using the default D8 flow direction type .

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster that delineates the drainage basins.This output is
          of integer type.

        """