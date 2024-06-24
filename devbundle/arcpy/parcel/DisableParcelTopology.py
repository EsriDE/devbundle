# Generated documentation for module arcpy.parcel


class DisableParcelTopology(object):
    """
    Disables geodatabase topology on a parcel fabric. System-defined topology rules and parcel fabric feature classes will be removed from the topology.
    """

    @property
    def description(self) -> str:
        return """

        DisableParcelTopology_parcel(in_parcel_fabric)

        Disables geodatabase topology on a parcel fabric. System-defined
        topology rules and parcel fabric feature classes will be removed from
        the topology.

     INPUTS:
      in_parcel_fabric (Parcel Layer):
          The parcel fabric for which the topology will be disabled. The input
          parcel fabric can be from a file, enterprise, or mobile geodatabase.

        """