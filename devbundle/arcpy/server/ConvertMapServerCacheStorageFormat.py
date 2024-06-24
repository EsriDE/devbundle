# Generated documentation for module arcpy.server


class ConvertMapServerCacheStorageFormat(object):
    """
    Converts the storage of a map image layer or a map or image service cache between the exploded format and the compactV2 format.
    """

    @property
    def description(self) -> str:
        return """

        ConvertMapServerCacheStorageFormat_server(input_service, {num_of_caching_service_instances})

        Converts the storage of a map image layer or a map or image service
        cache between the exploded format and the compactV2 format.

     INPUTS:
      input_service (Image Service / Map Server):
          The map or image service whose cache format will be converted. In
          ArcGIS Enterprise, this is a string containing the REST endpoint of
          the map image layer. In a stand-alone ArcGIS Server deployment, this
          is a string containing both the server and the service information.
      num_of_caching_service_instances {Long}:
          The total number of instances of the System/CachingTools service that
          will be dedicated to running this tool. When the default value of -1
          is used, all the caching tool instances of the ArcGIS Enterprise setup
          will be used. Use a lower value to use fewer caching tool instances.
          You can increase thesetting of the System/CachingTools service
          using thewindow available through an administrative connection to
          ArcGIS Server. Ensure that the server machines can support the chosen
          number of instances. Maximum number of instances per
          machineService Editor        When connecting to a stand-alone server,
          the default number of
          instances is equal to the value of thesetting of the caching tool
          service. Maximum number of instances

        """