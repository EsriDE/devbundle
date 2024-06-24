# Generated documentation for module arcpy.aviation


class GenerateAviationCartographicFeatures(object):
    """
    Creates cartographic copies of features based on the area of interest (AOI) in which they're located.
    """

    @property
    def description(self) -> str:
        return """

        GenerateAviationCartographicFeatures_aviation(source_target_carto_features;source_target_carto_features..., aoi_features, {extraction_query_table}, {inclusion_exclusion_table})

        Creates cartographic copies of features based on the area of interest
        (AOI) in which they're located.

     INPUTS:
      source_target_carto_features (Value Table):
          Associates source feature classes with the cartographic feature
          classes in which they will be generating features.The first row is the
          source feature class that features will be copied
          from, and the second row is the target cartographic feature class that
          features will be copied to.
      aoi_features (Feature Layer):
          A layer of AOI polygon features that will be used to spatially filter
          source features.
      extraction_query_table {Table View}:
          A table of where clauses that will be used to further filter source
          features based on an attribute query.
      inclusion_exclusion_table {Table View}:
          A table identifying manually included or excluded source features.

        """