# Generated documentation for module arcpy.topographic


class ExportMetadata(object):
    """
    Exports a Multinational Geospatial Co-production Program (MGCP) or MGCP Urban Vector Data (MUVD) metadata dataset (Cell or Resource, Subregion, and Source feature classes) to an .xml file.
    """

    @property
    def description(self) -> str:
        return """

        ExportMetadata_topographic(in_cell_features, export_location, {metadata_type})

        Exports a Multinational Geospatial Co-production Program (MGCP) or
        MGCP Urban Vector Data (MUVD) metadata dataset (Cell or Resource,
        Subregion, and Source feature classes) to an .xml file.

     INPUTS:
      in_cell_features (Feature Layer):
          The MGCP Cell or Resource feature layer that will be exported.
      export_location (Folder):
          The directory where the metadata .xml files will be created.
      metadata_type {String}:
          Specifies the type of metadata that will be
          exported.MGCP-Multinational Geospatial Co-production Program metadata
          will be
          exported. This is the default.MUVD-MGCP Urban Vector Data metadata
          will be exported.

        """