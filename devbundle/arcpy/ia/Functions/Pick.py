# Generated documentation for module arcpy.ia.Functions


class Pick(object):
    """
    The value from a position raster is used to determine from which raster in a list of input rasters the output cell value will be obtained.
    """

    @property
    def description(self) -> str:
        return """

        Pick_ia(in_position_raster, in_rasters_or_constants;in_rasters_or_constants..., {process_as_multiband})

        The value from a position raster is used to determine from which
        raster in a list of input rasters the output cell value will be
        obtained.

     INPUTS:
      in_position_raster (Composite Geodataset):
          The input raster defining the position of the raster to use for the
          output value.The input can be an integer or float raster.
      in_rasters_or_constants (Composite Geodataset):
          The list of inputs from which the output value will be selected.The
          inputs can be integer or float rasters. A number can also be used
          as an input.
      process_as_multiband {Boolean}:
          Specifies how the input multiband raster bands will be
          processed.SINGLE_BAND-Each band from a multiband raster input will be
          processed
          separately as a single band raster. This is the
          default.MULTI_BAND-Each multiband raster input will be processed as a
          multiband raster. The operation will be performed for each band from
          one input using the corresponding band number from the other inputs.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.

        """