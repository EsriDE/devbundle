# Generated documentation for module arcpy.management


class UpgradeGDB(object):
    """
    Upgrades a geodatabase to the latest ArcGIS release to take advantage of new functionality.
    """

    @property
    def description(self) -> str:
        return """

        UpgradeGDB_management(input_workspace, input_prerequisite_check, input_upgradegdb_check)

        Upgrades a geodatabase to the latest ArcGIS release to take advantage
        of new functionality.

     INPUTS:
      input_workspace (Workspace):
          The geodatabase that will be upgraded. When upgrading an enterprise
          geodatabase, specify a database connection file (.sde) that connects
          to the geodatabase as the geodatabase administrator.
      input_prerequisite_check (Boolean):
          Specifies whether the prerequisite check will be run before upgrading
          the geodatabase.NO_PREREQUISITE_CHECK-The prerequisite check will not
          be
          run.PREREQUISITE_CHECK-The prerequisite check will be run before
          upgrading
          the geodatabase. This is the default.
      input_upgradegdb_check (Boolean):
          Specifies whether the input geodatabase will be
          upgraded.NO_UPGRADE-The geodatabase will not be upgraded.UPGRADE-The
          geodatabase will be upgraded. This is the default.

        """