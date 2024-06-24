# Generated documentation for module arcpy.un


class EnableNetworkTopology(object):
    """
    Enables a network topology for a utility network.
    """

    @property
    def description(self) -> str:
        return """

        EnableNetworkTopology_un(in_utility_network, {max_number_of_errors}, {only_generate_errors})

        Enables a network topology for a utility network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network for which the network topology will be enabled.
      max_number_of_errors {Long}:
          The maximum number of errors that can be generated before the process
          of enabling the network topology will stop. Errors will be recorded in
          the dirty areas sublayer. The default value is 10000.Increasing the
          maximum number of errors value will increase the length
          of time to enable the topology. Setting a value higher than the
          default value of 10000 is not recommended.
      only_generate_errors {Boolean}:
          Specifies whether the topology will be enabled or only network errors
          will be generated.ONLY_ERRORS-The utility network will only be
          evaluated for network
          errors. The topology will not be enabled. If you are working with an
          enterprise geodatabase, the data cannot be registered as versioned.
          This allows you to inspect and fix errors in the network until you are
          ready to enable the topology.ENABLE_TOPO-The topology will be enabled
          and any existing errors will
          generate dirty areas with errors. This is the default.

        """