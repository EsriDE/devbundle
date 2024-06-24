# Generated documentation for module arcpy.locref


class CreateLRSNetwork(object):
    """
    Creates an LRS Network in an ArcGIS Location Referencing linear referencing system (LRS).
    """

    @property
    def description(self) -> str:
        return """

        CreateLRSNetwork_locref(in_path, lrs_name, network_name, route_id_field, route_name_field, from_date_field, to_date_field, {derive_from_line_network}, {line_network_name}, {include_fields_to_support_lines}, {line_id_field}, {line_name_field}, {line_order_field}, {measure_unit})

        Creates an LRS Network in an ArcGIS Location Referencing linear
        referencing system (LRS).

     INPUTS:
      in_path (Workspace / Feature Dataset):
          The input workspace that will contain the new LRS Network. This
          workspace must be a geodatabase that contains a Location Referencing
          LRS. In addition to the top level of a geodatabase, a feature dataset
          is also supported as a valid path.
      lrs_name (String):
          The LRS to which the new LRS Network will be registered. The LRS must
          reside in the same geodatabase as the in_path parameter value.
      network_name (String):
          The name of the LRS Network that will be created, as well as the name
          of the feature class that will be created and registered with the LRS
          Network. The LRS Network name must be 26 or fewer characters and
          cannot contain special characters other than underscores.
      route_id_field (String):
          The field in the output feature class that will be mapped as
          the LRS Network route ID. The field type is derived from thefield of
          the centerline sequence table and must be either string or GUID type.
          RouteId
      route_name_field (String):
          A string field in the output feature class that will be mapped as the
          LRS Network route name.
      from_date_field (String):
          A date field in the output feature class that will be mapped as the
          LRS Network from date.
      to_date_field (String):
          A date field in the output feature class that will be mapped as the
          LRS Network to date.
      derive_from_line_network {Boolean}:
          Specifies whether the network will be configured as an LRS derived
          network.DERIVE-The output will be an LRS derived network and a feature
          class
          to support the LRS derived network. The line_network_name parameter
          value must also be provided.DO_NOT_DERIVE-The output will not be an
          LRS derived network. This is
          the default.
      line_network_name {String}:
          The name of the LRS line network to which the output LRS derived
          network will be registered. The input LRS line network must reside in
          the same geodatabase workspace as the line_network_name value. This
          parameter is only used if the derive_from_line_network parameter is
          set to DERIVE.
      include_fields_to_support_lines {Boolean}:
          Specifies whether fields that support lines will be added.INCLUDE-The
          output will be an LRS line network, and the output feature
          class will include fields that support lines. The line_id_field,
          line_name_field, and line_order_field parameter values must also be
          provided.DO_NOT_INCLUDE-The output will not be an LRS line network.
          This is the
          default.
      line_id_field {String}:
          The field in the output feature class that will be mapped as
          the LRS Network line ID. This parameter is only used if the
          include_fields_to_support_lines parameter is set to INCLUDE. The field
          type is derived from thefield of the centerline sequence table and
          will either be a string of exactly 38 characters or a GUID field type.
          RouteId
      line_name_field {String}:
          A string field in the output feature class that will be mapped as the
          LRS Network line name. This parameter is only used if the
          include_fields_to_support_lines parameter is set to INCLUDE.
      line_order_field {String}:
          The field in the output feature class that will be mapped as the LRS
          Network line order. This parameter is only used if the
          include_fields_to_support_lines parameter is set to INCLUDE. This will
          be a long integer field type.
      measure_unit {String}:
          Specifies the unit of measure (m-unit) the LRS Network will
          use.MILES-The unit of measure will be miles. This is the
          default.INCHES-The unit of measure will be inches.FEET-The unit of
          measure will be feet.YARDS-The unit of measure will be
          yards.NAUTICAL_MILES-The unit of measure will be nautical
          miles.INTFEET-The unit of measure will be international
          feet.MILLIMETERS-The unit of measure will be
          millimeters.CENTIMETERS-The unit of measure will be
          centimetersMETERS-The unit of measure will be meters.KILOMETERS-The
          unit of measure will be kilometers.DECIMETERS-The unit of measure will
          be decimeters.

        """