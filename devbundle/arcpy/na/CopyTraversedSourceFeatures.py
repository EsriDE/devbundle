# Generated documentation for module arcpy.na


class CopyTraversedSourceFeatures(object):
    """
    Creates two feature classes and a table, which together contain information about the edges, junctions, and turns that are traversed while solving a network analysis layer.
    """

    @property
    def description(self) -> str:
        return """

        CopyTraversedSourceFeatures_na(input_network_analysis_layer, output_location, edge_feature_class_name, junction_feature_class_name, turn_table_name)

        Creates two feature classes and a table, which together contain
        information about the edges, junctions, and turns that are traversed
        while solving a network analysis layer.

     INPUTS:
      input_network_analysis_layer (Network Analyst Layer):
          The network analysis layer from which traversed source features will
          be copied. If the network analysis layer does not have a valid result,
          the layer will be solved to produce one.
      output_location (Workspace / Feature Dataset):
          The workspace where the output table and two feature classes will be
          saved.
      edge_feature_class_name (String):
          The name of the feature class that will contain information about the
          traversed edge source features. If the solved network analysis layer
          doesn't traverse any edge features, an empty feature class will be
          created.
      junction_feature_class_name (String):
          The name of the feature class that will contain information about the
          traversed junction source features, including system junctions and
          relevant points from the input network analysis layer. If the solved
          network analysis layer doesn't traverse any junctions, an empty
          feature class will be created.
      turn_table_name (String):
          The name of the table that will contain information about the
          traversed global turns and turn features that scale cost for the
          underlying edges. If the solved network analysis layer doesn't
          traverse any turns, an empty table will be created. Since restricted
          turns are never traversed, they are never included in the output.

        """