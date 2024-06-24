# Generated documentation for module arcpy.sa.Functions


class BandCollectionStats(object):
    """
    Calculates the statistics for a set of raster bands.
    """

    @property
    def description(self) -> str:
        return """

        BandCollectionStats_sa(in_raster_bands;in_raster_bands..., out_stat_file, {compute_matrices})

        Calculates the statistics for a set of raster bands.

     INPUTS:
      in_raster_bands (Composite Geodataset):
          The input raster bands.They can be integer or floating point type.
      compute_matrices {Boolean}:
          Specifies whether covariance and correlation matrices are
          calculated.BRIEF-Only the basic statistical measures (minimum,
          maximum, mean, and
          standard deviation) will be calculated for every layer. This is the
          default.DETAILED-In addition to the standard statistics calculated
          with
          {BRIEF}, the covariance and correlation matrices will also be
          determined.

     OUTPUTS:
      out_stat_file (File):
          The output ASCII file containing the statistics.A .txt extension is
          required.

        """