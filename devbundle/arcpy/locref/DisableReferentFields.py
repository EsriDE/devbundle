# Generated documentation for module arcpy.locref


class DisableReferentFields(object):
    """
    Disables referent fields for an existing linear referencing system (LRS) event feature class or feature layer. It does not delete the referent columns; it removes the referent column information from the Lrs_Metadata table.
    """

    @property
    def description(self) -> str:
        return """

        DisableReferentFields_locref(in_feature_class)

        Disables referent fields for an existing linear referencing system
        (LRS) event feature class or feature layer. It does not delete the
        referent columns; it removes the referent column information from the
        Lrs_Metadata table.

     INPUTS:
      in_feature_class (Feature Layer):
          The input feature class or feature layer for the LRS event.

        """