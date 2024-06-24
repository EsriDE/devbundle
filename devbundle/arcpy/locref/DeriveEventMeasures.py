# Generated documentation for module arcpy.locref


class DeriveEventMeasures(object):
    """
    Populates and updates the DerivedRouteID field and measure values on point and line events with those fields configured and enabled.
    """

    @property
    def description(self) -> str:
        return """

        DeriveEventMeasures_locref(in_route_features, {update_all_events}, {event_layers;event_layers...})

        Populates and updates the DerivedRouteID field and measure values on
        point and line events with those fields configured and enabled.

     INPUTS:
      in_route_features (Feature Layer):
          The LRS Network containing the events withand measure fields
          configured. DerivedRouteID
      update_all_events {Boolean}:
          Specifies whether all event feature classes in the network will be
          updated.UPDATE_ALL-All event feature classes in the network selected
          in the
          in_route_features parameter value will be updated. This is the
          default.UPDATE_SOME-All event feature classes in the network selected
          in the
          in_route_features parameter value will not be updated. Individual
          event layers can be selected using the event_layers parameter.
      event_layers {Feature Layer}:
          The event layers that will haveand measure fields updated.
          DerivedRouteID

        """