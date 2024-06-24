# Generated documentation for module arcpy.topographic


class ImportMetadata(object):
    """
    Imports Multinational Geospatial Co-production Program (MGCP) or MGCP Urban Vector Data (MUVD) metadata to an MGCP or MUVD database.
    """

    @property
    def description(self) -> str:
        return """

        ImportMetadata_topographic(files;files..., in_cell_features, {metadata_type})

        Imports Multinational Geospatial Co-production Program (MGCP) or MGCP
        Urban Vector Data (MUVD) metadata to an MGCP or MUVD database.

     INPUTS:
      files (File):
          The .xml files that contain the metadata that will be imported.
      in_cell_features (Feature Layer):
          The Cell or Resource feature class where the metadata will be
          imported.
      metadata_type {String}:
          Specifies the type of metadata that will be
          imported.MGCP-Multinational Geospatial Co-production Program metadata
          will be
          imported. This is the default.MUVD-MGCP Urban Vector Data metadata
          will be imported.

        """