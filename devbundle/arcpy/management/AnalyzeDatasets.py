# Generated documentation for module arcpy.management


class AnalyzeDatasets(object):
    """
    Updates database statistics of base tables, delta tables, and archive tables, along with the statistics on the indexes of those tables. This tool is used in enterprise geodatabases to help get optimal performance from the relational database management system (RDBMS) query optimizer. Stale statistics can affect geodatabase performance.
    """

    @property
    def description(self) -> str:
        return """

        AnalyzeDatasets_management(input_database, include_system, {in_datasets;in_datasets...}, {analyze_base}, {analyze_delta}, {analyze_archive})

        Updates database statistics of base tables, delta tables, and archive
        tables, along with the statistics on the indexes of those tables. This
        tool is used in enterprise geodatabases to help get optimal
        performance from the relational database management system (RDBMS)
        query optimizer. Stale statistics can affect geodatabase performance.

     INPUTS:
      input_database (Workspace):
          The database that contains the data to be analyzed.
      include_system (Boolean):
          Specifies whether statistics will be gathered on the states and state
          lineages tables.You must be the geodatabase administrator to use this
          parameter.This
          parameter only applies to geodatabases. If the input workspace is
          a database, this parameter will be ignored.NO_SYSTEM-Statistics will
          not be gathered on the states and state
          lineages tables. This is the default.SYSTEM-Statistics will be
          gathered on the states and state lineages
          tables.
      in_datasets {String}:
          The names of the datasets that will be analyzed. An individual dataset
          or a Python list of datasets can be used. Dataset names use paths
          relative to the input workspace; full paths are not valid input.The
          connected user must be the owner of the datasets provided.
      analyze_base {Boolean}:
          Specifies whether the selected dataset base tables will be
          analyzed.This parameter only applies to geodatabases. If the input
          workspace is
          a database, this parameter will be ignored.ANALYZE_BASE-Statistics
          will be gathered for the base tables for the
          selected datasets. This is the default.NO_ANALYZE_BASE-Statistics
          will not be gathered for the base tables
          for the selected datasets.
      analyze_delta {Boolean}:
          Specifies whether the selected dataset delta tables will be
          analyzed.This parameter only applies to geodatabases that contain
          traditional
          versions. If the input workspace is a database or does not participate
          in traditional versioning, this parameter will be
          ignored.ANALYZE_DELTA-Statistics will be gathered for the delta
          tables for
          the selected datasets. This is the default.NO_ANALYZE_DELTA-
          Statistics will not be gathered for the delta tables
          for the selected datasets.
      analyze_archive {Boolean}:
          Specifies whether the selected dataset archive tables will be
          analyzed.This parameter only applies to geodatabases that contain
          archive-
          enabled datasets. If the input workspace is a database, this parameter
          will be ignored.ANALYZE_ARCHIVE-Statistics will be gathered for the
          archive tables
          for the selected datasets. This is the default.NO_ANALYZE_ARCHIVE-
          Statistics will not be gathered for the archive
          tables for the selected datasets.

        """