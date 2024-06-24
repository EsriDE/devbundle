# Generated documentation for module arcpy.locref


class CreateLRSFromExistingDataset(object):
    """
    Creates a linear referencing system (LRS) in the specified workspace using existing datasets.
    """

    @property
    def description(self) -> str:
        return """

        CreateLRSFromExistingDataset_locref(lrs_name, centerline_feature_class, centerline_centerline_id_field, centerline_sequence_table, centerline_sequence_centerline_id_field, centerline_sequence_route_id_field, centerline_sequence_from_date_field, centerline_sequence_to_date_field, centerline_sequence_network_id_field, calibration_point_feature_class, calibration_point_measure_field, calibration_point_from_date_field, calibration_point_to_date_field, calibration_point_route_id_field, calibration_point_network_id_field, redline_feature_class, redline_from_measure_field, redline_to_measure_field, redline_route_id_field, redline_route_name_field, redline_effective_date_field, redline_activity_type_field, redline_network_id_field)

        Creates a linear referencing system (LRS) in the specified workspace
        using existing datasets.

     INPUTS:
      lrs_name (String):
          The name of the LRS to create. The name cannot already exist in the
          geodatabase.
      centerline_feature_class (Feature Layer):
          The feature class to use as the centerline in the LRS.
      centerline_centerline_id_field (Field):
          The GUID field containing the centerline ID. The field type
          must match thefield type in the centerline sequence table.
          centerlineID
      centerline_sequence_table (Table View):
          The table to use as the centerline sequence in the LRS.
      centerline_sequence_centerline_id_field (Field):
          The GUID field containing the centerline sequence ID. The
          field type must match thefield type and length in the centerline
          feature class. centerlineID
      centerline_sequence_route_id_field (Field):
          The GUID or text field containing the centerline sequence
          route ID. The field type must match thefield type and length in the
          calibration point and redline feature classes. routeID
      centerline_sequence_from_date_field (Field):
          A date field containing the centerline sequence from date.
      centerline_sequence_to_date_field (Field):
          A date field containing the centerline sequence to date.
      centerline_sequence_network_id_field (Field):
          The field containing the centerline sequence network ID. The short
          integer field type is supported.
      calibration_point_feature_class (Feature Layer):
          The feature class to use as the calibration point in the LRS.
      calibration_point_measure_field (Field):
          The field containing the calibration point measure. The double field
          type is supported.
      calibration_point_from_date_field (Field):
          A date field containing the calibration point from date.
      calibration_point_to_date_field (Field):
          A date field containing the calibration point to date.
      calibration_point_route_id_field (Field):
          The field containing the calibration point route ID. GUID and
          text field types are supported. The field type must match thefield
          type and length in the centerline sequence table and the redline
          feature class. routeID
      calibration_point_network_id_field (Field):
          The field containing the calibration point network ID. The short
          integer field type is supported.
      redline_feature_class (Feature Layer):
          The feature class to use as the redline in the LRS.
      redline_from_measure_field (Field):
          The field containing the redline from measure. The double field type
          is supported.
      redline_to_measure_field (Field):
          The field containing the redline to measure. The double field type is
          supported.
      redline_route_id_field (Field):
          The field containing the redline route ID. GUID and text field
          types are supported. The field type must match thefield type and
          length in the calibration point feature class and centerline sequence
          table. routeID
      redline_route_name_field (Field):
          A text field containing the redline route name.
      redline_effective_date_field (Field):
          A date field containing the redline effective date.
      redline_activity_type_field (Field):
          The field containing the redline activity type. The short integer
          field type is supported.
      redline_network_id_field (Field):
          The field containing the redline network ID. The short integer field
          type is supported.

        """