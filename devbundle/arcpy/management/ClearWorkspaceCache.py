# Generated documentation for module arcpy.management


class ClearWorkspaceCache(object):
    """
    Clears information about a workspace that has been cached in memory.
    """

    @property
    def description(self) -> str:
        return """

        ClearWorkspaceCache_management({in_data})

        Clears information about a workspace that has been cached in memory.

     INPUTS:
      in_data {Data Element / Layer}:
          The geodatabase, .sde connection file, or folder path representing the
          workspace that will be removed from the workspace cache. If no value
          is specified, all contents of the workspace cache will be cleared.

        """