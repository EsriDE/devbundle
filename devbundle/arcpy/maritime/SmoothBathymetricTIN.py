# Generated documentation for module arcpy.maritime


class SmoothBathymetricTIN(object):
    """
    Smooths a triangulated irregular network (TIN) dataset in a manner that strictly preserves a shallow bias.
    """

    @property
    def description(self) -> str:
        return """

        SmoothBathymetricTIN_maritime(in_tin, out_tin, depth_direction, smoothing_iterations)

        Smooths a triangulated irregular network (TIN) dataset in a manner
        that strictly preserves a shallow bias.

     INPUTS:
      in_tin (TIN Layer):
          The input TIN that will be smoothed with a shallow bias.
      depth_direction (String):
          Specifies how the depth will be captured in the input
          TIN.POSITIVE_UP-The depth will be captured in the input TIN. This is
          default.POSITIVE_DOWN-The downward depth will be captured in the input
          TIN.
      smoothing_iterations (Long):
          The number of smoothing passes that will be performed over the TIN.

     OUTPUTS:
      out_tin (TIN):
          The output smoothed TIN.

        """