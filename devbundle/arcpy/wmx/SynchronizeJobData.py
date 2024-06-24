# Generated documentation for module arcpy.wmx


class SynchronizeJobData(object):
    """
    Synchronizes multiple Workflow Manager (Classic) repositories participating in a Workflow Manager (Classic) cluster. The tool performs two-way synchronization; changes from the child repositories are sent to the parent repository and changes from the parent are sent to all child repositories.
    """

    @property
    def description(self) -> str:
        return """

        SynchronizeJobData_wmx(Input_Parent_Repository_URL, Input_Parent_Repository_Name, Input_Multi_Name;Input_Multi_Name...)

        Synchronizes multiple Workflow Manager (Classic) repositories
        participating in a Workflow Manager (Classic) cluster. The tool
        performs two-way synchronization; changes from the child repositories
        are sent to the parent repository and changes from the parent are sent
        to all child repositories.

     INPUTS:
      Input_Parent_Repository_URL (String):
          The URL for the parent repository will be the Workflow Manager
          (Classic) server URL, for example,
          http://localhost/arcgis/rest/services/parent/wmserver.
      Input_Parent_Repository_Name (String):
          The parent repository that will distribute the Workflow Manager
          (Classic) jobs and configuration elements.
      Input_Multi_Name (Value Table):
          The child repositories that will be updated with the parent
          repository configuration. child_repository-The name of the
          child repository. This must be a
          connected repository.connected-The only accepted value is "true". If
          any other value is
          provided, the child will not be synchronized.URL-The URL of the child
          repository.last_sync_time-The date and time in the system format. For
          example, if
          your system data and time format is MM:DD:YY HH:MM:SS, the value will
          be 08/01/2013 11:30:45.

        """