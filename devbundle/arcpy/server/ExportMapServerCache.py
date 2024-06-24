# Generated documentation for module arcpy.server


class ExportMapServerCache(object):
    """
    Exports tiles from a map image layer cache as a cache dataset or tile package to a folder on disk. The tiles can be imported into other caches, or they can be accessed from ArcGIS Desktop or mobile devices as a raster dataset, independent from their parent service.
    """

    @property
    def description(self) -> str:
        return """

        ExportMapServerCache_server(input_service, target_cache_path, export_cache_type, copy_data_from_server, storage_format_type, scales;scales..., {num_of_caching_service_instances}, {area_of_interest}, {export_extent}, {overwrite})

        Exports tiles from a map image layer cache as a cache dataset or tile
        package to a folder on disk. The tiles can be imported into other
        caches, or they can be accessed from ArcGIS Desktop or mobile devices
        as a raster dataset, independent from their parent service.

     INPUTS:
      input_service (Image Service / Map Server):
          The map image layer with the cache tiles to be exported.
      target_cache_path (Folder):
          The folder into which the cache will be exported. This folder
          does not have to be a registered server cache directory. The ArcGIS
          Server account must have write access to the target cache folder. If
          the server account cannot be granted write access to the destination
          folder but the ArcGIS Desktop or ArcGIS Pro client has write access to
          it, choose theparameter. Copy data from server
      export_cache_type (String):
          Exports a cache as a cache dataset or a tile package. Tile packages
          are suitable for ArcGIS Runtime and ArcGIS Mobile
          deployments.CACHE_DATASET-A map or image service cache that is
          generated using
          ArcGIS Server. It can be used in ArcGIS Desktop and by ArcGIS Server
          map or image services. This is the default.TILE_PACKAGE-A single
          compressed file where the cache dataset is added
          as a layer and consolidated so that it can be shared. In can be used
          in ArcGIS Desktop, ArcGIS Runtime, and mobile apps.
      copy_data_from_server (Boolean):
          Set this parameter to COPY_DATA if the ArcGIS Server account cannot be
          granted write access to the target folder and the ArcGIS Desktop or
          ArcGIS Pro client has write access to it. The software exports the
          tiles in the server output directory before moving them to the target
          folder.COPY_DATA-Tiles are placed in the server output directory and
          are then
          moved to the target folder. The ArcGIS Desktop or ArcGIS Pro client
          must have write access to the target folder.DO_NOT_COPY-Tiles are
          exported directly into the target folder. The
          ArcGIS Server account must have write access to the target folder.
          This is the default.
      storage_format_type (String):
          The storage format of the exported cache.COMPACT-Tiles are grouped in
          bundle and bundlex files to save space
          on disk and allow for faster copying of caches. If the
          export_cache_type parameter is set to Tile package, this is the
          default.COMPACT_V2-Tiles are grouped in bundle files only. This
          format
          provides better performance on network shares and cloudstore
          directories. If the export_cache_type parameter is set to Tile package
          then the extension of the tile package is (.tpkx),which is supported
          by newer versions of the ArcGIS Platform such as ArcGIS Online, ArcGIS
          Enterprise 11.3 and ArcGIS Runtime 100.5.EXPLODED-Each tile is stored
          as an individual file (the way caches
          were stored prior to ArcGIS Server).
      scales (Double):
          A list of scale levels at which tiles will be exported.
      num_of_caching_service_instances {Long}:
          Specifies the number of instances that will be used to update or
          generate the tiles. The value for this parameter is set to unlimited
          (-1) and cannot be modified.
      area_of_interest {Feature Set}:
          An area of interest that spatially constrains where tiles are exported
          from the cache. This parameter is useful if you want to export
          irregularly shaped areas, as the tool clips the cache dataset at pixel
          resolution.If you do not specify an area of interest, the full extent
          of the map
          is exported.
      export_extent {Extent}:
          A rectangular extent defining the tiles to be exported. By
          default, the extent is set to the full extent of the map service into
          which you are importing. Note that the optional parameter on this
          tool,, allows you to alternatively import using a polygon. It is
          recommended that you not provide values for both parameters for a job.
          If values are provided for both parameters, theparameter takes
          precedence over. Area Of InterestArea Of InterestImport
          ExtentMAXOF-The maximum extent of all inputs will be used.MINOF-The
          minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      overwrite {Boolean}:
          Specifies whether the images in the receiving cache will be merged
          with the tiles from the originating cache or overwritten by
          them.OVERWRITE-The export replaces all pixels in the area of interest,
          effectively overwriting tiles in the destination cache with tiles from
          the originating cache.MERGE-When the tiles are imported, transparent
          pixels in the
          originating cache are ignored by default. This results in a merged or
          blended image in the destination cache. This is the default.

        """