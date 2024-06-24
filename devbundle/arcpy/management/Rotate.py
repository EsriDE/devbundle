# Generated documentation for module arcpy.management


class Rotate(object):
    """
    Turns a raster dataset around a specified pivot point.
    """

    @property
    def description(self) -> str:
        return """

        Rotate_management(in_raster, out_raster, angle, {pivot_point}, {resampling_type}, {clipping_extent})

        Turns a raster dataset around a specified pivot point.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          The raster dataset to rotate.
      angle (Double):
          Specify a value between 0 and 360 degrees the raster will be rotated
          in the clockwise direction. To rotate the raster in the
          counterclockwise direction, specify the angle as a negative value. The
          angle can be specified as an integer or a floating-point value.
      pivot_point {Point}:
          The point the raster will rotate around. If left blank, the lower left
          corner of the input raster dataset will serve as the pivot.
      resampling_type {String}:
          Specifies the resampling technique that will be used. The
          default is. NearestNEAREST-The nearest neighbor technique will
          be used. It minimizes
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
          window. It is suitable for discrete data. Theandoptions are
          used for categorical data, such as a land-
          use classification. Theoption is the default. It is the quickest and
          does not change the pixel values. Do not use either of these options
          for continuous data, such as elevation surfaces.
          NearestMajorityNearest        Theandoptions are most appropriate for
          continuous data. It is
          recommended that you do not use either of these options with
          categorical data because the pixel values may be altered.
          BilinearCubic
      clipping_extent {Extent}:
          The processing extent of the raster dataset. The source data will be
          clipped to the specified extent before rotation.MAXOF-The maximum
          extent of all inputs will be used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.

     OUTPUTS:
      out_raster (Raster Dataset):
          The name, location, and format for the dataset you are creating. When
          storing a raster dataset in a geodatabase, do not add a file extension
          to the name of the raster dataset. When storing your raster dataset to
          a JPEG file, a JPEG 2000 file, a TIFF file, or a geodatabase, you can
          specify a compression type and compression quality.When storing the
          raster dataset in a file format, specify the file
          extension as follows:.bil-Esri BIL.bip-Esri BIP.bmp-BMP.bsq-Esri
          BSQ.dat-ENVI
          DAT.gif-GIF.img-ERDAS IMAGINE.jpg-JPEG.jp2-JPEG
          2000.png-PNG.tif-TIFF.mrf-MRF.crf-CRFNo extension for Esri Grid

        """