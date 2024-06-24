# Generated documentation for module arcpy.ca


class GenerateSectorLines(object):
    """
    Creates line features that represent the extent of cell site antenna sectors.
    """

    @property
    def description(self) -> str:
        return """

        GenerateSectorLines_ca(in_site_features, out_feature_class)

        Creates line features that represent the extent of cell site antenna
        sectors.

     INPUTS:
      in_site_features (Feature Layer):
          The point feature class derived from the Cell Site Records to Feature
          Class or Cell Phone Records to Feature Class tool.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the sector lines.

        """