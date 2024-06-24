# Generated documentation for module arcpy.management


class EnableCOGO(object):
    """
    Enables COGO on a line feature class and adds COGO fields and COGO- enabled labeling to a line feature class. COGO fields store dimensions that are used to create line features in relation to each other.
    """

    @property
    def description(self) -> str:
        return """

        EnableCOGO_management(in_line_features)

        Enables COGO on a line feature class and adds COGO fields and COGO-
        enabled labeling to a line feature class. COGO fields store dimensions
        that are used to create line features in relation to each other.

     INPUTS:
      in_line_features (Feature Layer):
          The line feature class that will be COGO enabled.

        """