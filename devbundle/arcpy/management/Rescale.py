# Generated documentation for module arcpy.management


class Rescale(object):
    """
    Resizes a raster by the specified x and y scale factors.
    """

    @property
    def description(self) -> str:
        return """

        Rescale_management(in_raster, out_raster, x_scale, y_scale)

        Resizes a raster by the specified x and y scale factors.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          The input raster.
      x_scale (Double):
          The factor by which to scale the cell size in the x direction.The
          factor must be greater than zero.
      y_scale (Double):
          The factor by which to scale the cell size in the y direction.The
          factor must be greater than zero.

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