# Generated documentation for module arcpy.ba


class AddFieldBasedSuitabilityCriteria(object):
    """
    Adds criteria based on the numerical fields existing in the input layer.
    """

    @property
    def description(self) -> str:
        return """

        AddFieldBasedSuitabilityCriteria_ba(in_analysis_layer, fields;fields...)

        Adds criteria based on the numerical fields existing in the input
        layer.

     INPUTS:
      in_analysis_layer (Feature Layer):
          The Suitability Analysis layer that will be used in the analysis.
      fields (Field):
          The numeric fields from which the suitability criteria will be
          determined.

        """