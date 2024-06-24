# Generated documentation for module arcpy.aviation


class ImportFAA18BShapefiles(object):
    """
    Imports one or more FAA Advisory Circular 150/5300-18B compliant shapefiles into a geodatabase that contains the ArcGIS Aviation Airports schema.
    """

    @property
    def description(self) -> str:
        return """

        ImportFAA18BShapefiles_aviation(in_features;in_features..., airports_workspace)

        Imports one or more FAA Advisory Circular 150/5300-18B compliant
        shapefiles into a geodatabase that contains the ArcGIS Aviation
        Airports schema.

     INPUTS:
      in_features (Shapefile):
          The FAA 18B shapefiles that will be imported into a geodatabase.
      airports_workspace (Workspace):
          The geodatabase into which the shapefiles will be imported.

        """