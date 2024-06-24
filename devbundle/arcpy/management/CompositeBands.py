# Generated documentation for module arcpy.management


class CompositeBands(object):
    """
    Creates a single raster dataset from multiple bands.
    """

    @property
    def description(self) -> str:
        return """

        CompositeBands_management(in_rasters;in_rasters..., out_raster)

        Creates a single raster dataset from multiple bands.

     INPUTS:
      in_rasters (Mosaic Dataset / Mosaic Layer / Raster Dataset / Raster Layer):
          The raster datasets that you want to use as the bands.

     OUTPUTS:
      out_raster (Raster Dataset):
          The name, location and format for the raster dataset you are creating.
          Make sure that it can support the necessary bit-depth.When storing the
          raster dataset in a file format, specify the file
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