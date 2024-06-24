# Generated documentation for module arcpy.locref


class CreateLRSEvent(object):
    """
    Creates line or point events for an existing LRS Network.
    """

    @property
    def description(self) -> str:
        return """

        CreateLRSEvent_locref(parent_network, event_name, geometry_type, event_id_field, route_id_field, from_date_field, to_date_field, loc_error_field, measure_field, {to_measure_field}, {event_spans_routes}, {to_route_id_field}, {store_route_name}, {route_name_field}, {to_route_name_field})

        Creates line or point events for an existing LRS Network.

     INPUTS:
      parent_network (Feature Layer):
          The network to which the event is registered.
      event_name (String):
          The event to be registered.
      geometry_type (String):
          The geometry type of the output event.POINT-The geometry type of the
          event is Point. This is the
          default.LINE-The geometry type of the event is Polyline.
      event_id_field (String):
          The event ID field available in the event feature class.
      route_id_field (String):
          Name of the route ID field if it is a point event that does not span
          routes, or from route ID field if the event_spans_routes parameter is
          set to SPANS_ROUTES.
      from_date_field (String):
          The from date field available in the event feature class.
      to_date_field (String):
          The to date field available in the event feature class.
      loc_error_field (String):
          The location error field available in the event feature class.
      measure_field (String):
          Name of the measure field if it is a point event or from measure field
          if it is a line event.
      to_measure_field {String}:
          Name of the to measure field. Required only for Line events.
      event_spans_routes {Boolean}:
          Specifies whether the event records spans routes.SPANS_ROUTES-The
          event records span routes.NO_SPANS_ROUTES-The event
          records do not span routes. This is the
          default.
      to_route_id_field {String}:
          Name of the to route ID field. Required only if the geometry_type
          parameter is set to LINE and the event_span_routes parameter is set to
          SPANS_ROUTES.
      store_route_name {Boolean}:
          Specifies whether the route name should be stored with the event
          records.STORE_ROUTE_NAME-Stores the route name with the event
          records.NO_STORE_ROUTE_NAME-Does not store the route name with the
          event
          records. This is the default.
      route_name_field {String}:
          The route name field if it is a point event that does not span routes,
          or the from route name field if it is a line event that spans routes.
          Required if STORE_ROUTE_NAME is set.
      to_route_name_field {String}:
          The to route name field for line events that span routes. Required if
          STORE_ROUTE_NAME is set.

        """