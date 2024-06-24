# Generated documentation for module arcpy.management


class RemoveJoin(object):
    """
    Removes a join from a feature layer or table view.
    """

    @property
    def description(self) -> str:
        return """

        RemoveJoin_management(in_layer_or_view, {join_name})

        Removes a join from a feature layer or table view.

     INPUTS:
      in_layer_or_view (Table View / Raster Layer / Mosaic Layer):
          The layer or table view from which the join will be removed.
      join_name {String}:
          The name of the join to be removed.If no name is provided, the tool
          will remove all joins from the input.

        """