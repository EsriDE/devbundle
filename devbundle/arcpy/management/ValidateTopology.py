# Generated documentation for module arcpy.management


class ValidateTopology(object):
    """
    Validates a geodatabase topology.
    """

    @property
    def description(self) -> str:
        return """

        ValidateTopology_management(in_topology, {visible_extent})

        Validates a geodatabase topology.

     INPUTS:
      in_topology (Topology Layer):
          The geodatabase topology to be validated.
      visible_extent {Boolean}:
          Specifies whether the current visible extent of the map or the full
          extent of the topology will be validated. If the tool is run in the
          Python window or in a Python script, the entire extent of the topology
          will be validated regardless of this parameter setting.Full_Extent-The
          entire extent of the topology will be validated. This
          is the default.Visible_Extent-Only the current visible extent will be
          validated.

        """