# Generated documentation for module arcpy.locref


class RemoveLRSEntity(object):
    """
    Removes a linear referencing system (LRS) entity from an input geodatabase workspace.
    """

    @property
    def description(self) -> str:
        return """

        RemoveLRSEntity_locref(in_workspace, lrs_entity_type, lrs_entity_name)

        Removes a linear referencing system (LRS) entity from an input
        geodatabase workspace.

     INPUTS:
      in_workspace (Workspace):
          The input geodatabase workspace that contains the LRS entity that will
          be removed.
      lrs_entity_type (String):
          Specifies the type of LRS entity that will be removed from the input
          geodatabase workspace.LRS-An LRS and its dependent LRS Networks, as
          well as the LRS events,
          and LRS intersections registered to those LRS Networks, will be
          removed.NETWORK-An LRS Network and the LRS events and LRS
          intersections
          registered to that LRS Network will be removed.EVENT-An LRS event will
          be removed.INTERSECTION-An LRS intersection will be
          removed.UN_FEATURE_CLASS-A utility network feature class will be
          removed.ADDRESS_FEATURE_CLASS-Address management feature classes will
          be
          removed.
      lrs_entity_name (String):
          The name of the LRS entity that will be removed from the input
          geodatabase workspace. The underlying feature classes and tables of
          the LRS entity will not be deleted.

        """