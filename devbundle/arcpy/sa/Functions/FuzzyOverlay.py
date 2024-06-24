# Generated documentation for module arcpy.sa.Functions


class FuzzyOverlay(object):
    """
    Combine fuzzy membership rasters data together, based on selected overlay type.
    """

    @property
    def description(self) -> str:
        return """

        FuzzyOverlay_sa(in_rasters;in_rasters..., {overlay_type}, {gamma})

        Combine fuzzy membership rasters data together, based on selected
        overlay type.

     INPUTS:
      in_rasters (Composite Geodataset):
          A list of input membership rasters to be combined in the overlay.
      overlay_type {String}:
          Specifies the method used to combine two or more membership
          data.AND-The minimum of the fuzzy memberships from the input fuzzy
          rasters.OR-The maximum of the fuzzy memberships from the input
          rasters.PRODUCT-A decreasive function. Use this when the combination
          of
          multiple evidence is less important or smaller than any of the inputs
          alone.SUM-An increasive function. Use this when the combination of
          multiple
          evidence is more important or larger than any of the inputs alone.
          GAMMA-The algebraic product of the fuzzyand fuzzy, both
          raised to the power of gamma. SumProduct
      gamma {Double}:
          The gamma value to be used. This is only available when theis
          set to. Overlay typeGammaDefault value is 0.9.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster which is the result of applying the fuzzy
          operator.This output will always have a value between 0 and 1.

        """