# Generated documentation for module arcpy.ba


class AddVariableBasedSuitabilityCriteria(object):
    """
    Adds criteria based on the values calculated for the input layer using the Enrich Layer tool.
    """

    @property
    def description(self) -> str:
        return """

        AddVariableBasedSuitabilityCriteria_ba(in_analysis_layer, variables;variables...)

        Adds criteria based on the values calculated for the input layer using
        the Enrich Layer tool.

     INPUTS:
      in_analysis_layer (Feature Layer):
          The Suitability Analysis layer that will be used in the analysis.
      variables (String):
          The variables from which the suitability criteria will be determined.

        """