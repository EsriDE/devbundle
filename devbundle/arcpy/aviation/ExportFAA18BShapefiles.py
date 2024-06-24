# Generated documentation for module arcpy.aviation


class ExportFAA18BShapefiles(object):
    """
    Exports one or more FAA Advisory Circular 150/5300-18B compliant shapefiles from a geodatabase that contains the ArcGIS Aviation Airports schema.
    """

    @property
    def description(self) -> str:
        return """

        ExportFAA18BShapefiles_aviation(in_workspace, target_folder, {in_features;in_features...})

        Exports one or more FAA Advisory Circular 150/5300-18B compliant
        shapefiles from a geodatabase that contains the ArcGIS Aviation
        Airports schema.

     INPUTS:
      in_workspace (Workspace):
          The workspace that contains the airport data.
      target_folder (Folder):
          The folder where the shapefiles will be written.
      in_features {String}:
          A list of feature classes that will be exported to shapefiles. If this
          parameter is not set, all feature classes in the input workspace will
          be exported to shapefiles.

        """