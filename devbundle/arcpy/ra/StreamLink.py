# Generated documentation for module arcpy.ra


class StreamLink(object):
    """
    Assigns unique values to sections of a raster linear network between intersections.
    """

    @property
    def description(self) -> str:
        return """

        StreamLink_ra(inputStreamRaster, inputFlowDirectionRaster, outputName)

        Assigns unique values to sections of a raster linear network between
        intersections.

     INPUTS:
      inputStreamRaster (Image Service / Raster Layer / String):
          An input raster that represents a linear stream network.
      inputFlowDirectionRaster (Image Service / Raster Layer / String):
          The input raster that shows the direction of flow out of each cell.
      outputName (String):
          The name of the output stream link raster service.The default name is
          based on the tool name and the input layer name.
          If the layer name already exists, you will be prompted to provide
          another name.

        """