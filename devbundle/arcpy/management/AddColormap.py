# Generated documentation for module arcpy.management


class AddColormap(object):
    """
    Adds a new color map or replaces an existing color map on a raster dataset.
    """

    @property
    def description(self) -> str:
        return """

        AddColormap_management(in_raster, {in_template_raster}, {input_CLR_file})

        Adds a new color map or replaces an existing color map on a raster
        dataset.

     INPUTS:
      in_raster (Raster Layer):
          The raster dataset to add or replace a color map.
      in_template_raster {Raster Layer}:
          A raster dataset that has a color map that you want to apply to the
          input raster dataset. If this is entered the input_CLR_file parameter
          is ignored.
      input_CLR_file {File}:
          Specify a .clr or .act file to use as the color map.

        """