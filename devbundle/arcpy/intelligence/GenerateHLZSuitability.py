# Generated documentation for module arcpy.intelligence


class GenerateHLZSuitability(object):
    """
    Creates a helicopter landing zone (HLZ) suitability raster layer from reclassified slope, reclassified land cover, and obstacle buffers.
    """

    @property
    def description(self) -> str:
        return """

        GenerateHLZSuitability_intelligence(in_slope_raster, in_land_cover_raster, in_obstacle_buffer_features, out_raster)

        Creates a helicopter landing zone (HLZ) suitability raster layer from
        reclassified slope, reclassified land cover, and obstacle buffers.

     INPUTS:
      in_slope_raster (Raster Layer):
          The reclassified slope raster with values 1 (acceptable) and 2
          (acceptable with caution). All other values will be excluded from the
          analysis.
      in_land_cover_raster (Raster Layer):
          The reclassified land cover raster with values 1 (acceptable) and 2
          (acceptable with caution). All other values will be excluded from the
          analysis.
      in_obstacle_buffer_features (Feature Layer):
          Obstacle area features representing approach and departure safety
          buffers around obstacles.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster dataset.

        """