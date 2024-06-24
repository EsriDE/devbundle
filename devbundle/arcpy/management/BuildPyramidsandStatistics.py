# Generated documentation for module arcpy.management


class BuildPyramidsandStatistics(object):
    """
    Traverses a folder structure, building pyramids and calculating statistics for all the raster datasets it contains. It can also build pyramids and calculate statistics for all the items in a mosaic dataset.
    """

    @property
    def description(self) -> str:
        return """

        BuildPyramidsandStatistics_management(in_workspace, {include_subdirectories}, {build_pyramids}, {calculate_statistics}, {BUILD_ON_SOURCE}, {block_field}, {estimate_statistics}, {x_skip_factor}, {y_skip_factor}, {ignore_values;ignore_values...}, {pyramid_level}, {SKIP_FIRST}, {resample_technique}, {compression_type}, {compression_quality}, {skip_existing}, {where_clause}, {sips_mode})

        Traverses a folder structure, building pyramids and calculating
        statistics for all the raster datasets it contains. It can also build
        pyramids and calculate statistics for all the items in a mosaic
        dataset.

     INPUTS:
      in_workspace (Text File / Workspace / Raster Layer / Mosaic Layer):
          The workspace that contains all the raster datasets or mosaic datasets
          to be processed.If the workspace includes a mosaic dataset, only the
          statistics
          associated with the mosaic dataset will be included. The statistics
          associated with the items within the mosaic dataset will not be
          included.
      include_subdirectories {Boolean}:
          Specifies whether subdirectories will be included.NONE-Does not
          include subdirectories.INCLUDE_SUBDIRECTORIES-Includes
          all the raster datasets within the
          subdirectories when loading. This is the default.If the workspace
          includes a mosaic dataset, only the statistics
          associated with mosaic dataset will be included. The statistics
          associated with the items within the mosaic dataset will not be
          included.
      build_pyramids {Boolean}:
          Specifies whether pyramids will be built.NONE-Pyramids will not be
          built.BUILD_PYRAMIDS-Pyramids will be built.
          This is the default.
      calculate_statistics {Boolean}:
          Specify whether to calculate statistics.NONE-Does not calculate
          statistics.CALCULATE_STATISTICS-Calculates
          statistics. This is the default.
      BUILD_ON_SOURCE {Boolean}:
          Specify whether to calculate statistics on the source raster datasets,
          or calculate statistics on the raster items in a mosaic dataset. This
          option only applies to mosaic datasets.NONE-Statistics will be
          calculated for each raster item in the mosaic
          dataset (on each row in the attribute table). Any functions added to
          the raster item will be applied before generating the statistics. This
          is the default.BUILD_ON_SOURCE-Calculates statistics on the source
          data of the mosaic
          dataset.
      block_field {String}:
          The name of the field within a mosaic dataset's attribute table used
          to identify items that should be considered one item when performing
          some calculations and operations.
      estimate_statistics {Boolean}:
          Specify whether to calculate statistics for the mosaic dataset (not
          the rasters within it). The statistics are derived from the existing
          statistics that have been calculated for each raster in the mosaic
          dataset.NONE-Statistics are not calculated for the mosaic dataset.
          This is the
          default.ESTIMATE_STATISTICS-Statistics will be calculated for the
          mosaic
          dataset.
      x_skip_factor {Long}:
          The number of horizontal pixels between samples.A skip factor controls
          the portion of the raster that is used when
          calculating the statistics. The input value indicates the horizontal
          or vertical skip factor, where a value of 1 will use each pixel and a
          value of 2 will use every second pixel. The skip factor can only range
          from 1 to the number of columns/rows in the raster.The value must be
          greater than zero and less than or equal to the
          number of columns in the raster. The default is 1 or the last skip
          factor used.
      y_skip_factor {Long}:
          The number of vertical pixels between samples.A skip factor controls
          the portion of the raster that is used when
          calculating the statistics. The input value indicates the horizontal
          or vertical skip factor, where a value of 1 will use each pixel and a
          value of 2 will use every second pixel. The skip factor can only range
          from 1 to the number of columns/rows in the raster.The value must be
          greater than zero and less than or equal to the
          number of rows in the raster. The default is 1 or the last y skip
          factor used.
      ignore_values {Long}:
          The pixel values that are not to be included in the statistics
          calculation.The default is no value.
      pyramid_level {Long}:
          The number of reduced-resolution dataset layers that will be built.
          The default value is -1, which will build full pyramids. A value of 0
          will result in no pyramid levels.The maximum number of pyramid levels
          you can specify is 29. Any value
          of 30 or higher will create a full set of pyramids.
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
          raster pyramids.DEFAULT-If the source data is compressed using a
          wavelet compression,
          pyramids will be built using the JPEG compression type; otherwise,
          LZ77 will be used. This is the default.LZ77-The LZ77 compression
          algorithm will be used to build pyramids.
          This compression type can be used for any data type. JPEG-The
          JPEG compression algorithm will be used to build
          pyramids. Only data that adheres to the JPEG compression specification
          can use this compression type. If this compression type is specified,
          you can then set theparameter value. Compression
          qualityJPEG_YCBCR-A lossy compression using the luma (Y) and chroma
          (Cb and
          Cr) color space components will be used.NONE-No compression will be
          used when building pyramids.
      compression_quality {Long}:
          The compression quality that will be used when pyramids are
          built with thecompression type. The value must be between 0 and 100.
          The values closer to 100 will produce a higher-quality image, but the
          compression ratio will be lower. JPEG
      skip_existing {Boolean}:
          Specify whether to calculate statistics only where they are missing,
          or regenerate them even if they exist.SKIP_EXISTING-Statistics will
          only be calculated if they do not
          already exist. This is the default.OVERWRITE-Statistics will be
          calculated even if they already exist;
          existing statistics will be overwritten.
      where_clause {SQL Expression}:
          An SQL expression to select raster datasets that will be processed.
      sips_mode {Boolean}:
          Specifies whether to enable building of pyramid files using key
          processes and algorithms defined in the Softcopy Image Processing
          Standard (SIPS), NGA.STND.0014.NONE-Pyramids will be built using
          standard subsampling methods. This
          is the default.SIPS_MODE-Pyramids will be built using SIPS processing.

        """