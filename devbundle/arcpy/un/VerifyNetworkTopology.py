# Generated documentation for module arcpy.un


class VerifyNetworkTopology(object):
    """
    Verifies the network topology system tables and logs inconsistencies to an output log file.
    """

    @property
    def description(self) -> str:
        return """

        VerifyNetworkTopology_un(in_utility_network, {out_log_file})

        Verifies the network topology system tables and logs inconsistencies
        to an output log file.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network that will be verified for consistency.

     OUTPUTS:
      out_log_file {File}:
          The output log file containing the discovered issues.

        """