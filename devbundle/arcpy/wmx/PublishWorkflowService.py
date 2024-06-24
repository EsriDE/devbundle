# Generated documentation for module arcpy.wmx


class PublishWorkflowService(object):
    """
    Uploads and shares a workflow service and a map service of job locations for an ArcGIS Workflow Manager (Classic) repository.
    """

    @property
    def description(self) -> str:
        return """

        PublishWorkflowService_wmx(service_name, aoi_service_name, server, out_service_draft_location, {input_database_path}, {server_folder}, {description}, {overwrite})

        Uploads and shares a workflow service and a map service of job
        locations for an ArcGIS Workflow Manager (Classic) repository.

     INPUTS:
      service_name (String):
          The name of the workflow service that will be uploaded and shared.
      aoi_service_name (String):
          The name of the map service that will be uploaded and shared.
      server (ServerConnection):
          The ArcGIS Server connection file (.ags) that contains the information
          needed to connect to ArcGIS Server or the URL to the ArcGIS Enterprise
          portal federated server.
      out_service_draft_location (Folder):
          The folder where service definitions will be saved.
      input_database_path {File}:
          The workflow connection file (.jtc) that contains the information
          needed to connect to the Workflow Manager (Classic) repository.The
          workflow connection in your ArcGIS Pro project will be used if a
          workflow connection file is not defined.
      server_folder {String}:
          The folder to which the services will be published on ArcGIS Server.If
          a folder is not specified, the services will be published to the
          root folder of ArcGIS Server.
      description {String}:
          A description of the services that will be published.
      overwrite {Boolean}:
          Specifies whether the service_name and aoi_service_name services will
          be overwritten.OVERWRITE-The services will be
          overwritten.NO_OVERWRITE-The services
          will not be overwritten. This is the
          default.

        """