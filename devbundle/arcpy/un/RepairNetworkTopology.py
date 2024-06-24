# Generated documentation for module arcpy.un


class RepairNetworkTopology(object):
    """
    Verifies and repairs inconsistencies identified in the network topology system tables.
    """

    @property
    def description(self) -> str:
        return """

        RepairNetworkTopology_un(in_utility_network, {out_log_file})

        Verifies and repairs inconsistencies identified in the network
        topology system tables.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network that will be repaired.

     OUTPUTS:
      out_log_file {File}:
          The folder location and name of the file containing the discovered
          issues.

        """