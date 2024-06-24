# Generated documentation for module arcpy.management


class CreateVersion(object):
    """
    Creates a new version in a specified geodatabase or feature service.
    """

    @property
    def description(self) -> str:
        return """

        CreateVersion_management(in_workspace, parent_version, version_name, {access_permission}, {version_description})

        Creates a new version in a specified geodatabase or feature service.

     INPUTS:
      in_workspace (Workspace):
          The enterprise geodatabase that contains the parent version and will
          contain the new version.For branch versioning, use a feature service
          URL (for example, https:/
          /mysite.mydomain/server/rest/services/ElectricNetwork/FeatureServer).
      parent_version (String):
          The geodatabase, or version of a geodatabase, on which the new version
          will be based.
      version_name (String):
          The name of the version that will be created.
      access_permission {String}:
          Specifies the permission access level for the version to protect it
          from being edited or viewed by users other than the owner.PRIVATE-Only
          the owner or the geodatabase administrator can view and
          modify the version or versioned data. This is the default.PUBLIC-Any
          user can view the version. Any user who has been granted
          read/write (update, insert, and delete) permissions on datasets can
          modify datasets in the version.PROTECTED-Any user can view the
          version, but only the owner or the
          geodatabase administrator can edit the version or datasets in the
          version.
      version_description {String}:
          The description of the version that will be created. The description
          cannot exceed 64 characters.

        """