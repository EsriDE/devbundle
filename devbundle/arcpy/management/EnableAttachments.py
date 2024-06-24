# Generated documentation for module arcpy.management


class EnableAttachments(object):
    """
    Enables attachments on a geodatabase feature class or table. The tool creates the necessary attachment relationship class and attachment table that will store attachment files internally.
    """

    @property
    def description(self) -> str:
        return """

        EnableAttachments_management(in_dataset)

        Enables attachments on a geodatabase feature class or table. The tool
        creates the necessary attachment relationship class and attachment
        table that will store attachment files internally.

     INPUTS:
      in_dataset (Table View):
          The geodatabase table or feature class for which attachments will be
          enabled. The input must be in a version 10 or later geodatabase.

        """