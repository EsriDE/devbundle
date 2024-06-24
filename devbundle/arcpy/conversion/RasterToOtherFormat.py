# Generated documentation for module arcpy.conversion


class RasterToOtherFormat(object):
    """
    Converts one or more raster datasets to a different format.
    """

    @property
    def description(self) -> str:
        return """

        RasterToOtherFormat_conversion(Input_Rasters;Input_Rasters..., Output_Workspace, {Raster_Format})

        Converts one or more raster datasets to a different format.

     INPUTS:
      Input_Rasters (Raster Dataset / Raster Layer):
          The raster datasets to convert.
      Output_Workspace (Workspace):
          The folder where the raster dataset will be written.
      Raster_Format {String}:
          Specifies the format that will be used for the output raster
          dataset.BIL-The output will be Esri BIL format.BIP-The output will be
          Esri BIP
          format.BMP-The output will be Microsoft BMP format.BSQ-The output will
          be Esri BSQ format.CRF-The output will be CRF format.ENVI DAT-The
          output will be ENVI DAT format.GIF-The output will be GIF
          format.GRID-The output will be Esri Grid format.IMAGINE Image-The
          output will be ERDAS IMAGINE format.JP2000-The output will be JPEG
          2000 format.JPEG-The output will be JPEG format.MRF-The output will be
          MRF format.PNG-The output will be PNG format.TIFF-The output will be
          TIFF format.

        """