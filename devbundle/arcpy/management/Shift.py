# Generated documentation for module arcpy.management


class Shift(object):
    """
    Moves (slides) the raster to a new geographic location based on x and y shift values. This tool is helpful if your raster dataset needs to be shifted to align with another data file.
    """

    @property
    def description(self) -> str:
        return """

        Shift_management(in_raster, out_raster, x_value, y_value, {in_snap_raster})

        Moves (slides) the raster to a new geographic location based on x and
        y shift values. This tool is helpful if your raster dataset needs to
        be shifted to align with another data file.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          The input raster dataset.
      x_value (Double):
          The value used to shift the x-coordinates.
      y_value (Double):
          The value used to shift the y-coordinates.
      in_snap_raster {Raster Layer}:
          The raster dataset used to align the cells of the output raster
          dataset.

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