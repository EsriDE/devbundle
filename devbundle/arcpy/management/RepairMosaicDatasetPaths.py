# Generated documentation for module arcpy.management


class RepairMosaicDatasetPaths(object):
    """
    Resets paths to source imagery if you have moved or copied a mosaic dataset.
    """

    @property
    def description(self) -> str:
        return """

        RepairMosaicDatasetPaths_management(in_mosaic_dataset, paths_list;paths_list..., {where_clause})

        Resets paths to source imagery if you have moved or copied a mosaic
        dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset with the broken paths.
      paths_list (Value Table):
          A list of the paths to remap. Include the current path stored in the
          mosaic dataset and the path to which it will be changed. You can enter
          an asterisk (*) as the original path if you wish to change all your
          paths.
      where_clause {SQL Expression}:
          An SQL expression to limit the repairs to selected rasters within the
          mosaic dataset.

        """