# Generated documentation for module arcpy.management


class DisableAttachments(object):
    """
    Disables attachments on a geodatabase feature class or table. The tool deletes the attachment relationship class and attachment table.
    """

    @property
    def description(self) -> str:
        return """

        DisableAttachments_management(in_dataset)

        Disables attachments on a geodatabase feature class or table. The tool
        deletes the attachment relationship class and attachment table.

     INPUTS:
      in_dataset (Table View):
          The geodatabase table or feature class for which attachments will be
          disabled. The input must be in a version 10 or later geodatabase.

        """