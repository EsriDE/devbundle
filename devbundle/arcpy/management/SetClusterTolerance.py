# Generated documentation for module arcpy.management


class SetClusterTolerance(object):
    """
    Sets the cluster tolerance of a topology.
    """

    @property
    def description(self) -> str:
        return """

        SetClusterTolerance_management(in_topology, cluster_tolerance)

        Sets the cluster tolerance of a topology.

     INPUTS:
      in_topology (Topology Layer):
          The topology for which you want to change the cluster tolerance.
      cluster_tolerance (Double):
          The value to be set as the cluster tolerance property of the selected
          topology. If you enter a value of zero, the default or minimum cluster
          tolerance will be applied to the topology.

        """