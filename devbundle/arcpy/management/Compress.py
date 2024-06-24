# Generated documentation for module arcpy.management


class Compress(object):
    """
    Compresses an enterprise geodatabase by removing states not referenced by a version and redundant rows.
    """

    @property
    def description(self) -> str:
        return """

        Compress_management(in_workspace)

        Compresses an enterprise geodatabase by removing states not referenced
        by a version and redundant rows.

     INPUTS:
      in_workspace (Workspace):
          The database connection file that connects to the enterprise
          geodatabase to be compressed. Connect as the geodatabase
          administrator.

        """