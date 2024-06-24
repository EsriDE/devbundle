# Generated documentation for module arcpy.server


class ManageMapServerCacheStatus(object):
    """
    Manages internal data kept by the server about the built tiles in a map or image service cache.
    """

    @property
    def description(self) -> str:
        return """

        ManageMapServerCacheStatus_server(input_service, manage_mode, {scales;scales...}, {num_of_caching_service_instances}, {report_folder}, {area_of_interest}, {report_extent})

        Manages internal data kept by the server about the built tiles in a
        map or image service cache.

     INPUTS:
      input_service (Image Service / Map Server):
          The map image layer for which the cache status will be
          modified.. You can choose it by browsing to the desired service in
          Portal or you can drag and drop a web tile layer from thepanetab to
          supply this parameter. CatalogPortal
      manage_mode (String):
          DELETE_CACHE_STATUS-Deletes the status information used by the
          server.REBUILD_CACHE_STATUS-Deletes, then rebuilds the status
          information
          used by the server. REPORT_BUNDLE_STATUS-Creates status
          information in a new file
          geodatabase named Status.gdb in a folder you specify in theparameter.
          This option is used when you want to create a custom status report for
          a particular area of interest or set of scales. Output Folder
      scales {Double}:
          The scale levels for which the status will be modified. This parameter
          is only applicable when building a custom status using the
          REPORT_BUNDLE_STATUS option for the manage_mode parameter.
      num_of_caching_service_instances {Long}:
          Defines the number of instances that will be used to update/generate
          the tiles. The value for this parameter is set to unlimited (-1) and
          cannot be modified.
      report_folder {Folder}:
          Output folder for the Status.gdb. This parameter is only applicable
          when building a custom status using the REPORT_BUNDLE_STATUS option.
      area_of_interest {Feature Set}:
          An area of interest (polygon) that determines what geography the
          status report will cover. This parameter is only applicable when
          building a custom status using the REPORT_BUNDLE_STATUS option.
      report_extent {Extent}:
          A rectangular extent defining the area for which the status will be
          built. This parameter is only applicable when building a custom status
          using the REPORT_BUNDLE_STATUS option.Note that the area_of_interest
          parameter allows you to specify an area
          of interest that is nonrectangular.MAXOF-The maximum extent of all
          inputs will be used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.

        """