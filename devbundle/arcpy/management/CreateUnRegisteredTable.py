# Generated documentation for module arcpy.management


class CreateUnRegisteredTable(object):
    """
    Creates an empty table in an enterprise or mobile geodatabase. The table is not registered with the geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        CreateUnRegisteredTable_management(out_path, out_name, {template;template...}, {config_keyword})

        Creates an empty table in an enterprise or mobile geodatabase. The
        table is not registered with the geodatabase.

     INPUTS:
      out_path (Workspace):
          The enterprise geodatabase or mobile geodatabase in which the table
          will be created.
      out_name (String):
          The name of the table that will be created.
      template {Table View}:
          An existing dataset or list of datasets with fields and attribute
          schema that will be used to define the fields in the output table.
      config_keyword {String}:
          Specifies the default storage parameters (configurations) for
          geodatabases in a relational database management system (RDBMS). This
          setting is applicable only when using enterprise geodatabase
          tables.Configuration keywords are set by the database administrator.

        """