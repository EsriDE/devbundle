# Generated documentation for module arcpy.maritime


class TransferQualityOfPosition(object):
    """
    Transfers the Quality of Position (QUAPOS) attribution from S-57 edge primitives (captured in PLTS_SpatialAttributeL) to the feature to aid in symbolization dependent on this attribute.
    """

    @property
    def description(self) -> str:
        return """

        TransferQualityOfPosition_maritime(in_geodatabase, {unverified_features_only})

        Transfers the Quality of Position (QUAPOS) attribution from S-57 edge
        primitives (captured in PLTS_SpatialAttributeL) to the feature to aid
        in symbolization dependent on this attribute.

     INPUTS:
      in_geodatabase (Workspace):
          The input geodatabase that contains the chart data in the maritime
          chart schema.
      unverified_features_only {Boolean}:
          Specifies whether only features marked as unverified will be
          processed.UNVERIFIED_FEATURES-Only features marked as unverified will
          be
          processed.ALL_FEATURES-All features will be processed. This is the
          default.

        """