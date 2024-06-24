# Generated documentation for module arcpy.locref


class ModifyLRS(object):
    """
    Modifies an existing linear referencing system (LRS) in the specified workspace.
    """

    @property
    def description(self) -> str:
        return """

        ModifyLRS_locref(in_workspace, current_lrs_name, {new_lrs_name}, {centerline_feature_class}, {centerline_centerline_id_field}, {centerline_sequence_table}, {centerline_sequence_centerline_id_field}, {centerline_sequence_route_id_field}, {centerline_sequence_from_date_field}, {centerline_sequence_to_date_field}, {centerline_sequence_network_id_field}, {calibration_point_feature_class}, {calibration_point_measure_field}, {calibration_point_from_date_field}, {calibration_point_to_date_field}, {calibration_point_route_id_field}, {calibration_point_network_id_field}, {redline_feature_class}, {redline_from_measure_field}, {redline_to_measure_field}, {redline_route_id_field}, {redline_route_name_field}, {redline_effective_date_field}, {redline_activity_type_field}, {redline_network_id_field}, {conflict_prevention}, {move_to_feature_dataset})

        Modifies an existing linear referencing system (LRS) in the specified
        workspace.

     INPUTS:
      in_workspace (Workspace):
          The LRS workspace.
      current_lrs_name (String):
          The name of the current LRS.
      new_lrs_name {String}:
          The new name of the current LRS.
      centerline_feature_class {Feature Layer}:
          An existing centerline feature class for the minimum schema.
      centerline_centerline_id_field {Field}:
          The name of the centerline ID field from the centerline_feature_class
          parameter value.
      centerline_sequence_table {Table View}:
          An existing centerline sequence table for the minimum schema.
      centerline_sequence_centerline_id_field {Field}:
          The name of the centerline ID field from the centerline_sequence_table
          parameter value.
      centerline_sequence_route_id_field {Field}:
          The name of the route ID field from the centerline_sequence_table
          parameter value.
      centerline_sequence_from_date_field {Field}:
          The name of the from date field from the centerline_sequence_table
          parameter value.
      centerline_sequence_to_date_field {Field}:
          The name of the to date field from the centerline_sequence_table
          parameter value.
      centerline_sequence_network_id_field {Field}:
          The name of the network ID field from the centerline_sequence_table
          parameter value.
      calibration_point_feature_class {Feature Layer}:
          An existing calibration point feature class for the minimum schema.
      calibration_point_measure_field {Field}:
          The name of the measure field from the calibration_point_feature_class
          parameter value.
      calibration_point_from_date_field {Field}:
          The name of the from date field from the
          calibration_point_feature_class parameter value.
      calibration_point_to_date_field {Field}:
          The name of the to date field from the calibration_point_feature_class
          parameter value.
      calibration_point_route_id_field {Field}:
          The name of the route ID field from the
          calibration_point_feature_class parameter value.
      calibration_point_network_id_field {Field}:
          The name of the network ID field from the
          calibration_point_feature_class parameter value.
      redline_feature_class {Feature Layer}:
          An existing redline feature class for the minimum schema.
      redline_from_measure_field {Field}:
          The name of the from measure field from the redline_feature_class
          parameter value.
      redline_to_measure_field {Field}:
          The name of the to measure field from the redline_feature_class
          parameter value.
      redline_route_id_field {Field}:
          The name of the route ID field from the redline_feature_class
          parameter value.
      redline_route_name_field {Field}:
          The name of the route name field from the redline_feature_class
          parameter value.
      redline_effective_date_field {Field}:
          The name of the effective date field from the redline_feature_class
          parameter value.
      redline_activity_type_field {Field}:
          The name of the activity type field from the redline_feature_class
          parameter value.
      redline_network_id_field {Field}:
          The name of the network ID field from the redline_feature_class
          parameter value.
      conflict_prevention {String}:
          Specifies whether conflict prevention will be enabled for the input
          LRS. Conflict prevention is only available when editing or performing
          geoprocessing on branch versioned data that is published as a feature
          service.AS_IS-The current conflict prevention setting will be used.
          This is
          the default.ENABLE-Conflict prevention will be enabled for the input
          LRS.DISABLE-Conflict prevention will be disabled for the input LRS.
      move_to_feature_dataset {Boolean}:
          Specifies whether feature classes will be moved to the required LRS
          feature dataset.DO_NOT_MOVE-Feature classes will not be moved to the
          required LRS
          feature dataset. This is the default.MOVE-Feature classes will be
          moved to the required LRS feature
          dataset.

        """