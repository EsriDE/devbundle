# Generated documentation for module arcpy.lr


class OverlayRouteEvents(object):
    """
    Overlays two event tables to create an output event table that represents the union or intersection of the input.
    """

    @property
    def description(self) -> str:
        return """

        OverlayRouteEvents_lr(in_table, in_event_properties, overlay_table, overlay_event_properties, overlay_type, out_table, out_event_properties, {zero_length_events}, {in_fields}, {build_index})

        Overlays two event tables to create an output event table that
        represents the union or intersection of the input.

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
      overlay_table (Table View):
          The overlay event table.
      overlay_event_properties (Route Measure Event Properties):
          The route location fields and the type of events in the overlay event
          table.Route identifier field-The field containing values that indicate
          which
          route each event is along. This field can be a numeric, text, or GUID
          field.Event type-The type of events in the overlay event table (POINT
          or
          LINE).POINT-Point events occur at a precise location along a route.
          Only a
          from-measure field must be specified.LINE-Line events define a portion
          of a route. Both from- and to-
          measure fields must be specified.From-measure field-A field containing
          measure values. This field must
          be numeric and is required when the event type is POINT or LINE.To-
          measure field-A field containing measure values. This field must be
          numeric and is required when the event type is LINE.
      overlay_type (String):
          Specifies the type of overlay that will be performed.INTERSECT-Only
          overlapping events will be written to the output event
          table. This is the default.UNION-All events will be written to the
          output table. Linear events
          will be split at their intersections.
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
      zero_length_events {Boolean}:
          Specifies whether zero-length line events will be added to the
          out_table parameter value. This parameter is only valid when the
          output event type is LINE.ZERO-Zero-length line events will be added.
          This is the
          default.NO_ZERO-Zero-length line events will not be added.
      in_fields {Boolean}:
          Specifies whether all the fields from the input and overlay event
          tables will be included in the out_table parameter value.FIELDS-All
          the fields from the input tables will be included in the
          output table. This is the default. NO_FIELDS-All the fields
          from the input tables will not be
          included in the output table. Only thefield and the route location
          fields will be included. ObjectID
      build_index {Boolean}:
          Specifies whether an attribute index will be created for the route
          identifier field that is written to the out_table parameter
          value.INDEX-An attribute index will be created. This is the
          default.NO_INDEX-An attribute index will not be created.

     OUTPUTS:
      out_table (Table):
          The table that will be created.

        """