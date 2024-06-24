# Generated documentation for module arcpy.management


class Mirror(object):
    """
    Reorients the raster by turning it over, from left to right, along the vertical axis through the center of the raster.
    """

    @property
    def description(self) -> str:
        return """

        Mirror_management(in_raster, out_raster)

        Reorients the raster by turning it over, from left to right, along the
        vertical axis through the center of the raster.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          The input raster dataset.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster dataset.When storing the raster dataset in a file
          format, specify the file
          extension as follows:.bil-Esri BIL.bip-Esri BIP.bmp-BMP.bsq-Esri
          BSQ.dat-ENVI
          DAT.gif-GIF.img-ERDAS IMAGINE.jpg-JPEG.jp2-JPEG
          2000.png-PNG.tif-TIFF.mrf-MRF.crf-CRFNo extension for Esri GridWhen
          storing a raster dataset in a geodatabase, do not add a file
          extension to the name of the raster dataset. When storing a
          raster dataset to a JPEG format file, a JPEG
          2000 format file, a TIFF format file, or a geodatabase, you can
          specifyandvalues in the geoprocessing environments. Compression
          TypeCompression Quality

        """