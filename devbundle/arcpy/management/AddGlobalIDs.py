# Generated documentation for module arcpy.management


class AddGlobalIDs(object):
    """
    Adds global IDs to a list of geodatabase feature classes, tables, and feature datasets.
    """

    @property
    def description(self) -> str:
        return """

        AddGlobalIDs_management(in_datasets;in_datasets...)

        Adds global IDs to a list of geodatabase feature classes, tables, and
        feature datasets.

     INPUTS:
      in_datasets (Layer / Table View / Dataset):
          A list of geodatabase classes, tables, and feature datasets to which
          global IDs will be added.

        """