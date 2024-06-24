# Generated documentation for module arcpy.tn


class EnableNetworkTopology(object):
    """
    Enables a network topology for a trace network.
    """

    @property
    def description(self) -> str:
        return """

        EnableNetworkTopology_tn(in_trace_network, {max_number_of_errors}, {only_generate_errors})

        Enables a network topology for a trace network.

     INPUTS:
      in_trace_network (Trace Network / Trace Network Layer):
          The trace network for which the network topology will be enabled.
      max_number_of_errors {Long}:
          The maximum number of errors that can occur before the process of
          enabling the network topology will stop. Errors will be recorded in
          the errors table. The default value is 10000.Increasing the maximum
          number of errors value will increase the length
          of time it takes to enable the topology. Setting a value higher than
          the default value of 10000 is not recommended.
      only_generate_errors {Boolean}:
          Specifies whether the topology will be enabled or only network errors
          will be generated.ONLY_ERRORS-The trace network will only be evaluated
          for network
          errors. The topology will not be enabled. If you are working with an
          enterprise geodatabase, the data cannot be registered as versioned.
          This allows you to inspect and fix errors in the network until you
          enable the topology.ENABLE_TOPO-The topology will be enabled and any
          errors that exist
          will generate error features. This is the default.

        """