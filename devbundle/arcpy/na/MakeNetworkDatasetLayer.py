# Generated documentation for module arcpy.na


class MakeNetworkDatasetLayer(object):
    """
    Creates a network dataset layer from a network dataset.
    """

    @property
    def description(self) -> str:
        return """

        MakeNetworkDatasetLayer_na(in_network_dataset, output_layer, {draw_elements;draw_elements...})

        Creates a network dataset layer from a network dataset.

     INPUTS:
      in_network_dataset (Network Dataset Layer):
          The network dataset from which to make the new layer.
      draw_elements {String}:
          This parameter is not yet supported in ArcGIS Pro.

     OUTPUTS:
      output_layer (Network Dataset Layer):
          The name of the network dataset layer to be created.The layer can be
          used as an input to any geoprocessing tool that
          accepts a network dataset layer as input.

        """