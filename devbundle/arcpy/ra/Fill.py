# Generated documentation for module arcpy.ra


class Fill(object):
    """
    Fills sinks in a surface raster to remove small imperfections in the data.
    """

    @property
    def description(self) -> str:
        return """

        Fill_ra(inputSurfaceRaster, outputName, {zLimit})

        Fills sinks in a surface raster to remove small imperfections in the
        data.

     INPUTS:
      inputSurfaceRaster (Image Service / Raster Layer / String):
          The input raster representing a continuous surface.
      outputName (String):
          The name of the output fill raster service.The default name is based
          on the tool name and the input layer name.
          If the layer name already exists, you will be prompted to provide
          another name.
      zLimit {Double}:
          Maximum elevation difference between a sink and its pour point to be
          filled.

        """