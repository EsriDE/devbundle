# Generated documentation for module arcpy.td


class AddTerritoryBarriers(object):
    """
    Allows the addition of polygon or line features to prevent or restrict the growth of territories.
    """

    @property
    def description(self) -> str:
        return """

        AddTerritoryBarriers_td(in_territory_solution, level, in_barrier_features, {barrier_type}, {append_data})

        Allows the addition of polygon or line features to prevent or restrict
        the growth of territories.

     INPUTS:
      in_territory_solution (Group Layer / Feature Dataset / String):
          The Territory Design solution layer that will be used in the analysis.
      level (String):
          The level to which the barriers will be applied.
      in_barrier_features (Feature Layer):
          Line or polygon features used as a barrier.
      barrier_type {String}:
          Specifies the type of barrier.IMPEDANCE-Limits the growth of
          territories. This is the
          default.RESTRICTED_AREA-Prevents the creation of territories.
      append_data {Boolean}:
          Specifies whether to append or replace the records to the barriers
          layer.APPEND-Appends records to an existing barrier
          layer.REPLACE-Creates a
          new barrier layer or replaces records in an existing
          barrier layer. This is the default.

        """