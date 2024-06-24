# Generated documentation for module arcpy.aviation


class PrepareAviationData(object):
    """
    Migrates attributes from main aviation data to their cartographic features based on specific JSON scripts. These attributes are used for labeling and symbolizing cartographic features. Attributes defined in the JSON will be copied from their locations in the main feature classes and formatted into output attributes also defined in the JSON.
    """

    @property
    def description(self) -> str:
        return """

        PrepareAviationData_aviation(target_gdb, config_file, {in_dataset_names;in_dataset_names...}, {aoi_features})

        Migrates attributes from main aviation data to their cartographic
        features based on specific JSON scripts. These attributes are used for
        labeling and symbolizing cartographic features. Attributes defined in
        the JSON will be copied from their locations in the main feature
        classes and formatted into output attributes also defined in the JSON.

     INPUTS:
      target_gdb (Workspace):
          The ArcGIS Aviation Charting schema workspace on which the evaluation
          will be run.
      config_file (File):
          The .json file containing the evaluation criteria.
      in_dataset_names {String}:
          The names of the tables and feature classes that will be evaluated.
      aoi_features {Feature Layer}:
          An area of interest polygon layer that will be used to spatially
          filter source features.

        """