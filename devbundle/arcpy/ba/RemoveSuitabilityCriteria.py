# Generated documentation for module arcpy.ba


class RemoveSuitabilityCriteria(object):
    """
    Removes criteria from a suitability analysis layer.
    """

    @property
    def description(self) -> str:
        return """

        RemoveSuitabilityCriteria_ba(in_analysis_layer, drop_criteria;drop_criteria...)

        Removes criteria from a suitability analysis layer.

     INPUTS:
      in_analysis_layer (Feature Layer):
          The suitability analysis layer from which criteria will be removed.
      drop_criteria (String):
          A list of criteria to be removed from a suitability analysis layer.

        """