# Generated documentation for module arcpy.topographic


class MakeMasksFromRules(object):
    """
    Creates polygon masks for features based on color rules.
    """

    @property
    def description(self) -> str:
        return """

        MakeMasksFromRules_topographic(in_map, rule_file, out_feature_dataset)

        Creates polygon masks for features based on color rules.

     INPUTS:
      in_map (Map):
          The map containing symbolized features.
      rule_file (File):
          The .xml file containing rules that define how features will be masked
          based on colors and symbol parts.

     OUTPUTS:
      out_feature_dataset (Feature Dataset):
          The output feature dataset. The tool will create a feature dataset
          containing polygon feature classes that will be used for masking. The
          spatial reference for the feature dataset will be taken from the map
          for which masks are generated.

        """