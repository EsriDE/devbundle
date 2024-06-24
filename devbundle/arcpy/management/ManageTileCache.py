# Generated documentation for module arcpy.management


class ManageTileCache(object):
    """
    Creates a tile cache or updates tiles in an existing tile cache. You can use this tool to create tiles, replace missing tiles, overwrite outdated tiles, and delete tiles.
    """

    @property
    def description(self) -> str:
        return """

        ManageTileCache_management(in_cache_location, manage_mode, {in_cache_name}, {in_datasource}, {tiling_scheme}, {import_tiling_scheme}, {scales;scales...}, {area_of_interest}, {max_cell_size}, {min_cached_scale}, {max_cached_scale})

        Creates a tile cache or updates tiles in an existing tile cache. You
        can use this tool to create tiles, replace missing tiles, overwrite
        outdated tiles, and delete tiles.

     INPUTS:
      in_cache_location (Raster Layer / Folder):
          The folder in which the cache dataset is created, the raster layer, or
          the path to an existing tile cache.
      manage_mode (String):
          Specifies the mode that will be used to manage the
          cache.RECREATE_ALL_TILES-Existing tiles will be replaced and new tiles
          will
          be added if the extent has changed or if layers have been added to a
          multilayer cache.RECREATE_EMPTY_TILES-Only tiles that are empty will
          be created.
          Existing tiles will be left unchanged.DELETE_TILES-Tiles will be
          deleted from the cache. The cache folder
          structure will not be deleted.
      in_cache_name {String}:
          The name of the cache dataset to be created in the cache location.
      in_datasource {Mosaic Layer / Raster Layer / Map}:
          A raster dataset, mosaic dataset, or map file.This parameter is not
          required when the manage_mode parameter is set
          to DELETE_TILES.A map file (.mapx) cannot contain a map service or
          image service.
      tiling_scheme {String}:
          Specifies the tiling scheme that will be used.ARCGISONLINE_SCHEME-The
          default ArcGIS Online tiling scheme will be
          used.IMPORT_SCHEME-An existing tiling scheme will be imported and
          used.ARCGISONLINE_ELEVATION_SCHEME-The elevation services tiling
          scheme
          will be used.WGS84_V2_SCHEME-The WGS84 version 2 tiling scheme will be
          used.WGS84_V2_ELEVATION_SCHEME-The WGS84 version 2 tiling scheme will
          be
          used to build a tile cache for elevation data.
      import_tiling_scheme {Image Service / Map Server / File}:
          The path to an existing scheme file (.xml) or to a tiling scheme
          imported from an existing image service or map service.
      scales {Double}:
          The scale levels at which tiles will be created or deleted , depending
          on the value of the manage_mode parameter. The pixel size is based on
          the spatial reference of the tiling scheme.By default, only the values
          for min_cached_scale and max_cached_scale
          will be used when generating cache.Altering the value of either the
          min_cached_scale or the
          max_cached_scale parameter will change which scales will be used when
          generating cache.Scales that exist but are not within the range of the
          min_cached_scale
          or max_cached_scale parameter values will be ignored when generating
          the cache.
      area_of_interest {Feature Set}:
          Defines an area of interest to constrain where tiles will be created
          or deleted.It can be a feature class, or it can be a feature set that
          you
          interactively define.This parameter is useful if you want to manage
          tiles for irregularly
          shaped areas. It's also useful when you want to precache some areas
          and leave less-visited areas uncached.
      max_cell_size {Double}:
          The value that defines the visibility of the data source for which the
          cache will be generated. By default, the value is empty.If the value
          is empty, the following apply:For levels of cache that lie within the
          visibility ranges of the data
          source, the cache will be generated from the data source.For levels of
          cache that fall outside the visibility of the data
          source, the cache will be generated from the previous level of
          cache.If the value is greater than zero, the following apply:
          For levels with cell sizes smaller than or equal to
          the(max_cell_size) value, the cache will be generated from the data
          source. Maximum Source Cell Size         For levels with cell
          sizes greater than the(max_cell_size)
          value, the cache will be generated from the previous level of cache.
          Maximum Source Cell Size        The unit of thevalue should be the
          same as the unit of the
          cell size of the source dataset. Maximum Source Cell Size
      min_cached_scale {Double}:
          The minimum scale at which tiles will be created. This value does not
          have to be the smallest scale in the tiling scheme. The minimum cache
          scale will determine which scales are used when generating cache.
      max_cached_scale {Double}:
          The maximum scale at which tiles will be created. This does not have
          to be the largest scale in the tiling scheme. The maximum cache scale
          will determine which scales are used when generating cache.

        """