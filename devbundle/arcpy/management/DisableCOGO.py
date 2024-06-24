# Generated documentation for module arcpy.management


class DisableCOGO(object):
    """
    Disables COGO on a line feature class and removes COGO fields and COGO-enabled labeling and symbology. COGO fields can be deleted.
    """

    @property
    def description(self) -> str:
        return """

        DisableCOGO_management(in_line_features)

        Disables COGO on a line feature class and removes COGO fields and
        COGO-enabled labeling and symbology. COGO fields can be deleted.

     INPUTS:
      in_line_features (Feature Layer):
          The line feature class that will have COGO disabled.

        """