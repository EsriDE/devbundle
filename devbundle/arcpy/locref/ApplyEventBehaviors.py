# Generated documentation for module arcpy.locref


class ApplyEventBehaviors(object):
    """
    Updates the event locations for all event feature classes registered with the input network based on the route edit performed.
    """

    @property
    def description(self) -> str:
        return """

        ApplyEventBehaviors_locref(in_route_features)

        Updates the event locations for all event feature classes registered
        with the input network based on the route edit performed.

     INPUTS:
      in_route_features (Feature Layer):
          The LRS Network for which event locations will be updated. This must
          be a feature layer registered as a network with the LRS.

        """