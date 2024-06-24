# Generated documentation for module arcpy.sa.Functions


class Fill(object):
    """
    Fills sinks in a surface raster to remove small imperfections in the data.
    """

    @property
    def description(self) -> str:
        return """

        Fill_sa(in_surface_raster, {z_limit})

        Fills sinks in a surface raster to remove small imperfections in the
        data.

     INPUTS:
      in_surface_raster (Composite Geodataset):
          The input raster representing a continuous surface.
      z_limit {Double}:
          Maximum elevation difference between a sink and its pour point to be
          filled.If the difference in z-values between a sink and its pour point
          is
          greater than the z_limit, that sink will not be filled.The value for
          z-limit must be greater than zero.Unless a value is specified for this
          parameter, all sinks will be
          filled, regardless of depth.

     OUTPUTS:
      out_surface_raster (Raster Dataset):
          The output surface raster after the sinks have been filled.If the
          surface raster is integer, the output filled raster will be
          integer type. If the input is floating point, the output raster will
          be floating point.

        """