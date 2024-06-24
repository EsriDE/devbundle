# Generated documentation for module arcpy.management


class UpdatePortalDatasetOwner(object):
    """
    Updates the portal owner of a dataset to another user.
    """

    @property
    def description(self) -> str:
        return """

        UpdatePortalDatasetOwner_management(in_dataset, target_owner)

        Updates the portal owner of a dataset to another user.

     INPUTS:
      in_dataset (Utility Network / Utility Network Layer / Trace Network / Trace Network Layer):
          The input dataset for which the portal owner will be updated.
      target_owner (String):
          The name of the portal user who will be the new portal owner of the
          dataset.

        """