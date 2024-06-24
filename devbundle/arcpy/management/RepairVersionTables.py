# Generated documentation for module arcpy.management


class RepairVersionTables(object):
    """
    Repairs inconsistencies in the delta (A and D) tables of datasets that are registered for traditional versioning.
    """

    @property
    def description(self) -> str:
        return """

        RepairVersionTables_management(input_database, out_log, {target_version}, {input_tables;input_tables...})

        Repairs inconsistencies in the delta (A and D) tables of datasets that
        are registered for traditional versioning.

     INPUTS:
      input_database (Workspace):
          The database connection (.sde file) to the enterprise geodatabase in
          which delta table inconsistencies exist. The connection must be made
          as the geodatabase administrator.
      target_version {String}:
          The geodatabase version to be repaired. If no version is specified,
          all versions are processed.
      input_tables {String}:
          A single table or a text file containing a list of versioned tables
          with the associated delta tables to be repaired. Use fully-qualified
          table names in the text file, and place one table name per line. If no
          table or file is specified, all tables are processed.

     OUTPUTS:
      out_log (File):
          The location where the log file will be written and the name of the
          log file. The log file is an ASCII file containing the results of the
          repair operation.

        """