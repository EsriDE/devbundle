# Generated documentation for module arcpy.topographic


class ApplyFeatureLevelMetadata(object):
    """
    Applies values from a metadata record in the FeatureLevelMetadata table to selected features that have matching attribute fields.
    """

    @property
    def description(self) -> str:
        return """

        ApplyFeatureLevelMetadata_topographic(in_features;in_features..., in_metadata_table, metadata_favorite)

        Applies values from a metadata record in the FeatureLevelMetadata
        table to selected features that have matching attribute fields.

     INPUTS:
      in_features (Feature Layer):
          The inputs to which the metadata_favorite parameter value will be
          applied.
      in_metadata_table (Table View):
          The path to the metadata table containing the records that will be
          used to populate attributes.
      metadata_favorite (String):
          The record that will be used to populate attributes. The available
          options depend on the records available in the metadata table.

        """