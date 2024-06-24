# Generated documentation for module arcpy.topographic


class LoadData(object):
    """
    Moves features from one schema to another by loading data from a source to a target workspace. Data mapping rules described in a cross-reference database are applied during loading.
    """

    @property
    def description(self) -> str:
        return """

        LoadData_topographic(in_cross_reference, in_sources;in_sources..., in_target, {in_dataset_map_defs;in_dataset_map_defs...}, {row_level_errors})

        Moves features from one schema to another by loading data from a
        source to a target workspace. Data mapping rules described in a
        cross-reference database are applied during loading.

     INPUTS:
      in_cross_reference (Workspace):
          The path to a cross-reference database.
      in_sources (Workspace):
          A list of workspaces that contain the source features that will be
          loaded into the target workspace.
      in_target (Workspace):
          The target workspace that contains the schema referenced in the cross-
          reference database. Source features are loaded into this workspace.
      in_dataset_map_defs {String}:
          The source to target feature class mapping list. The format of this
          string is id | SourceDataset | TargetDataset | WhereClause | Subtype.
      row_level_errors {Boolean}:
          Specifies whether the tool will log errors that occur while inserting
          new rows into feature classes and tables in the in_target
          parameter.ROW_LEVEL_ERROR_LOGGING-Errors that occur during individual
          row-level
          inserts will be logged. This is the
          default.NO_ROW_LEVEL_ERROR_LOGGING-Errors that occur during individual
          row-
          level inserts will not be logged.

        """