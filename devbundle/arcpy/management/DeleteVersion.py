# Generated documentation for module arcpy.management


class DeleteVersion(object):
    """
    Deletes the specified version from the input enterprise geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        DeleteVersion_management(in_workspace, version_name)

        Deletes the specified version from the input enterprise geodatabase.

     INPUTS:
      in_workspace (Workspace):
          The database connection file to the enterprise geodatabase containing
          the version to be deleted.For branch versioning, use a feature service
          URL (that is, https://mys
          ite.mydomain/server/rest/services/ElectricNetwork/FeatureServer) or a
          feature layer portal item.You can also delete a branch version using a
          database connection file
          (connected to a branch versioned workspace) when connected as the
          geodatabase admin user.
      version_name (String):
          The name of the version to be deleted.For branch versioning, if the
          input workspace is a database connection
          file, the name of the branch version to delete should be fully
          qualified (for example, servicename.portaluser.versionname). If the
          input workspace is a feature service URL, the name of the branch
          version to delete should not include the service name (for example,
          portaluser.versionname).

        """