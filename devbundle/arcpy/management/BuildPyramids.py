# Generated documentation for module arcpy.management


class BuildPyramids(object):
    """
    Builds raster pyramids for your raster dataset.
    """

    @property
    def description(self) -> str:
        return """

        BuildPyramids_management(in_raster_dataset, {pyramid_level}, {SKIP_FIRST}, {resample_technique}, {compression_type}, {compression_quality}, {skip_existing})

        Builds raster pyramids for your raster dataset.

     INPUTS:
      in_raster_dataset (Raster Dataset / Raster Layer):
          The raster dataset for which you want to build pyramids.The input
          should have more than 1,024 rows and 1,024 columns.
      pyramid_level {Long}:
          The number of reduced-resolution dataset layers that will be built.
          The default value is -1, which will build full pyramids. A value of 0
          will result in no pyramid levels. To delete pyramids, set the
          number of levels to. 0The maximum number of pyramid levels you
          can specify is 29. Any value
          that is 30 or higher will revert to a value of -1, which will create a
          full set of pyramids.
      SKIP_FIRST {Boolean}:
          Specifies whether the first pyramid level will be skipped. Skipping
          the first level will take up slightly less disk space but will slow
          down performance at these scales.NONE-The first pyramid level will not
          be skipped; it will be built.
          This is the default.SKIP_FIRST-The first pyramid level will be
          skipped; it will not be
          built.
      resample_technique {String}:
          Specifies the resampling technique that will be used to build the
          pyramids.NEAREST-The value of the closest pixel will be used to assign
          a value
          to the output pixel when resampling. This is the default.BILINEAR-The
          new value of a pixel will be based on a weighted distance
          average of the four nearest input pixel centers.CUBIC-The new value of
          a pixel will be based on fitting a smooth curve
          through the 16 nearest input pixel centers.
      compression_type {String}:
          Specifies the compression type that will be used when building the
          raster pyramids. DEFAULT-If the source data is compressed
          using a wavelet
          compression, it will build pyramids with thecompression type;
          otherwise,will be used. This is the default compression method.
          JPEGLZ77         LZ77-Thecompression algorithm will be used to build
          the
          pyramids.can be used for any data type. LZ77LZ77
          JPEG-Thecompression algorithm will be used to build pyramids.
          Only data that adheres to the JPEG compression specification can use
          this compression type. Ifis chosen, you can then set the compression
          quality. JPEGJPEGJPEG_YCbCr-A lossy compression using the luma
          (Y) and chroma (Cb and
          Cr) color space components will be used to build pyramids.NONE-No
          compression will be used when building pyramids.
      compression_quality {Long}:
          The compression quality that will be used when pyramids are
          built with thecompression type. The value must be between 0 and 100.
          The values closer to 100 will produce a higher-quality image, but the
          compression ratio will be lower. JPEG
      skip_existing {Boolean}:
          Specifies whether pyramids will be built only when they are missing or
          will be regenerated even if they exist.OVERWRITE-Pyramids will be
          built even if they already exist, and
          existing pyramids will be overwritten. This is the
          default.SKIP_EXISTING-Pyramids will only be built if they do not
          already
          exist.

        """