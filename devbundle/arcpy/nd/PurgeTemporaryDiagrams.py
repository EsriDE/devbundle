# Generated documentation for module arcpy.nd


class PurgeTemporaryDiagrams(object):
    """
    Purges temporary network diagrams related to a given utility network or trace network.
    """

    @property
    def description(self) -> str:
        return """

        PurgeTemporaryDiagrams_nd(in_utility_network, {created_before})

        Purges temporary network diagrams related to a given utility network
        or trace network.

     INPUTS:
      in_utility_network (Utility Network / Trace Network):
          The utility network or trace network data element with the temporary
          diagrams to be purged.
      created_before {Date}:
          The cutoff date for temporary network diagrams to be purged. All
          temporary network diagrams created before this date will be purged.If
          no date is specified, all temporary diagrams in the database will
          be purged.

        """