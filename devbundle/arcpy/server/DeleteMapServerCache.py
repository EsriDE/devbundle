# Generated documentation for module arcpy.server


class DeleteMapServerCache(object):
    """
    Deletes an existing map image layer cache, including all associated files on disk.
    """

    @property
    def description(self) -> str:
        return """

        DeleteMapServerCache_server(input_service, {num_of_caching_service_instances})

        Deletes an existing map image layer cache, including all associated
        files on disk.

     INPUTS:
      input_service (Image Service / Map Server):
          The map image layer whose cache tiles you want to delete.
      num_of_caching_service_instances {Long}:
          Defines the number of instances that will be used to update/generate
          the tiles. The value for this parameter is set to unlimited (-1) and
          cannot be modified.

        """