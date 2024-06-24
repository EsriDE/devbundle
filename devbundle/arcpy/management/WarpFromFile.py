# Generated documentation for module arcpy.management


class WarpFromFile(object):
    """
    Transforms a raster dataset using an existing text file containing source and target control points.
    """

    @property
    def description(self) -> str:
        return """

        WarpFromFile_management(in_raster, out_raster, link_file, {transformation_type}, {resampling_type})

        Transforms a raster dataset using an existing text file containing
        source and target control points.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          The raster to be transformed.
      link_file (Text File):
          The text, CSV file, or TAB file containing the coordinates to
          warp the input raster. This can be generated from the Register Raster
          tool or from thetab. Georeferencing
      transformation_type {String}:
          Specifies the transformation method for shifting the raster
          dataset.POLYORDER0-A zero-order polynomial will be used to shift the
          data.
          This is commonly used when the data is georeferenced, but a small
          shift will better line it up. Only one link is required to perform a
          zero-order polynomial shift.POLYSIMILARITY-A first order
          transformation will be used that
          attempts to preserve the shape of the original raster. The RMS error
          tends to be higher than other polynomial transformations because the
          preservation of shape is more important than the best fit.POLYORDER1-A
          first-order polynomial (affine) will be used to fit a
          flat plane to the input points.POLYORDER2-A second-order polynomial
          will be used to fit a somewhat
          more complicated surface to the input points.POLYORDER3-A third-order
          polynomial will be used to fit a more
          complicated surface to the input points.ADJUST-A polynomial
          transformation is combined with a triangulated
          irregular network (TIN) interpolation technique that will optimize
          both global and local accuracy.SPLINE-The source control points will
          be transformed precisely to the
          target control points. In the output, the control points will be
          accurate, but the raster pixels between the control points will
          not.PROJECTIVE-Lines will be warped so that they remain straight.
          Lines
          that were once parallel may no longer remain parallel. The projective
          transformation is especially useful for oblique imagery, scanned maps,
          and for some imagery products.
      resampling_type {String}:
          The resampling algorithm to be used.NEAREST-The nearest neighbor
          technique will be used. It minimizes
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

     OUTPUTS:
      out_raster (Raster Dataset):
          The name, location, and format for the dataset you are creating. When
          storing a raster dataset in a geodatabase, do not add a file extension
          to the name of the raster dataset. When storing your raster dataset to
          a JPEG file, a JPEG 2000 file, a TIFF file, or a geodatabase, you can
          specify a compression type and compression quality using environment
          settings..bil-Esri BIL.bip-Esri BIP.bmp-BMP.bsq-Esri BSQ.dat-ENVI
          DAT.gif-GIF.img-ERDAS IMAGINE.jpg-JPEG.jp2-JPEG
          2000.png-PNG.tif-TIFF.mrf-MRF.crf-CRFNo extension for Esri Grid

        """