# Generated documentation for module arcpy.topographic


class GAIT(object):
    """
    Validates data using the Geospatial Analysis Integrity Tool (GAIT), checking geometry, feature codes, attribute values and domains, and metadata.
    """

    @property
    def description(self) -> str:
        return """

        GAIT_topographic(in_features;in_features..., gait_exe, folder, schema, project, format, metadata, silent, {reviewer_workspace}, {specfile})

        Validates data using the Geospatial Analysis Integrity Tool (GAIT),
        checking geometry, feature codes, attribute values and domains, and
        metadata.

     INPUTS:
      in_features (Table View / Feature Layer):
          The features to validate.
      gait_exe (File):
          The path to the GAIT executable file.
      folder (Folder):
          The shapefile export directory.
      schema (String):
          The data model that corresponds to the data displayed in the input
          feature layer.
      project (String):
          The name of the project. The project contains validation information,
          such as the checks run on the data and the results.
      format (String):
          The set of checks to run on the data. This is specific to the data
          model listed in the attribution schema.
      metadata (String):
          The metadata mapping table that corresponds to the data model of the
          input feature layer and the attribution schema.META_ESRI-Esri
          metadataMETA_INGR-Intergraph metadataMETA_MGCPNGA-MGCP
          NGA metadata
      silent (Boolean):
          Indicates the amount of output messages to return from
          GAIT.exe.SILENT-Limit messaging from GAIT.exe. This is the
          default.VERBOSE-Run
          GAIT.exe in verbose mode.
      reviewer_workspace {Workspace}:
          The workspace to write the output features. Each shapefile result
          record is written to the reviewer table in this workspace.
      specfile {File}:
          A file that defines custom checks.

        """