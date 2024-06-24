# Generated documentation for module arcpy.management


class DiagnoseVersionMetadata(object):
    """
    Identifies inconsistencies in the system tables used to manage traditional versions and states in a geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        DiagnoseVersionMetadata_management(input_database, out_log)

        Identifies inconsistencies in the system tables used to manage
        traditional versions and states in a geodatabase.

     INPUTS:
      input_database (Workspace):
          The database connection (.sde file) to the enterprise geodatabase in
          which traditional versioning system table inconsistencies may
          exist.The connection must be made as the geodatabase administrator.

     OUTPUTS:
      out_log (File):
          The name and location of the output log file.The log file is an ASCII
          file containing a list of the system tables
          in the specified version that contain inconsistent records, as well as
          the database connection file used.

        """