# Generated documentation for module arcpy.na


class DissolveNetwork(object):
    """
    Creates a network dataset that minimizes the number of line features required to correctly model the input network dataset. The more efficient output network dataset reduces the time required to solve analyses, draw results, and generate driving directions. This tool outputs a new network dataset and source feature classes; the input network dataset and its source features remain unchanged.
    """

    @property
    def description(self) -> str:
        return """

        DissolveNetwork_na(in_network_dataset, out_workspace_location)

        Creates a network dataset that minimizes the number of line features
        required to correctly model the input network dataset. The more
        efficient output network dataset reduces the time required to solve
        analyses, draw results, and generate driving directions. This tool
        outputs a new network dataset and source feature classes; the input
        network dataset and its source features remain unchanged.

     INPUTS:
      in_network_dataset (Network Dataset Layer):
          The network dataset to be dissolved. The input network dataset
          must be a file or personal
          geodatabase network dataset with exactly one edge source. Any number
          of junction sources and turn sources is allowed. The edge source must
          have:        End point connectivity policyAn elevation policy of
          either None or
          Elevation FieldsThe input network dataset must be built before it can
          be used in this
          tool.
      out_workspace_location (Workspace):
          The geodatabase workspace in which to create the dissolved network
          dataset. The workspace must be an ArcGIS 10 geodatabase or later, and
          it must be a different geodatabase than the one where the input
          network dataset resides.

        """