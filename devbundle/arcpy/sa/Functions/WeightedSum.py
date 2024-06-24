# Generated documentation for module arcpy.sa.Functions


class WeightedSum(object):
    """
    Overlays several rasters, multiplying each by their given weight and summing them together.
    """

    @property
    def description(self) -> str:
        return """

        WeightedSum_sa(in_weighted_sum_table)

        Overlays several rasters, multiplying each by their given weight and
        summing them together.

     INPUTS:
      in_weighted_sum_table (Weighted Sum):
          The Weighted Sum tool overlays several rasters, multiplying each by
          their given weight and summing them together.An Overlay class is used
          to define the table. The WSTable object is
          used to specify a Python list of input rasters and weight them
          accordingly. The form of the object is:
          WSTable(weightedSumTable)

     OUTPUTS:
      out_raster (Raster Dataset):
          The output weighted raster.It will be of floating-point type.

        """