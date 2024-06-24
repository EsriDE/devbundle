# Generated documentation for module arcpy.maritime


class ImportS57ToGeodatabase(object):
    """
    Imports an S-57 file into an ArcGIS Maritime geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        ImportS57ToGeodatabase_maritime(in_base_cell, target_workspace, {in_update_cells;in_update_cells...}, {in_product_config})

        Imports an S-57 file into an ArcGIS Maritime geodatabase.

     INPUTS:
      in_base_cell (File):
          The base cell file (*.000).
      target_workspace (Workspace):
          The workspace where all the objects will be written.
      in_update_cells {File}:
          Updates cell files (*.001 - *.999).
      in_product_config {File}:
          The product configuration file that will be imported.

        """