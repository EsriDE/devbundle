# Generated documentation for module arcpy.intelligence


class DropZones(object):
    """
    Identifies drop zone locations suitable for parachuting equipment or personnel within a designated area of interest given slope and vegetation data.
    """

    @property
    def description(self) -> str:
        return """

        DropZones_intelligence(in_slope_raster, in_vegetation_features, clip_features, out_feature_class)

        Identifies drop zone locations suitable for parachuting equipment or
        personnel within a designated area of interest given slope and
        vegetation data.

     INPUTS:
      in_slope_raster (Raster Layer):
          The slope raster percentage used to determine the slope component of
          DZ suitability.
      in_vegetation_features (Feature Layer):
          The features that define the combined vegetation and land cover types.
          These features will be used to find areas with suitable vegetation
          coverage for DZs.
      clip_features (Feature Set):
          The area within which suitable DZs will be found.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class showing terrain suitability for DZs.

        """