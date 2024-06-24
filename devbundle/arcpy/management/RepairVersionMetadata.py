# Generated documentation for module arcpy.management


class RepairVersionMetadata(object):
    """
    Repairs inconsistencies in the versioning system tables of a geodatabase that contains traditional versions.
    """

    @property
    def description(self) -> str:
        return """

        RepairVersionMetadata_management(input_database, out_log)

        Repairs inconsistencies in the versioning system tables of a
        geodatabase that contains traditional versions.

     INPUTS:
      input_database (Workspace):
          The database connection (.sde file) to the enterprise geodatabase in
          which versioning system table inconsistencies exist. The connection
          must be made as the geodatabase administrator.

     OUTPUTS:
      out_log (File):
          The output log file. The log file is an ASCII file containing the
          results of the repair operation.

        """