# Generated documentation for module arcpy.management


class ImportTileCache(object):
    """
    Imports tiles from an existing tile cache or a tile package. The target cache must have the same tiling scheme, spatial reference, and storage format as the source tile cache.
    """

    @property
    def description(self) -> str:
        return """

        ImportTileCache_management(in_cache_target, in_cache_source, {scales;scales...}, {area_of_interest}, {overwrite})

        Imports tiles from an existing tile cache or a tile package. The
        target cache must have the same tiling scheme, spatial reference, and
        storage format as the source tile cache.

     INPUTS:
      in_cache_target (Raster Layer):
          An existing tile cache to which the tiles will be imported.
      in_cache_source (Raster Layer / File):
          An existing tile cache or a tile package from which the tiles are
          imported.
      scales {Double}:
          A list of scale levels at which tiles will be imported.
      area_of_interest {Feature Set}:
          An area of interest will spatially constrain where tiles are imported
          into the cache.This parameter is useful if you want to import tiles
          for irregularly
          shaped areas.
      overwrite {Boolean}:
          Determines whether the images in the destination cache will be merged
          with the tiles from the originating cache or overwritten by
          them.MERGE-When the tiles are imported, transparent pixels in the
          originating cache are ignored by default. This results in a merged or
          blended image in the destination cache. This is the
          default.OVERWRITE-The import replaces all pixels in the area of
          interest,
          effectively overwriting tiles in the destination cache with tiles from
          the originating cache.

        """