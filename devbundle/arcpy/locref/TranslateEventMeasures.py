# Generated documentation for module arcpy.locref


class TranslateEventMeasures(object):
    """
    Translates the measures (m-values) of a point or line event layer from one linear referencing method (LRM) to another.
    """

    @property
    def description(self) -> str:
        return """

        TranslateEventMeasures_locref(in_source_event, in_target_route_features, out_target_event, {in_concurrent_route_matching})

        Translates the measures (m-values) of a point or line event layer from
        one linear referencing method (LRM) to another.

     INPUTS:
      in_source_event (Feature Layer):
          The input event layer to be translated.
      in_target_route_features (Feature Layer):
          The target LRS Network against which the input events will be
          translated.
      in_concurrent_route_matching {String}:
          Specifies the method used to determine which route to translate the
          event against when concurrent routes exist in the target LRS Network.
          This parameter is only applied when the location of the event
          translation on the target LRS Network has concurrent routes (routes
          that share a location).ANY-The input event layer is translated against
          the first of two or
          more concurrent routes found in the target LRS Network.ROUTE_ID-The
          Route ID of the source event is compared to the Route IDs
          of concurrent routes in the target LRS Network. The source event will
          translate based on Route ID matches in the source event and target
          network. The Route IDs of the input event and target LRS Network must
          be an exact match for this method to correctly translate the event.
          The input event layer must also be a registered LRS event to use this
          method.ALL-The input event is translated against all the concurrent
          routes at
          that location in the target LRS Network.

     OUTPUTS:
      out_target_event (Feature Class):
          The output feature class that will contain the translated event
          features.

        """