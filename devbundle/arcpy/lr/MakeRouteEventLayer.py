# Generated documentation for module arcpy.lr


class MakeRouteEventLayer(object):
    """
    Creates a temporary feature layer using routes and route events.
    """

    @property
    def description(self) -> str:
        return """

        MakeRouteEventLayer_lr(in_routes, route_id_field, in_table, in_event_properties, out_layer, {offset_field}, {add_error_field}, {add_angle_field}, {angle_type}, {complement_angle}, {offset_direction}, {point_event_type})

        Creates a temporary feature layer using routes and route events.

     INPUTS:
      in_routes (Feature Layer):
          The route features on which events will be located.
      route_id_field (Field):
          The field containing values that uniquely identify each route. The
          field can be a numeric, text, or GUID field.
      in_table (Table View):
          The table whose rows will be located along routes.
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
      offset_field {Field}:
          The field containing the values that will be used to offset events
          from their underlying route. This field must be numeric.
      add_error_field {Boolean}:
          Specifies whether afield will be added to the temporary layer
          that is created. LOC_ERRORNO_ERROR_FIELD-A field to store
          locating errors will not be added.
          This is the default.ERROR_FIELD-A field to store locating errors will
          be added.
      add_angle_field {Boolean}:
          Specifies whether afield will be added to the temporary layer
          that is created. This parameter is only valid when the event type is
          point. LOC_ANGLENO_ANGLE_FIELD-A field to store locating angles
          will not be added.
          This is the default.ANGLE_FIELD-A field to store locating angles will
          be added.
      angle_type {String}:
          Specifies the type of locating angle that will be calculated. This
          parameter is only valid if add_angle_field = "ANGLE_FIELD".NORMAL-The
          normal (perpendicular) angle will be calculated. This is
          the default.TANGENT-The tangent angle will be calculated.
      complement_angle {Boolean}:
          Specifies whether the complement of the locating angle will be
          written. This parameter is only valid if add_angle_field =
          "ANGLE_FIELD".ANGLE-The complement of the angle will not be written.
          Only the
          calculated angle will be written. This is the default.COMPLEMENT-The
          complement of the angle will be written.
      offset_direction {Boolean}:
          Specifies the side on which the route events with a positive offset
          will be displayed. This parameter is only valid if an offset field has
          been specified.LEFT-Events with a positive offset will be displayed to
          the left of
          the route. The side of the route is determined by the measures and not
          necessarily the digitized direction. This is the default.RIGHT-Events
          with a positive offset will be displayed to the right of
          the route. The side of the route is determined by the digitized
          direction.
      point_event_type {Boolean}:
          Specifies whether point events will be treated as point features or
          multipoint features.POINT-Point events will be treated as point
          features. This is the
          default.MULTIPOINT-Point events will be treated as multipoint
          features.

     OUTPUTS:
      out_layer (Feature Layer):
          The layer that will be created. This layer is stored in memory, so a
          path is not necessary.

        """