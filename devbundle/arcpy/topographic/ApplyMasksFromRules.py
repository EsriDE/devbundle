# Generated documentation for module arcpy.topographic


class ApplyMasksFromRules(object):
    """
    Applies symbol layer masking to feature layers in a map based on an XML rule file and mask features created by the Make Mask From Rules tool.
    """

    @property
    def description(self) -> str:
        return """

        ApplyMasksFromRules_topographic(in_map, rule_file, in_feature_dataset)

        Applies symbol layer masking to feature layers in a map based on an
        XML rule file and mask features created by the Make Mask From Rules
        tool.

     INPUTS:
      in_map (Map):
          The input map containing symbolized features such as a map in a
          project or a MAPX file on disk.
      rule_file (File):
          The XML file containing rules to define how features should be masked
          based on colors and symbol parts.
      in_feature_dataset (Feature Dataset):
          The feature dataset containing the masking polygon feature classes
          created by the Make Mask From Rules tool.

        """