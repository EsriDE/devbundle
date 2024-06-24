# Generated documentation for module arcpy.defense


class FindLocalPeaksValleys(object):
    """
    Finds local peaks or valleys within a defined area.
    """

    @property
    def description(self) -> str:
        return """

        FindLocalPeaksValleys_defense(in_surface, out_feature_class, peak_valley_op_type, num_peaks_valleys, {in_feature})

        Finds local peaks or valleys within a defined area.

     INPUTS:
      in_surface (Raster Layer / Mosaic Dataset / Mosaic Layer):
          The input elevation raster surface.
      peak_valley_op_type (String):
          Specifies the type of operation the tool will perform.PEAKS-Local
          peaks will be found. This is the default.VALLEYS-Local
          valleys will be found.
      num_peaks_valleys (Long):
          The number of peaks or valleys to find.
      in_feature {Feature Set}:
          The input polygon feature class in which the local peaks or valleys
          will be found.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output point feature class containing the local peaks or valleys.

        """