# Generated documentation for module arcpy.tn


class ConvertGeometricNetworkToTraceNetwork(object):
    """
    Converts a geometric network to a trace network.
    """

    @property
    def description(self) -> str:
        return """

        ConvertGeometricNetworkToTraceNetwork_tn(in_geometric_network, out_trace_network_name)

        Converts a geometric network to a trace network.

     INPUTS:
      in_geometric_network (Geometric Network):
          The geometric network that will be converted to a trace
          network.Converting a geometric network to a trace network will drop
          the
          geometric network and create a trace network in its place. This change
          cannot be undone. Create a backup of the data before proceeding.
      out_trace_network_name (String):
          The name of the output trace network.

        """