# Generated documentation for module arcpy.indoors


class ClassifyIndoorPathways(object):
    """
    Classifies pathways that pass through selected unit spaces, such as conference rooms or service areas, as lower priority.
    """

    @property
    def description(self) -> str:
        return """

        ClassifyIndoorPathways_indoors(in_unit_features, target_pathways)

        Classifies pathways that pass through selected unit spaces, such as
        conference rooms or service areas, as lower priority.

     INPUTS:
      in_unit_features (Feature Layer):
          The input polygon features representing spaces in a building
          for which theparameter values will be classified. In the ArcGIS
          Indoors Information Model, this is the Units layer. Select features in
          the units layer before running the tool. Target Pathways
      target_pathways (Feature Layer):
          The existing feature class or feature layer in which pathways will be
          updated. In the Indoors model, this is the Pathways layer.

        """