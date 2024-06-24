# Generated documentation for module arcpy.locref


class AppendRoutes(object):
    """
    Appends routes from an input polyline into an LRS Network.
    """

    @property
    def description(self) -> str:
        return """

        AppendRoutes_locref(source_routes, in_lrs_network, route_id_field, {route_name_field}, {from_date_field}, {to_date_field}, {line_id_field}, {line_name_field}, {line_order_field}, {field_map}, {load_type}, {load_field}, {consider_existing_centerlines})

        Appends routes from an input polyline into an LRS Network.

     INPUTS:
      source_routes (Feature Layer):
          The input from which the routes will be derived. The input can be a
          polyline feature class, shapefile, feature service, or LRS Network
          feature class.
      in_lrs_network (Feature Layer):
          The target LRS Network where the routes will be loaded.
      route_id_field (Field):
          The field in the input polyline feature class that will be
          mapped to the LRS Network route ID. The field type must match thefield
          type of the target LRS Network and must be either a string or GUID
          field type. If it is a string field, the field length must be shorter
          than or equal to the length of the targetfield. RouteIDRouteID
      route_name_field {Field}:
          The field in the input polyline feature class that will be mapped as
          the LRS Network route name. The field must be a string field, and the
          field length must be shorter than or equal to the length of the target
          route name field.
      from_date_field {Field}:
          A date field in the input polyline feature class that will be mapped
          as the from_date_field value in the LRS Network. If the field is not
          mapped, a null value representing the beginning of time will be
          provided for all appended routes.
      to_date_field {Field}:
          A date field in the input polyline feature class that will be mapped
          as the to_date_field value in the LRS Network. If the field is not
          mapped, a null value representing the end of time will be provided for
          all appended routes.
      line_id_field {Field}:
          The field in the input polyline feature class that will be
          mapped as the LRS Network line ID. This parameter is only used if the
          target LRS Network is an LRS line network. The field type and length
          must match thefield type and length of the centerline sequence table.
          RouteID
      line_name_field {Field}:
          The string field in the input polyline feature class that will be
          mapped as the LRS Network line name. This parameter is only used if
          the target LRS Network is an LRS line network.
      line_order_field {Field}:
          The long integer field in the input polyline feature class that will
          be mapped as the LRS Network line order. This parameter is only used
          if the target LRS Network is an LRS line network.Learn more about line
          networks and line order in Pipeline Referencing
          or line networks and line order in Roads and Highways.
      field_map {Field Mappings}:
          Controls how attribute information in the source route fields will be
          transferred to the input LRS Network. Fields cannot be added to or
          removed from the target LRS Network because the data of the source
          routes is appended to an existing LRS Network that has a predefined
          schema (field definitions). While you can set merge rules for each
          output field, the tool will ignore them. The ArcPy FieldMappings class
          can be used to define this parameter.
      load_type {String}:
          Specifies how appended routes with measure or temporality overlaps
          with identical route IDs will be loaded into the network feature
          class.ADD-The appended routes will be loaded into the target LRS
          Network. If
          any route ID in the source routes already exists in the target LRS
          Network with the same temporality, it will be written to the output
          log as a duplicate route and must be corrected or filtered out before
          completing the loading process. This is the
          default.RETIRE_BY_ROUTE_ID-The appended routes will be loaded into the
          target
          LRS Network and any routes in the target LRS Network that have the
          same route ID and temporality overlap as the appended routes will be
          retired. If the appended route eclipses a target route with the same
          route ID, the target route will be deleted.REPLACE_BY_ROUTE_ID-The
          appended routes will be loaded into the target
          LRS Network and any routes in the target LRS Network with the same
          route ID as the appended routes will be deleted.
      load_field {String}:
          Specifies the field that will be used for loading routes.
          ROUTE_ID-The routes will be loaded using thefield. This is
          the default. RouteID         ROUTE_NAME-The routes will be
          loaded using thefield. This
          option is only available for the networks with RouteName configured in
          the LRS Network when the load_type parameter is set to ADD.
          RouteName
      consider_existing_centerlines {Boolean}:
          Specifies whether routes will be appended using existing
          centerlines.CONSIDER-Routes will be appended using existing
          centerlines and no new
          centerlines will be created.DO_NOT_CONSIDER-New centerlines will be
          created for the appended
          routes. This is the default.

        """