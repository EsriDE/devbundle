# Generated documentation for module arcpy.server


class ManageMapServerCacheScales(object):
    """
    Updates the scale levels in an existing map image layer in ArcGIS Enterprise or in a cached map or image service on a stand-alone server. Use this tool to add new scales or delete existing scales from a cache.
    """

    @property
    def description(self) -> str:
        return """

        ManageMapServerCacheScales_server(input_service, scales;scales...)

        Updates the scale levels in an existing map image layer in ArcGIS
        Enterprise or in a cached map or image service on a stand-alone
        server. Use this tool to add new scales or delete existing scales from
        a cache.

     INPUTS:
      input_service (Image Service / Map Server):
          The map image layer or map or image service where cache scales will be
          added or removed. In ArcGIS Enterprise, this is a string containing
          the REST endpoint of the web map image layer. In a stand-alone ArcGIS
          Server, this is a string containing both the server and the service
          information.
      scales (Value Table):
          The scale values that will be included in the updated tiling scheme.

        """