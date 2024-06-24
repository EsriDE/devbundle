# Generated documentation for module arcpy.maritime


class ImportS100Cell(object):
    """
    Imports S-100 hydrographic data into a geodatabase created from a related S-100 Feature Catalogue.
    """

    @property
    def description(self) -> str:
        return """

        ImportS100Cell_maritime(in_feature_catalogue, in_base_cell, target_workspace, {in_update_cells;in_update_cells...})

        Imports S-100 hydrographic data into a geodatabase created from a
        related S-100 Feature Catalogue.

     INPUTS:
      in_feature_catalogue (File):
          An .xml file that follows the S-100 Feature Catalogue format as
          defined by the IHO. It describes the content of a data product and its
          specifications. The default file location for S-100 catalogue files is
          <installation location>\ArcGIS Maritime\Product
          Files\<version>\S-101\, provided the Maritime product files are
          installed.
      in_base_cell (File):
          The data contained in a base file in S-100 format.
      target_workspace (Workspace):
          The geodatabase to which all output data will be written.
      in_update_cells {File}:
          The data that will be updated in a base file in S-100 format.

        """