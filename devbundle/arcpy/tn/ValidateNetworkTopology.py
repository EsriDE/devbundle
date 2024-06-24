# Generated documentation for module arcpy.tn


class ValidateNetworkTopology(object):
    """
    Validates the network topology of a trace network. Validation of the network topology is necessary after edits have been made to network attributes or the geometry of features in the network.
    """

    @property
    def description(self) -> str:
        return """

        ValidateNetworkTopology_tn(in_trace_network, {extent})

        Validates the network topology of a trace network. Validation of the
        network topology is necessary after edits have been made to network
        attributes or the geometry of features in the network.

     INPUTS:
      in_trace_network (Trace Network / Trace Network Layer):
          The trace network for which the network topology will be
          validated.When working with an enterprise geodatabase, the input trace
          network
          must be from a trace network service.
      extent {Extent}:
          The geographical area for which to build the trace network. This
          parameter is similar to the Extent geoprocessing environment.MAXOF-The
          maximum extent of all inputs will be used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.

        """