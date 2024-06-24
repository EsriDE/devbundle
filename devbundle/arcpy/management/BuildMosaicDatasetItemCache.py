# Generated documentation for module arcpy.management


class BuildMosaicDatasetItemCache(object):
    """
    Inserts the Cached Raster function as the final step in all function chains within a mosaic dataset.
    """

    @property
    def description(self) -> str:
        return """

        BuildMosaicDatasetItemCache_management(in_mosaic_dataset, {where_clause}, {define_cache}, {generate_cache}, {item_cache_folder}, {compression_method}, {compression_quality}, {max_allowed_rows}, {max_allowed_columns}, {request_size_type}, {request_size})

        Inserts the Cached Raster function as the final step in all function
        chains within a mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset where you want to apply the cache function.
      where_clause {SQL Expression}:
          An SQL expression to select specific raster datasets within the mosaic
          dataset on which you want the item cache built.
      define_cache {Boolean}:
          Choose to define the mosaic dataset cache. A Cached Raster function
          will be inserted to the selected items. If an item already has a
          Cached Raster function, it will not add another one.DEFINE_CACHE-The
          Cached Raster function will be added to the selected
          items. If an item already has this function, it will not add another
          one. This is the default.NO_DEFINE_CACHE-No raster cache will be
          defined.
      generate_cache {Boolean}:
          Choose to generate the cache files based on the properties defined in
          the Cached Raster function, such as the location and the compression
          of the cache.GENERATE_CACHE-Cache will be generated. This is the
          default.NO_GENERATE_CACHE-Cache will not be generated.
      item_cache_folder {Workspace}:
          Choose to overwrite the default location to save your cache. If the
          mosaic dataset is inside of a file geodatabase, by default, the cache
          is saved in a folder with the same name as the geodatabase and a
          .cache extension. If the mosaic dataset is inside of an enterprise
          geodatabase, by default, the cache will be saved inside of that
          geodatabase. Once created, the cache will always save to the same
          location. To save the cache to a different location, you need to first
          use the Repair Mosaic Dataset tool to specify a new location and run
          this tool again.Once an item cache is created, regenerating an item
          cache to a
          different location is not possible by specifying a different cache
          path and rerunning this tool. It will still generate the item cache in
          the location where it was generated the first time. However, you can
          remove this function and insert a new one with the new path or use the
          Repair Mosaic Dataset tool to modify the cache path and run this tool
          to generate the item cache in a different location.
      compression_method {String}:
          Choose how you want to compress your data for faster
          transmission.LOSSLESS-Retain the values of each pixel when generating
          cache.
          Lossless has a compression ratio of approximately 2:1.LOSSY-
          Appropriate when your imagery is only used as a backdrop. Lossy
          has the highest compression ratio (20:1) but groups similar pixel
          values to achieve higher compression.NONE-Do not compress imagery.
          This will make your imagery slower to
          transmit but faster to draw because it will not need to be
          decompressed when viewed.
      compression_quality {Long}:
          Set a compression quality when using the lossy method. The compression
          quality value is between 1 and 100 percent, with 100 compressing the
          least.
      max_allowed_rows {Long}:
          Limit the size of the cache dataset by number of rows. If value is
          more than the number of rows in the dataset, the cache will not
          generate.
      max_allowed_columns {Long}:
          Limit the size of the cache dataset by number of columns. If value is
          more than the number of columns in the dataset, the cache will not
          generate.
      request_size_type {String}:
          Resample the cache using one of these two methods:PIXEL_SIZE_FACTOR-
          Set a scaling factor relative to the pixel size. To
          not resample the cache, choose PIXEL_SIZE_FACTOR and set the
          request_size parameter to 1.PIXEL_SIZE-Specify a pixel size for the
          cached raster.
      request_size {Double}:
          Set a value to apply to the request_size_type.

        """