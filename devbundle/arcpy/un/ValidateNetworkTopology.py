# Generated documentation for module arcpy.un


class ValidateNetworkTopology(object):
    """
    Validates features with dirty areas in the network topology of a utility network after edits have been made.
    """

    @property
    def description(self) -> str:
        return """

        ValidateNetworkTopology_un(in_utility_network, {extent})

        Validates features with dirty areas in the network topology of a
        utility network after edits have been made.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network for which the network topology will be validated.
      extent {Extent}:
          The geographical extent that will be used to validate the network
          topology. This parameter is similar to the Extent geoprocessing
          environment.MAXOF-The maximum extent of all inputs will be
          used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.

        """