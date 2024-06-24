# Generated documentation for module arcpy.management


class DiagnoseVersionTables(object):
    """
    Identifies inconsistencies in the delta (A and D) tables of datasets that are registered for traditional versioning.
    """

    @property
    def description(self) -> str:
        return """

        DiagnoseVersionTables_management(input_database, out_log, {target_version}, {input_tables;input_tables...})

        Identifies inconsistencies in the delta (A and D) tables of datasets
        that are registered for traditional versioning.

     INPUTS:
      input_database (Workspace):
          The database connection (.sde file) to the enterprise geodatabase in
          which delta table inconsistencies may exist. The connection must be
          made as the geodatabase administrator.
      target_version {String}:
          The geodatabase version with the delta tables that will be checked for
          inconsistencies. If no version is specified, all versions are
          processed.
      input_tables {String}:
          A single table or a text file containing a list of versioned tables
          with the associated delta tables to be checked for inconsistencies.
          Use fully-qualified table names in the text file, and place one table
          name per line. If no file is specified, all tables in the geodatabase
          are processed.

     OUTPUTS:
      out_log (File):
          The path and name of the output log file. The log file is an ASCII
          file containing a list of the tables in the specified version that
          contain inconsistent records, as well as information about the
          connection file, geodatabase version, and tables for which the tool
          was run.

        """