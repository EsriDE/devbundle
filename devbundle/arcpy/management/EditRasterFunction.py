# Generated documentation for module arcpy.management


class EditRasterFunction(object):
    """
    Adds, replaces, or removes a function chain in a mosaic dataset or a raster layer that contains a raster function.
    """

    @property
    def description(self) -> str:
        return """

        EditRasterFunction_management(in_mosaic_dataset, {edit_mosaic_dataset_item}, {edit_options}, {function_chain_definition}, {location_function_name})

        Adds, replaces, or removes a function chain in a mosaic dataset or a
        raster layer that contains a raster function.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer / Raster Layer):
          The mosaic dataset or a raster layer. If you use a raster layer, it
          must have a function applied.
      edit_mosaic_dataset_item {Boolean}:
          Determines if edits affect functions or the entire mosaic
          dataset.EDIT_MOSAIC_DATASET-Edits affect the functions associated with
          the
          mosaic dataset. This is the default.EDIT_MOSAIC_DATASET_ITEM-Edits
          affect the functions associated with
          all of the items within the mosaic dataset.
      edit_options {String}:
          Insert, replace, or remove a function chain.INSERT-Insert the function
          chain above the Function Name of the
          existing chain. Specify the function chain in the
          location_function_name parameter. This is the default.REPLACE-Replace
          the existing function chain with the function chain
          specified in this tool. Specify the function chain below in the
          location_function_name parameter.REMOVE-Remove the function chain
          starting from the function specified
          in the location_function_name parameter.
      function_chain_definition {File}:
          Choose the function chain (rft.xml file) that you want to insert or
          replace.
      location_function_name {String}:
          Choose where to insert, replace, or remove the function chain within
          the existing function chain.

        """