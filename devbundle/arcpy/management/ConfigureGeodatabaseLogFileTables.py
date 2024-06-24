# Generated documentation for module arcpy.management


class ConfigureGeodatabaseLogFileTables(object):
    """
    Alters the type of log file tables used by an earlier release enterprise geodatabase to maintain lists of records cached by ArcGIS.
    """

    @property
    def description(self) -> str:
        return """

        ConfigureGeodatabaseLogFileTables_management(input_database, log_file_type, {log_file_pool_size}, {use_tempdb})

        Alters the type of log file tables used by an earlier release
        enterprise geodatabase to maintain lists of records cached by ArcGIS.

     INPUTS:
      input_database (Workspace):
          A database connection (.sde file) to the enterprise geodatabase where
          the log file table configuration will be changed. The connection must
          be made as the geodatabase administrator.
      log_file_type (String):
          Specifies the type of log file tables the geodatabase will
          use.SESSION_LOG_FILE-Session-based log file tables for selection sets
          will
          be used. Session-based log file tables are dedicated to a single
          session and may contain multiple selection sets.SHARED_LOG_FILE-Shared
          log file tables for selection sets will be
          used. Shared log file tables are shared by all sessions that connect
          as the same user.
      log_file_pool_size {Long}:
          The number of tables included in the pool that the geodatabase will
          use if a pool of session-based log file tables owned by the
          geodatabase administrator is used.
      use_tempdb {Boolean}:
          This parameter is no longer applicable in any supported ArcGIS
          release.

        """