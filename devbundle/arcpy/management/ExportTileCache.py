# Generated documentation for module arcpy.management


class ExportTileCache(object):
    """
    Exports tiles from an existing tile cache to a new tile cache or a tile package. The tiles can be either independently imported into other caches or accessed from ArcGIS Pro or mobile devices.
    """

    @property
    def description(self) -> str:
        return """

        ExportTileCache_management(in_cache_source, in_target_cache_folder, in_target_cache_name, {export_cache_type}, {storage_format_type}, {scales;scales...}, {area_of_interest})

        Exports tiles from an existing tile cache to a new tile cache or a
        tile package. The tiles can be either independently imported into
        other caches or accessed from ArcGIS Pro or mobile devices.

     INPUTS:
      in_cache_source (Raster Layer / Raster Dataset):
          An existing tile cache to be exported.
      in_target_cache_folder (Folder):
          The output folder into which the tile cache or tile package will be
          exported.
      in_target_cache_name (String):
          The name of the exported tile cache or tile package.
      export_cache_type {String}:
          Specifies whether the cache will be exported as a tile cache or a tile
          package. Tile packages are suitable for ArcGIS Runtime and ArcGIS
          Mobile deployments.TILE_CACHE-The cache will be exported as a stand-
          alone cache raster
          dataset. This is the default.TILE_PACKAGE-The cache will be exported
          as a single compressed file
          (.tpk) in which the cache dataset is added as a layer and consolidated
          so that it can be shared easily. This type can be used in ArcMap as
          well as in ArcGIS Runtime and ArcGIS Mobile applications.
          TILE_PACKAGE_TPKX-The cache will be exported using Compact_v2
          storage format (.tpkx), which provides better performance on network
          shares and cloud storage directories. This improved and
          simplified package structure type is supported by
          newer versions of the ArcGIS platform such as ArcGIS Online, ArcGIS
          Pro 2.3, ArcGIS Enterprise 10.7, and ArcGIS Runtime 100.5.
      storage_format_type {String}:
          Determines the storage format of tiles.COMPACT-Group tiles into large
          files called bundles. This storage
          format is more efficient in terms of storage and mobility.
          COMPACT_V2-Tiles are grouped in bundle files only. This
          format provides better performance on network shares and cloudstore
          directories. If theparameter is set tothen the extension of the tile
          package is (.tpkx), which is supported by newer versions of the ArcGIS
          Platform such as ArcGIS Online, ArcGIS Enterprise 11.3 and ArcGIS
          Runtime 100.5. Export cache typeTile package (tpkx)This is the
          default. EXPLODED-Each tile is stored as an individual file.
          Note that this format cannot be used with tile packages.
      scales {Double}:
          A list of scale levels at which tiles will be exported.
      area_of_interest {Feature Set}:
          An area of interest that spatially constrains where tiles will be
          exported from the cache.The area of interest can be a feature class or
          a feature that you draw
          on the map.This parameter is useful if you want to export irregularly
          shaped
          areas, as the tool clips the cache dataset at pixel resolution.

        """