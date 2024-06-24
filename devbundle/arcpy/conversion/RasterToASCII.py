# Generated documentation for module arcpy.conversion


class RasterToASCII(object):
    """
    Converts a raster dataset to an ASCII file representing raster data.
    """

    @property
    def description(self) -> str:
        return """

        RasterToASCII_conversion(in_raster, out_ascii_file)

        Converts a raster dataset to an ASCII file representing raster data.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster dataset.The raster can be integer or floating-point
          type.

     OUTPUTS:
      out_ascii_file (File):
          The output ASCII raster file.

        """