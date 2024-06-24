# Generated documentation for module arcpy.wmx


class ClearJobReplicationInfo(object):
    """
    Deletes the replication information on a parent repository and sends a web service call to all the child repositories in the cluster. Consequently, the replication information is cleared from all the repositories participating in the cluster.
    """

    @property
    def description(self) -> str:
        return """

        ClearJobReplicationInfo_wmx(Input_Repository_URL, {Input_DatabasePath})

        Deletes the replication information on a parent repository and sends a
        web service call to all the child repositories in the cluster.
        Consequently, the replication information is cleared from all the
        repositories participating in the cluster.

     INPUTS:
      Input_Repository_URL (String):
          The URL for the Workflow Manager (Classic) Server Object as defined on
          the server.For example,
          http://ServerName/arcgis/rest/services/ServerObjectName/WMServer.
      Input_DatabasePath {File}:
          The Workflow Manager (Classic) connection file (.jtc) for the database
          from which to delete the replication information. If no connection
          file is specified, the current default Workflow Manager (Classic)
          database is used.

        """