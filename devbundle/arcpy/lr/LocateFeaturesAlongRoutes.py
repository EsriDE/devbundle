# Generated documentation for module arcpy.lr


class LocateFeaturesAlongRoutes(object):
    """
    Computes the intersection of input features (point, line, or polygon) and route features and writes the route and measure information to a new event table.
    """

    @property
    def description(self) -> str:
        return """

        LocateFeaturesAlongRoutes_lr(in_features, in_routes, route_id_field, radius_or_tolerance, out_table, out_event_properties, {route_locations}, {distance_field}, {zero_length_events}, {in_fields}, {m_direction_offsetting})

        Computes the intersection of input features (point, line, or polygon)
        and route features and writes the route and measure information to a
        new event table.

     INPUTS:
      in_features (Feature Layer):
          The input point, line, or polygon features.
      in_routes (Feature Layer):
          The routes with which the in_features parameter value will intersect.
      route_id_field (Field):
          The field containing values that uniquely identify each route. The
          field can be a numeric, text, or GUID field.
      radius_or_tolerance (Linear Unit):
          If the in_features parameter value is points, the search radius will
          be a numeric value defining how far around each point a search will be
          done to find a target route.If the in_features parameter value is
          lines, the search tolerance will
          be a cluster tolerance, which is a numeric value representing the
          maximum tolerated distance between the input lines and the target
          routes.If the in_features parameter value is polygons, this parameter
          is
          ignored and no search radius will be used.
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
      route_locations {Boolean}:
          Specifies whether the closest route location or every route location
          within the search radius will be written to the out_table parameter
          value. When locating points along routes, more than one route may be
          within the search radius of any given point. This parameter is ignored
          when locating lines or polygons along routes.FIRST-Only the closest
          route location will be written to the out_table
          parameter value. This is the default.ALL-Every route location within
          the search radius will be written to
          the out_table parameter value.
      distance_field {Boolean}:
          Specifies whether afield will be added to the out_table
          parameter value. The values in this field are in the units of the
          specified search radius. This parameter is ignored when locating lines
          or polygons along routes. DISTANCEDISTANCE-A field containing
          the point-to-route distance will be added
          to the out_table parameter value. This is the default.NO_DISTANCE-A
          field containing the point-to-route distance will not be
          added to the out_table parameter value.
      zero_length_events {Boolean}:
          Specifies whether zero-length line events will be written to the
          output. When locating polygons along routes, events may be created
          where the from-measure is equal to the to-measure. This parameter is
          ignored when locating points or lines along routes.ZERO-Zero-length
          line events will be written to the out_table
          parameter value. This is the default.NO_ZERO-Zero-length line events
          will not be written to the out_table
          parameter value.
      in_fields {Boolean}:
          Specifies whether the out_table parameter value will contain route
          location fields and all the attributes from the in_features parameter
          value.FIELDS-The out_table parameter value will contain route location
          fields and all the attributes from the in_features parameter value.
          This is the default. NO_FIELDS-The out_table parameter value
          will only contain
          route location fields and thefield from the in_features parameter
          value. ObjectID
      m_direction_offsetting {Boolean}:
          Specifies whether the offset distance calculated will be based on the
          m-direction or the digitized direction. Distances are included in the
          out_table parameter value if the distance_field parameter is set to
          DISTANCE.M_DIRECTON-The distance values in the out_table parameter
          value will
          be calculated based on the m-direction of the route. Input features to
          the left of the m-direction of the route will be assigned a positive
          (+) offset, and features to the right of the m-direction will be
          assigned a negative (-) offset. This is the default.NO_M_DIRECTION-The
          distance values in the out_table parameter value
          will be calculated based on the digitized direction of the route.
          Input features to the left of the digitized direction of the route
          will be assigned a negative (-) offset, and features to the right of
          the digitized direction will be assigned a positive (+) offset.

     OUTPUTS:
      out_table (Table):
          The table that will be created. The output table can be a dBase (.dbf
          file) or a geodatabase table.

        """