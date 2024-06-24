# Generated documentation for module arcpy.sa.Functions


class WeightedOverlay(object):
    """
    Overlays several rasters using a common measurement scale and weights each according to its importance.
    """

    @property
    def description(self) -> str:
        return """

        WeightedOverlay_sa(in_weighted_overlay_table)

        Overlays several rasters using a common measurement scale and weights
        each according to its importance.

     INPUTS:
      in_weighted_overlay_table (Weighted Overlay Table):
          The Weighted Overlay tool allows the calculation of a multiple-
          criteria analysis between several rasters.An Overlay class is used to
          define the table. The WOTable object is
          used to specify the criteria rasters and their respective properties.
          The form of the object is:
          WOTable(weightedOverlayTable, evaluationScale)

     OUTPUTS:
      out_raster (Raster Dataset):
          The output weighted raster.

        """