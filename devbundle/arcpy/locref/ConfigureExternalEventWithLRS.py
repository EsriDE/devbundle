# Generated documentation for module arcpy.locref


class ConfigureExternalEventWithLRS(object):
    """
    Associates event data stored in an external system with an LRS.
    """

    @property
    def description(self) -> str:
        return """

        ConfigureExternalEventWithLRS_locref(in_event, parent_network, event_name, event_id_field, route_id_field, measure_field, {geometry_type}, {to_measure_field}, {from_date_field}, {to_date_field}, {event_spans_routes}, {to_route_id_field}, {store_route_name}, {route_name_field}, {to_route_name_field}, {calibrate_rule}, {retire_rule}, {extend_rule}, {reassign_rule}, {realign_rule}, {reverse_rule}, {carto_realign_rule})

        Associates event data stored in an external system with an LRS.

     INPUTS:
      in_event (Table View):
          The external event feature class or table that will be registered to
          an LRS.
      parent_network (Feature Layer):
          The LRS Network to which the event will be registered.
      event_name (String):
          The name of the external event or table that will be registered to the
          LRS.
      event_id_field (Field):
          The event ID field available in the event feature class or table.
      route_id_field (Field):
          The name of the route ID field if it is a point event or a line event
          that does not span routes, or the name of the from route ID field if
          the event spans routes. The field must be available in the external
          event table or feature class.
      measure_field (Field):
          The name of the measure field if it is a point event or the name of
          the from measure field if it is a line event.
      geometry_type {String}:
          Specifies the geometry type of the external event or table.POINT-The
          geometry type of the event will be point. This is the
          default.LINE-The geometry type of the event will be polyline.
      to_measure_field {Field}:
          The name of the to measure field. This field is only required for line
          events.
      from_date_field {Field}:
          The from date field in the event feature class or table.
      to_date_field {Field}:
          The to date field in the event feature class or table.
      event_spans_routes {String}:
          Specifies whether the event records will span routes.AS_IS-The
          property will not change. This is the
          default.NO_SPANS_ROUTES-The event records will not span routes. This
          is
          applicable to line events only.SPANS_ROUTES-The event records will
          span routes. This is applicable
          to line events only.
      to_route_id_field {Field}:
          The name of the to route ID field available in the event feature class
          or table.
      store_route_name {String}:
          Specifies whether the route name will be stored with the event
          records.AS_IS-The property will not change. This is the
          default.NO_STORE_ROUTE_NAME-The route name will not be stored with the
          event
          records.STORE_ROUTE_NAME-The route name will be stored with the event
          records.
      route_name_field {Field}:
          The route name field if it is a point event or line event that does
          not span routes, or the name of the from route name field if the event
          spans routes. The field must be available in the external event table
          or feature class.
      to_route_name_field {Field}:
          The to route name field for line events that span routes. This
          parameter is required if the store_route_name and event_spans_routes
          parameters are set.
      calibrate_rule {String}:
          Specifies the event behavior rule for the calibrate activity.STAY_PUT-
          The geographic location of the event will be preserved;
          measures may change. This is the default.RETIRE-Both measure and
          geographic location will be preserved; the
          event will be retired.MOVE-The measures of the event will be
          preserved; the geographic
          location may change.
      retire_rule {String}:
          Specifies the event behavior rule for the retire activity.STAY_PUT-
          The geographic location of the event will be preserved;
          measures may change. This is the default.RETIRE-Both measure and
          geographic location will be preserved; the
          event will be retired.MOVE-The measures of the event will be
          preserved; the geographic
          location may change.SNAP-The geographic location of the event will be
          preserved by
          snapping the event to a concurrent route; measures may change.
      extend_rule {String}:
          Specifies the event behavior rule for the extend activity.STAY_PUT-
          The geographic location of the event will be preserved;
          measures may change. This is the default.RETIRE-Both measure and
          geographic location will be preserved; the
          event will be retired.MOVE-The measures of the event will be
          preserved; the geographic
          location may change.COVER-The geometric location and measure of a line
          event will be
          modified to include a new or newly modified section.
      reassign_rule {String}:
          Specifies the event behavior rule for the reassign activity.STAY_PUT-
          The geographic location of the event will be preserved;
          measures may change. This is the default.RETIRE-Both measure and
          geographic location will be preserved; the
          event will be retired.MOVE-The measures of the event will be
          preserved; the geographic
          location may change.SNAP-The geographic location of the event will be
          preserved by
          snapping the event to a concurrent route; measures may change.
      realign_rule {String}:
          Specifies the event behavior rule for the realign activity.STAY_PUT-
          The geographic location of the event will be preserved;
          measures may change. This is the default.RETIRE-Both measure and
          geographic location will be preserved; the
          event will be retired.MOVE-The measures of the event will be
          preserved; the geographic
          location may change.SNAP-The geographic location of the event will be
          preserved by
          snapping the event to a concurrent route; measures may
          change.COVER-The geometric location and measure of a line event will
          be
          modified to include a new or newly modified section.
      reverse_rule {String}:
          Specifies the event behavior rule for the reverse activity.STAY_PUT-
          The geographic location of the event will be preserved;
          measures may change. This is the default.RETIRE-Both measure and
          geographic location will be preserved; the
          event will be retired.MOVE-The measures of the event will be
          preserved; the geographic
          location may change.
      carto_realign_rule {String}:
          Specifies the event behavior rule for the cartographic realign
          activity.HONOR_ROUTE_MEASURE-The measure of the event will be
          preserved or
          changed proportionally to the route's measure change. This is the
          default.

        """