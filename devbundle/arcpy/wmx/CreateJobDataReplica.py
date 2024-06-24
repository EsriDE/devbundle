# Generated documentation for module arcpy.wmx


class CreateJobDataReplica(object):
    """
    Replicates the ArcGIS Workflow Manager (Classic) configuration from a parent repository to child repositories using ArcGIS Workflow Manager (Classic). Each child repository becomes an identical copy (replica) of the parent repository.
    """

    @property
    def description(self) -> str:
        return """

        CreateJobDataReplica_wmx(Input_Parent_Repository_URL, Input_Parent_Repository_Name, Input_Multi_Name;Input_Multi_Name...)

        Replicates the ArcGIS Workflow Manager (Classic) configuration from a
        parent repository to child repositories using ArcGIS Workflow Manager
        (Classic). Each child repository becomes an identical copy (replica)
        of the parent repository.

     INPUTS:
      Input_Parent_Repository_URL (String):
          The URL for the parent repository as the Workflow Manager (Classic)
          service URL, for example,
          http://localhost/arcgis/rest/services/parent/wmserver.
      Input_Parent_Repository_Name (String):
          The name of the parent repository that will distribute the Workflow
          Manager (Classic) jobs and configuration elements.
      Input_Multi_Name (Value Table):
          The child repositories that will be updated with the parent
          repository configuration. child_name-The name of the child
          repository.connected-Specify "true"
          if the child is participating in connected
          replication and both parent and child Workflow Manager (Classic)
          services are published and online. Specify "false" if the child is
          participating in disconnected replication. In this case, only the
          parent Workflow Manager (Classic) service is published and
          online.URL-If connected is "true", specify the URL of the child
          repository.
          If connected is "false", specify a folder location to contain the
          configuration file exported from the parent repository. This
          configuration file can be used with the Import Job Data tool to
          replicate the parent repository to this disconnected repository.

        """