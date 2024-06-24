# Generated documentation for module arcpy.lr


class DissolveRouteEvents(object):
    """
    Removes redundant information from event tables or separates event tables having more than one descriptive attribute into individual tables.
    """

    @property
    def description(self) -> str:
        return """

        DissolveRouteEvents_lr(in_events, in_event_properties, dissolve_field;dissolve_field..., out_table, out_event_properties, {dissolve_type}, {build_index})

        Removes redundant information from event tables or separates event
        tables having more than one descriptive attribute into individual
        tables.

     INPUTS:
      in_events (Table View):
          The table with the rows that will be aggregated.
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
      dissolve_field (Field):
          The fields that will be used to aggregate rows.
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
      dissolve_type {Boolean}:
          Specifies how the input events will be aggregated.DISSOLVE-Events will
          be aggregated wherever there is measure overlap.
          This is the default.CONCATENATE-Events will be aggregated where the
          to-measure of one
          event matches the from-measure of the next event. This option is
          applicable only for line events.
      build_index {Boolean}:
          Specifies whether an attribute index will be created for the route
          identifier field that is written to the output event table.INDEX-An
          attribute index will be created. This is the
          default.NO_INDEX-An attribute index will not be created.

     OUTPUTS:
      out_table (Table):
          The table that will be created.

        """