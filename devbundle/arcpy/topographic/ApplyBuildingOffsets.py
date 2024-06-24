# Generated documentation for module arcpy.topographic


class ApplyBuildingOffsets(object):
    """
    Aligns, moves, and hides building or bridge marker symbols based on product specification rules defined in an .xml file.
    """

    @property
    def description(self) -> str:
        return """

        ApplyBuildingOffsets_topographic(in_map, rule_file)

        Aligns, moves, and hides building or bridge marker symbols based on
        product specification rules defined in an .xml file.

     INPUTS:
      in_map (Map):
          The map that contains the layers with proper symbology. This can be a
          map in the application or an .mapx file on disk.
      rule_file (File):
          An .xml file containing the offset rules that define how features will
          be aligned and refined in case of any conflict.

        """