# Generated documentation for module arcpy.locref


class CreateLRSEventFromExistingDataset(object):
    """
    Registers an existing feature class as an LRS event.
    """

    @property
    def description(self) -> str:
        return """

        CreateLRSEventFromExistingDataset_locref(parent_network, in_feature_class, event_id_field, route_id_field, from_date_field, to_date_field, loc_error_field, measure_field, {to_measure_field}, {event_spans_routes}, {to_route_id_field}, {store_route_name}, {route_name_field}, {to_route_name_field})

        Registers an existing feature class as an LRS event.

     INPUTS:
      parent_network (Feature Layer):
          The network to which the event will be registered.
      in_feature_class (Feature Layer):
          The event to be registered.
      event_id_field (Field):
          The event ID field in the event feature class.
      route_id_field (Field):
          The route ID field if the feature class is a point event or the from
          route ID field if the feature class is a line event and
          event_spans_routes is set to SPANS_ROUTES.
      from_date_field (Field):
          The from date field in the event feature class.
      to_date_field (Field):
          The to date field in the event feature class.
      loc_error_field (Field):
          The location error field in the event feature class.
      measure_field (Field):
          The measure field if the feature class is a point event or the from
          measure field if the feature class is a line event.
      to_measure_field {Field}:
          The to measure field in the event feature class. This parameter is
          required for line events.
      event_spans_routes {Boolean}:
          Specifies whether the event records will span
          routes.NO_SPANS_ROUTES-The event records will not span routes. This is
          the
          default.SPANS_ROUTES-The event records will span routes.
      to_route_id_field {Field}:
          The to route ID field for events that span routes. This parameter is
          required if the in_feature class parameter geometry type is polyline
          and event_spans_routes is set to SPANS_ROUTES.
      store_route_name {Boolean}:
          Specifies whether the route name will be stored with the event
          records.NO_STORE_ROUTE_NAME-The route name will not be stored with
          the event
          records. This is the default.STORE_ROUTE_NAME-The route name will be
          stored with the event records.
      route_name_field {Field}:
          The route name field if the feature class is a point event that
          doesn't span routes or the from route name field if the feature class
          is a line event that spans routes. This parameter is required if
          store_route_name is set to STORE_ROUTE_NAME.
      to_route_name_field {Field}:
          The to route name field for line events that span routes. This
          parameter is required if store_route_name is set to STORE_ROUTE_NAME.

        """