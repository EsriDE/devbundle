# Generated documentation for module arcpy.ra


class ConvertFeatureToRaster(object):
    """
    Converts features to a raster dataset.
    """

    @property
    def description(self) -> str:
        return """

        ConvertFeatureToRaster_ra(inputFeatures, valueField, outputName, {outputCellSize})

        Converts features to a raster dataset.

     INPUTS:
      inputFeatures (Feature Set):
          The input feature layer.
      valueField (Field):
          Choose the field that will be used to assign values to the output
          raster.
      outputName (String):
          The name of the output raster service.The default name is based on the
          tool name and the input layer name.
          If the layer name already exists, you will be prompted to provide
          another name.
      outputCellSize {Linear Unit}:
          Enter the cell size and unit for the output raster.The unit values are
          Kilometers, Meters, MilesInt, FeetInt, Miles, and
          Feet.The default units are meters.

        """