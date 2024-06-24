# Generated documentation for module arcpy.management


class Resample(object):
    """
    Changes the spatial resolution of a raster dataset and sets rules for aggregating or interpolating values across the new pixel sizes.
    """

    @property
    def description(self) -> str:
        return """

        Resample_management(in_raster, out_raster, {cell_size}, {resampling_type})

        Changes the spatial resolution of a raster dataset and sets rules for
        aggregating or interpolating values across the new pixel sizes.

     INPUTS:
      in_raster (Mosaic Dataset / Mosaic Layer / Raster Dataset / Raster Layer):
          The raster dataset with the spatial resolution to be changed.
      cell_size {Cell Size XY}:
          The cell size of the new raster using an existing raster dataset or by
          specifying its width (x) and height (y). You can specify the
          cell size in the following ways:
          Use a single number specifying a square cell size.Use two numbers that
          specify the x and y cell size, which is space
          delimited.Use the path of a raster dataset from which the square cell
          size will
          be imported.
      resampling_type {String}:
          Specifies the resampling technique to be used.NEAREST-The nearest
          neighbor technique will be used. It minimizes
          changes to pixel values since no new values are created and is the
          fastest resampling technique. It is suitable for discrete data, such
          as land cover.BILINEAR-The bilinear interpolation technique will be
          used. It
          calculates the value of each pixel by averaging (weighted for
          distance) the values of the surrounding four pixels. It is suitable
          for continuous data.CUBIC-The cubic convolution technique will be
          used. It calculates the
          value of each pixel by fitting a smooth curve based on the surrounding
          16 pixels. This produces the smoothest image but can create values
          outside of the range found in the source data. It is suitable for
          continuous data.MAJORITY-The majority resampling technique will be
          used. It determines
          the value of each pixel based on the most popular value in a 4 by 4
          window. It is suitable for discrete data.

     OUTPUTS:
      out_raster (Raster Dataset):
          The name, location, and format of the dataset being created..bil-Esri
          BIL.bip-Esri BIP.bmp-BMP.bsq-Esri BSQ.dat-ENVI
          DAT.gif-GIF.img-ERDAS IMAGINE.jpg-JPEG.jp2-JPEG
          2000.png-PNG.tif-TIFF.mrf-MRF.crf-CRFNo extension for Esri GridWhen
          storing a raster dataset in a geodatabase, do not add a file
          extension to the name of the raster dataset. When storing a raster
          dataset to JPEG, JPEG 2000, or TIFF format, or in a geodatabase, you
          can specify a compression type and compression quality.

        """