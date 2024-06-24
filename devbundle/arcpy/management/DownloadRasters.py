# Generated documentation for module arcpy.management


class DownloadRasters(object):
    """
    Downloads the source files from an image service or mosaic dataset.
    """

    @property
    def description(self) -> str:
        return """

        DownloadRasters_management(in_image_service, out_folder, {where_clause}, {selection_feature}, {clipping}, {convert_rasters}, {format}, {compression_method}, {compression_quality}, {MAINTAIN_FOLDER})

        Downloads the source files from an image service or mosaic dataset.

     INPUTS:
      in_image_service (Image Service / String / Mosaic Layer / Raster Layer):
          The image service or mosaic dataset to download.
      out_folder (Folder):
          The destination for the image service or mosaic dataset.
      where_clause {SQL Expression}:
          An SQL expression to limit the download to raster datasets that
          satisfy the expression.
      selection_feature {Extent}:
          Limits the download to an extent of a feature class or bounding box.
          All raster datasets that intersect the extent will be
          downloaded.MAXOF-The maximum extent of all inputs will be
          used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      clipping {Boolean}:
          Specify if you want to clip the downloaded images based on the
          geometry of a feature. Any raster that intersects the clipping
          geometry will be clipped and then downloaded. This is useful when your
          area of interest is not a rectangle. When downloaded images are
          clipped, you need to specify an output format for the clipped
          images.NO_CLIPPING-The files will be clipped based on the minimum
          bounding
          rectangle that has been specified. This is the default.CLIPPING-The
          files will be clipped based on the geometry of the
          selection_feature.
      convert_rasters {Boolean}:
          Choose whether to always convert your rasters to the specified format,
          or to only convert when it is necessary.CONVERT_AS_REQUIRED-Do not
          convert the raster datasets to a new
          format.ALWAYS_CONVERT-Convert the downloaded raster datasets into
          another
          format. If you used selection_feature to limit the extent, then you
          need to specify a format in the format parameter.
      format {String}:
          Choose a output format for the downloaded raster datasets.TIFF-Tagged
          Image File Format. This is the default.BIL-Esri band
          interleaved by line.BSQ-Esri band sequential.BIP-Esri band interleaved
          by pixel.BMP-Bitmap.ENVI-ENVI DAT file.IMAGINE Image-ERDAS
          IMAGINE.JPEG-Joint Photographics Experts Group. If chosen, you can
          also
          specify the compression quality. The valid compression quality value
          ranges are from 0 to 100.GIF-Graphic interchange format.JP2-JPEG 2000.
          If chosen, you can also specify the compression
          quality. The valid compression quality value ranges are from 0 to
          100.PNG-Portable Network Graphics.
      compression_method {String}:
          Choose the compression method to use with the specified.
          Output FormatNONE-No compression will occur. This is the
          default.JPEG-Lossy
          compression that uses the public JPEG compression
          algorithm. If you choose JPEG, you can also specify the compression
          quality. The valid compression quality value ranges are from 0 to 100.
          This compression can be used for JPEG files and TIFF
          files.LZW-Lossless compression that preserves all raster cell
          values.PACKBITS-PackBits compression for TIFF files.RLE-Run-length
          encoding for IMG files.CCITT_GROUP3-Lossless compression for 1-bit
          data.CCITT_GROUP4-Lossless compression for 1-bit
          data.CCITT_1D-Lossless compression for 1-bit data.
      compression_quality {Long}:
          Set a value from 1 - 100. Higher values will have better image
          quality, but less compression.
      MAINTAIN_FOLDER {Boolean}:
          Determines the folder structure of the downloaded
          rasters.MAINTAIN_FOLDER-Replicate the hierarchical folder structure
          used to
          store the source raster datasets.NO_MAINTAIN_FOLDER-Raster datasets
          will be downloaded into the
          out_folder as a flat folder structure.

        """