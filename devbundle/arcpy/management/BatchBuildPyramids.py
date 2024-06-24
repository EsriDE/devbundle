# Generated documentation for module arcpy.management


class BatchBuildPyramids(object):
    """
    Builds pyramids for multiple raster datasets.
    """

    @property
    def description(self) -> str:
        return """

        BatchBuildPyramids_management(Input_Raster_Datasets;Input_Raster_Datasets..., {Pyramid_levels}, {Skip_first_level}, {Pyramid_resampling_technique}, {Pyramid_compression_type}, {Compression_quality}, {Skip_Existing})

        Builds pyramids for multiple raster datasets.

     INPUTS:
      Input_Raster_Datasets (Raster Dataset):
          The raster datasets for which raster pyramids will be built.Each input
          should have more than 1,024 rows and 1,024 columns.
      Pyramid_levels {Long}:
          The number of reduced-resolution dataset layers that will be built.
          The default value is -1, which will build full pyramids. A value of 0
          will result in no pyramid levels.
      Skip_first_level {Boolean}:
          Specifies whether the first pyramid level will be skipped. Skipping
          the first level will take up slightly less disk space but will slow
          down performance at these scales.NONE-The first pyramid level will not
          be skipped; it will be built.
          This is the default.SKIP_FIRST-The first pyramid level will be
          skipped; it will not be
          built.
      Pyramid_resampling_technique {String}:
          Specifies the resampling technique that will be used to build the
          pyramids.NEAREST-The new value of a cell will be based on the closest
          cell when
          resampling. This is the default.BILINEAR-The new value of a cell will
          be based on a weighted distance
          average of the four nearest input cell centers.CUBIC-The new value of
          a cell will be determined by fitting a smooth
          curve through the 16 nearest input cell centers.
      Pyramid_compression_type {String}:
          Specifies the compression type that will be used when building the
          pyramids.DEFAULT-If the source data is compressed using a wavelet
          compression,
          pyramids will be built with the JPEG compression type; otherwise, LZ77
          will be used. This is the default.LZ77-The LZ77 compression algorithm
          will be used to build the
          pyramids. LZ77 can be used for any data type.JPEG-The JPEG compression
          algorithm will be used to build the
          pyramids. Only data that adheres to the JPEG compression specification
          can use this compression type. If JPEG is chosen, you can then set the
          compression quality.NONE-No compression will be used when building
          pyramids.
      Compression_quality {Long}:
          The compression quality that will be used when pyramids are
          built with thecompression type. The value must be between 0 and 100.
          The values closer to 100 will produce a higher-quality image, but the
          compression ratio will be lower. JPEG
      Skip_Existing {Boolean}:
          Specifies whether pyramids will be built only if they do not exist or
          built even if they exist.OVERWRITE-Pyramids will be built even if they
          already exist; existing
          pyramids will be overwritten. This is the
          default.SKIP_EXISTING-Pyramids will only be built if they do not
          exist;
          existing pyramids will be skipped.

        """