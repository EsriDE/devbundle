# Generated documentation for module arcpy.conversion


class RasterToFloat(object):
    """
    Converts a raster dataset to a file of binary floating-point values representing raster data.
    """

    @property
    def description(self) -> str:
        return """

        RasterToFloat_conversion(in_raster, out_float_file)

        Converts a raster dataset to a file of binary floating-point values
        representing raster data.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster dataset.The raster can be integer or floating-point
          type.

     OUTPUTS:
      out_float_file (File):
          The output floating-point raster file.The file name must have a .flt
          extension.

        """