# Generated documentation for module arcpy.un


class SetEdgeConnectivity(object):
    """
    Defines how features will connect to a line or edge object of a given asset type.
    """

    @property
    def description(self) -> str:
        return """

        SetEdgeConnectivity_un(in_utility_network, domain_network, line_featureclass, assetgroup, assettype, edge_connectivity)

        Defines how features will connect to a line or edge object of a given
        asset type.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network that contains the asset type with the edge
          connectivity to set.
      domain_network (String):
          The domain network that contains the asset type with the edge
          connectivity to set.
      line_featureclass (String):
          The name of the input feature class or table that contains the asset
          type with the edge connectivity to set.
      assetgroup (String):
          The asset group that contains the asset type with the edge
          connectivity to set.
      assettype (String):
          The asset type that requires the edge connectivity to set.
      edge_connectivity (String):
          Specifies the edge connectivity type that will be assigned to the
          asset type.ANY_VERTEX-Features will connect anywhere along the edge
          including end
          vertices.END_VERTEX-Features will only connect to the end vertex of an
          edge.

        """