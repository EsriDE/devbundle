# Generated documentation for module arcpy.server


class ManageMapServerCacheTiles(object):
    """
    Creates and updates tiles in an existing web tile layer cache (in ArcGIS Enterprise or ArcGIS Online), map image layers in ArcGIS Enterprise, and cached map or image services in a stand-alone server. This tool is used to create new tiles, replace missing tiles, overwrite outdated tiles, and delete tiles.
    """

    @property
    def description(self) -> str:
        return """

        ManageMapServerCacheTiles_server(input_service, scales;scales..., update_mode, {num_of_caching_service_instances}, {area_of_interest}, {update_extent}, {wait_for_job_completion}, {portal_url})

        Creates and updates tiles in an existing web tile layer cache (in
        ArcGIS Enterprise or ArcGIS Online), map image layers in ArcGIS
        Enterprise, and cached map or image services in a stand-alone server.
        This tool is used to create new tiles, replace missing tiles,
        overwrite outdated tiles, and delete tiles.

     INPUTS:
      input_service (Image Service / Map Server):
          The web tile layer, web imagery layer, or map image layer whose cache
          tiles will be updated.
      scales (Double):
          A list of scale levels at which tiles will be created.
      update_mode (String):
          Specifies the mode that will be used to update the
          cache.RECREATE_EMPTY_TILES-Only tiles that are empty will be created.
          Existing tiles will be left unchanged. This option is not available
          for web tile layers published to ArcGIS
          Online.RECREATE_ALL_TILES-Existing tiles will be replaced and new
          tiles will
          be added if the extent has changed.DELETE_TILES-Tiles will be deleted
          from the cache. The cache folder
          structure will not be deleted.
      num_of_caching_service_instances {Long}:
          The total number of instances of the System/CachingTools service that
          will be dedicated to running this tool. If the default value of -1 is
          used, all the caching tool instances of the ArcGIS Enterprise setup
          will be used. Use a lower value to use fewer caching tool instances.
          You can increase thesetting of the System/CachingTools service
          using thewindow available through an administrative connection to
          ArcGIS Server. Ensure that the server machines can support the chosen
          number of instances. Maximum number of instances per
          machineService Editor        When connecting to a stand-alone server,
          the default number of
          instances is equal to the value of thesetting of the caching tool
          service. Maximum number of instances
      area_of_interest {Feature Set}:
          An area of interest that will constrain where tiles will be created or
          deleted. This parameter is useful for managing tiles for irregularly
          shaped areas. It is also useful when precaching some areas and leaving
          less-visited areas uncached.If you do not provide a value for this
          parameter, the default value
          uses the full extent of the map.
      update_extent {Extent}:
          A rectangular extent used to create or delete tiles, depending on the
          value of the update_mode parameter. If both the update_extent and
          area_of_interest parameter values are specified, the area_of_interest
          value will be used.MAXOF-The maximum extent of all inputs will be
          used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      wait_for_job_completion {Boolean}:
          Specifies whether the tool will continue to run while the cache job
          runs on ArcGIS Online or Portal for ArcGIS.WAIT-The tool will continue
          to run while the cache job runs on ArcGIS
          Online or Portal for ArcGIS. Using this option, you can request
          detailed progress reports at any time and view the geoprocessing
          messages as they appear. This is the default. It is recommended that
          you use this option in Python scripts.DO_NOT_WAIT-A job will be
          submitted to the server, allowing you to
          perform other geoprocessing tasks. Use this option when you are
          building a cache automatically at the time you publish the service.
          You can also set this option on any other cache that you build.
      portal_url {String}:
          The URL of the portal.

        """