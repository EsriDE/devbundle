# Generated documentation for module arcpy.un


class RebuildNetworkTopology(object):
    """
    Rebuilds the network topology in a specified extent to address errors identified during the validate network topology operation.
    """

    @property
    def description(self) -> str:
        return """

        RebuildNetworkTopology_un(in_utility_network, extent)

        Rebuilds the network topology in a specified extent to address errors
        identified during the validate network topology operation.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network for which the network topology will be rebuilt.
      extent (Extent):
          Specifies the geographical extent that will be used to rebuild the
          network topology.MAXOF-The maximum extent of all inputs will be
          used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.

        """