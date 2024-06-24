# Generated documentation for module arcpy.na


class CopyNetworkAnalysisLayer(object):
    """
    Copies a network analysis layer to a duplicate layer. The new layer will have the same analysis settings and network data source as the original layer and a copy of the original layer's analysis data.
    """

    @property
    def description(self) -> str:
        return """

        CopyNetworkAnalysisLayer_na(in_network_analysis_layer, {out_layer_name})

        Copies a network analysis layer to a duplicate layer. The new layer
        will have the same analysis settings and network data source as the
        original layer and a copy of the original layer's analysis data.

     INPUTS:
      in_network_analysis_layer (Network Analyst Layer):
          The network analysis layer to copy.
      out_layer_name {String}:
          The name of the network analysis layer to create.

        """