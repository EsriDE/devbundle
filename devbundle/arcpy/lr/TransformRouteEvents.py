# Generated documentation for module arcpy.lr


class TransformRouteEvents(object):
    """
    Transforms the measures of events from one route reference to another and writes them to a new event table.
    """

    @property
    def description(self) -> str:
        return """

        TransformRouteEvents_lr(in_table, in_event_properties, in_routes, route_id_field, target_routes, target_route_id_field, out_table, out_event_properties, cluster_tolerance, {in_fields})

        Transforms the measures of events from one route reference to another
        and writes them to a new event table.

     INPUTS:
      in_table (Table View):
          The input event table.
      in_event_properties (Route Measure Event Properties):
          The route location fields and the type of events in the input event
          table.Route identifier field-The field containing values that indicate
          the
          route on which each event is located. This field can be a numeric,
          text, or GUID field. Event type-The type of events in the
          input event table (POINT
          or LINE). POINT-Point events occur at a precise location along
          a route. Only a
          from-measure field must be specified.LINE-Line events define a portion
          of a route. Both from- and to-
          measure fields must be specified.From-measure field-A field containing
          measure values. This field must
          be numeric and is required when the event type is POINT or LINETo-
          measure field-A field containing measure values. This field must be
          numeric and is required when the event type is LINE.
      in_routes (Feature Layer):
          The input route features.
      route_id_field (Field):
          The field containing values that uniquely identify each input route.
          The field can be a numeric, text, or GUID field.
      target_routes (Feature Layer):
          The route features to which the input events will be transformed.
      target_route_id_field (Field):
          The field containing values that uniquely identify each target route.
          The field can be a numeric, text, or GUID field.
      out_event_properties (Route Measure Event Properties):
          The route location fields and the type of events that will be written
          to the output event table.Route identifier field-The field that will
          contain values that
          indicate the route on which each event is located. The field can be a
          numeric, text, or GUID field. Event type-The type of events
          the output event table will
          contain (POINT or LINE). POINT-Point events occur at a precise
          location along a route. Only a
          single measure field must be specified.LINE-Line events define a
          portion of a route. Both from- and to-
          measure fields must be specified.From-measure field-A field that will
          contain measure values. This
          field is required when the event type is POINT or LINE.To-measure
          field-A field that will contain measure values. This field
          is required when the event type is LINE.
      cluster_tolerance (Linear Unit):
          The maximum tolerated distance between the input events and the target
          routes.
      in_fields {Boolean}:
          Specifies whether the out_table parameter value will contain route
          location fields plus all the attributes from the input
          events.FIELDS-The out_table parameter value will contain route
          location
          fields plus all the attributes from the input events. This is the
          default. NO_FIELDS-The out_table parameter value will only
          contain
          route location fields plus thefield from the input events.
          ObjectID

     OUTPUTS:
      out_table (Table):
          The table that will be created.

        """