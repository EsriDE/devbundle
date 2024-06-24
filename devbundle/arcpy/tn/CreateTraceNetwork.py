# Generated documentation for module arcpy.tn


class CreateTraceNetwork(object):
    """
    Creates a trace network.
    """

    @property
    def description(self) -> str:
        return """

        CreateTraceNetwork_tn(in_feature_dataset, in_trace_network_name, {input_junctions;input_junctions...}, {input_edges;input_edges...})

        Creates a trace network.

     INPUTS:
      in_feature_dataset (Feature Dataset):
          The feature dataset that will contain the trace network.
      in_trace_network_name (String):
          The name of the trace network that will be created.
      input_junctions {String}:
          The names of the point feature classes in the feature dataset that
          will be included in the trace network.
      input_edges {Value Table}:
          The line feature classes and associated connectivity policy
          that will be included in the trace network. Class Name-The name
          of the line feature class in the feature dataset
          that will be included in the trace network. Connectivity
          Policy-The associated connectivity policy of
          the specified feature class. SIMPLE_EDGE-Resources will flow
          from one end of the edge and out the
          other end.COMPLEX_EDGE-Resources will be siphoned off along the length
          of the
          edge.

        """