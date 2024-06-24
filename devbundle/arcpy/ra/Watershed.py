# Generated documentation for module arcpy.ra


class Watershed(object):
    """
    Determines the contributing area above a set of cells in a raster.
    """

    @property
    def description(self) -> str:
        return """

        Watershed_ra(inputFlowDirectionRaster, inPourPointRasterOrFeatures, outputName, {pourPointField})

        Determines the contributing area above a set of cells in a raster.

     INPUTS:
      inputFlowDirectionRaster (Image Service / Raster Layer / String):
          The input raster that shows the direction of flow out of each cell.
      inPourPointRasterOrFeatures (Image Service / Feature Layer / Raster Layer / String):
          The input pour point locations.
      outputName (String):
          The name of the output watershed raster service.The default name is
          based on the tool name and the input layer name.
          If the layer name already exists, you will be prompted to provide
          another name.
      pourPointField {String}:
          Field used to assign values to the pour point locations.

        """