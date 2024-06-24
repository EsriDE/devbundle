# Generated documentation for module arcpy.management


class AlterVersion(object):
    """
    Alters the properties of a geodatabase version.
    """

    @property
    def description(self) -> str:
        return """

        AlterVersion_management(in_workspace, in_version, {name}, {description}, {access}, {target_owner})

        Alters the properties of a geodatabase version.

     INPUTS:
      in_workspace (Workspace):
          The database connection file to the enterprise, workgroup, or desktop
          geodatabase where the version to be altered is located. The default is
          to use the workspace defined in the Current Workspace environment.For
          branch versioning, use a feature service URL (that is, https://mys
          ite.mydomain/server/rest/services/ElectricNetwork/FeatureServer) or
          the feature layer portal item.
      in_version (String):
          The name of the version to be altered. If altering a branch version
          from a database connection connected as the geodatabase administrator,
          the version name must also include the service name, for example,
          myservice.versionowner.versionname.
      name {String}:
          The new name of the version.
      description {String}:
          The new description of the version.
      access {String}:
          Specifies the access permission for the version. If no value is
          specified, the access permission will not be updated.PRIVATE-Only the
          owner can view the version and modify available
          feature classes.PUBLIC-Any user can view the version and modify
          available feature
          classes.PROTECTED-Any user can view the version, but only the owner
          can modify
          available feature classes.
      target_owner {String}:
          The name of the portal user to which the version ownership will be
          transferred. Ensure that the target owner user exists; the tool does
          not check the validity of the owner name specified. This parameter is
          only applicable for branch versions.

        """