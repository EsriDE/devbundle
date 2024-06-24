# Generated documentation for module arcpy.ba


class MakeSuitabilityAnalysisLayer(object):
    """
    Creates a Suitability Analysis layer for a given input site's polygonal layer.
    """

    @property
    def description(self) -> str:
        return """

        MakeSuitabilityAnalysisLayer_ba(in_features, layer_name)

        Creates a Suitability Analysis layer for a given input site's
        polygonal layer.

     INPUTS:
      in_features (Feature Layer):
          The feature layer that will be used in the creation of the Suitability
          Analysis layer.
      layer_name (String):
          The name of the output Suitability Analysis layer to be created.

        """