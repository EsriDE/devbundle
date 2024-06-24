# Generated documentation for module arcpy.locref


class ModifyLRSEvent(object):
    """
    Modifies properties of a linear referencing system (LRS) event.
    """

    @property
    def description(self) -> str:
        return """

        ModifyLRSEvent_locref(in_feature_class, {event_id_field}, {route_id_field}, {from_date_field}, {to_date_field}, {loc_error_field}, {measure_field}, {to_measure_field}, {event_spans_routes}, {to_route_id_field}, {store_route_name}, {route_name_field}, {to_route_name_field})

        Modifies properties of a linear referencing system (LRS) event.

     INPUTS:
      in_feature_class (Feature Layer):
          The input feature class or feature layer for the event.
      event_id_field {Field}:
          Name of the event ID field.
      route_id_field {Field}:
          Name of the route ID field.
      from_date_field {Field}:
          Name of the from date field.
      to_date_field {Field}:
          Name of the to date field.
      loc_error_field {Field}:
          Name of the location error field.
      measure_field {Field}:
          Name of the measure field if it is a point event or from measure field
          if it is a line event.
      to_measure_field {Field}:
          Name of the to measure field. Required only for line events.
      event_spans_routes {String}:
          Determines if the event records will span routes.AS_IS-No change to
          the property. This is the
          default.NO_SPANS_ROUTES-The event records do not span routes.
          Applicable only
          for line events.SPANS_ROUTES-The event records may span routes.
          Applicable only for
          line events.
      to_route_id_field {Field}:
          Name of the to route ID field. Required only if it is a line event and
          it spans routes.
      store_route_name {String}:
          Determines if the event records will store the route name.AS_IS-No
          change to the property. This is the
          default.STORE_ROUTE_NAME-Stores the route name with the event
          records.NO_STORE_ROUTE_NAME-Does not store the route name with the
          event
          records.
      route_name_field {Field}:
          The route name field if it is a point event that does not span routes,
          or the from route name field if it is a line event that spans routes.
          Required if STORE_ROUTE_NAME is set.
      to_route_name_field {Field}:
          Name of the to route name field. Required if it is a line event, and
          store_route_name and SPANS_ROUTES are set.

        """