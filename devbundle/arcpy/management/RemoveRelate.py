# Generated documentation for module arcpy.management


class RemoveRelate(object):
    """
    Removes a relate from a feature layer or a table view.
    """

    @property
    def description(self) -> str:
        return """

        RemoveRelate_management(in_layer_or_view, {relate_name})

        Removes a relate from a feature layer or a table view.

     INPUTS:
      in_layer_or_view (Table View / Raster Layer / Mosaic Layer):
          The layer or table view from which to remove the relate.
      relate_name {String}:
          The name of the relate to remove.

        """