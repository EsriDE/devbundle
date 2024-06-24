# Generated documentation for module arcpy.server


class ImportMapServerCache(object):
    """
    Imports tiles from a folder on disk into a map image layer cache.
    """

    @property
    def description(self) -> str:
        return """

        ImportMapServerCache_server(input_service, source_cache_type, {source_cache_dataset}, {source_tile_package}, {upload_data_to_server}, {scales;scales...}, {num_of_caching_service_instances}, {area_of_interest}, {import_extent}, {overwrite})

        Imports tiles from a folder on disk into a map image layer cache.

     INPUTS:
      input_service (Image Service / Map Server):
          The map image layer with the cache tiles to be imported.
      source_cache_type (String):
          Imports a cache from a cache dataset or tile package to a cached map
          or image service running on the server.CACHE_DATASET-A map or image
          service cache that is generated using
          ArcGIS Server. It can be used in ArcGIS Desktop and by ArcGIS Server
          map or image services.TILE_PACKAGE-A single compressed file where the
          cache dataset is added
          as a layer and consolidated so that it can be shared. It can be used
          in ArcGIS Desktop, ArcGIS Runtime, and mobile apps.
      source_cache_dataset {Raster Dataset}:
          The path to the cache folder matching the data frame name. You do not
          have to specify a registered server cache directory; most of the time
          you'll specify a location on disk where tiles have been previously
          exported. This location should be accessible to the ArcGIS Server
          account. If the ArcGIS Server account cannot be granted access to this
          location, set the upload_data_to_server parameter to UPLOAD_DATA.
      source_tile_package {File}:
          The path to the tile package (.tpk) that will be imported. This
          location should be accessible to the ArcGIS Server account. When
          importing a tile package file to a cached map or image service, the
          upload_data_to_server parameter is ignored as it is automatically set
          to UPLOAD_DATA.
      upload_data_to_server {Boolean}:
          Set this parameter to UPLOAD_DATA if the ArcGIS Server account does
          not have read access to the source cache. The tool will upload the
          source cache to the ArcGIS Server uploads directory before moving it
          to the ArcGIS Server cache directory.UPLOAD_DATA-Tiles are placed in
          the server uploads directory and are
          then moved to the server cache directory. This is enabled by default
          when source_cache_type is TILE_PACKAGE.DO_NOT_UPLOAD-Tiles are
          imported directly into the server cache
          directory. The ArcGIS Server account must have read access to the
          source cache.
      scales {Double}:
          A list of scale levels at which tiles will be imported.
      num_of_caching_service_instances {Long}:
          Specifies the number of instances that will be used to update or
          generate the tiles. The value for this parameter is set to unlimited
          (-1) and cannot be modified.
      area_of_interest {Feature Set}:
          An area of interest polygon that spatially constrains where tiles are
          imported into the cache. This parameter is useful if you want to
          import tiles for irregularly shaped areas, as the tool clips the cache
          dataset, which intersects the polygon at pixel resolution and imports
          it to the service cache directory. If you do not provide a
          value for this parameter, the value of
          theparameter will be used. The default is to use the full extent of
          the map. Import Extent
      import_extent {Extent}:
          A rectangular extent defining the tiles to be imported into
          the cache. By default, the extent is set to the full extent of the map
          service into which you are importing. Note that the optional parameter
          on this tool,, allows you to spatially constrain the imported tiles
          using an irregular shape. If values are provided for both parameters,
          theparameter takes precedence over. Area Of InterestArea Of
          InterestImport ExtentMAXOF-The maximum extent of all inputs will be
          used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      overwrite {Boolean}:
          Specifies whether the images in the destination cache will be merged
          with the tiles from the originating cache or overwritten by
          them.OVERWRITE-The import replaces all pixels in the area of interest,
          effectively overwriting tiles in the destination cache with tiles from
          the originating cache.MERGE-When the tiles are imported, transparent
          pixels in the
          originating cache are ignored by default. This results in a merged or
          blended image in the destination cache. This is the default.

        """