# Generated documentation for module arcpy.topographic


class UnzipCellAndImport(object):
    """
    Unzips and imports compressed Multinational Geospatial Co-production Program (MGCP) 1-degree-by-1-degree cell packages (*.zip) into a target geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        UnzipCellAndImport_topographic(Root_Folder, Target_Geodatabase)

        Unzips and imports compressed Multinational Geospatial Co-production
        Program (MGCP) 1-degree-by-1-degree cell packages (*.zip) into a
        target geodatabase.

     INPUTS:
      Root_Folder (Folder):
          The root folder that contains one or more compressed shapefile cell
          packages in a .zip file.
      Target_Geodatabase (Workspace):
          The geodatabase where the unzipped shapefiles will be imported.

        """