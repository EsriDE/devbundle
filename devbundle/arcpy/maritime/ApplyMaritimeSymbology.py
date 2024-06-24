# Generated documentation for module arcpy.maritime


class ApplyMaritimeSymbology(object):
    """
    Applies maritime paper chart symbols to layers based on a CXML format file that contains rules.
    """

    @property
    def description(self) -> str:
        return """

        ApplyMaritimeSymbology_maritime(target_features;target_features..., cxml_file)

        Applies maritime paper chart symbols to layers based on a CXML format
        file that contains rules.

     INPUTS:
      target_features (Feature Class / Feature Layer):
          The input point, line, or polygon features.
      cxml_file (File):
          The .cxml file that contains rules for applying symbology.

        """