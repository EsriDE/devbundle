# Generated documentation for module arcpy.topographic


class CreateCrossReferenceGeodatabase(object):
    """
    Creates a cross-reference geodatabase that the Load Data tool uses to map source data to target data when loading batch data.
    """

    @property
    def description(self) -> str:
        return """

        CreateCrossReferenceGeodatabase_topographic(source_workspace, target_database, out_database, {mapping_file})

        Creates a cross-reference geodatabase that the Load Data tool uses to
        map source data to target data when loading batch data.

     INPUTS:
      source_workspace (LocalDatabase|RemoteDatabase|FileSystem):
          The workspace, either a geodatabase or shapefile directory, that
          contains the schema of data that will be mapped to the target
          workspace.
      target_database (Workspace):
          The geodatabase that contains the schema of the database to which the
          source will be mapped.
      mapping_file {File}:
          An Excel spreadsheet that contains information on how the source
          features, fields, and attribute value will be mapped to the
          target_database parameter value.

     OUTPUTS:
      out_database (Workspace):
          The file geodatabase that will be created containing the mapping from
          the source_workspace parameter value to the target_database parameter
          value.

        """