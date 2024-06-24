# Generated documentation for module arcpy.locref


class CreateLRS(object):
    """
    Creates an ArcGIS Location Referencing linear referencing system (LRS) and minimum schema items in a specified workspace.
    """

    @property
    def description(self) -> str:
        return """

        CreateLRS_locref(in_workspace, lrs_name, centerline_feature_class_name, calibration_point_feature_class_name, redline_feature_class_name, centerline_sequence_table_name, spatial_reference, {xy_tolerance}, {z_tolerance}, {xy_resolution}, {z_resolution})

        Creates an ArcGIS Location Referencing linear referencing system (LRS)
        and minimum schema items in a specified workspace.

     INPUTS:
      in_workspace (Workspace / Feature Dataset):
          The file or multipurpose geodatabase where the LRS and minimum schema
          will be created.
      lrs_name (String):
          The name of the output LRS.
      centerline_feature_class_name (String):
          The name of the output centerline feature class.
      calibration_point_feature_class_name (String):
          The name of the output calibration point feature class.
      redline_feature_class_name (String):
          The name of the output redline feature class.
      centerline_sequence_table_name (String):
          The name of the output centerline sequence table.
      spatial_reference (Spatial Reference):
          The spatial reference for the output feature classes. When using a
          Python script, you can use the Well Known ID (WKID) for the spatial
          reference.
      xy_tolerance {Linear Unit}:
          The x,y-tolerance of the output feature classes.
      z_tolerance {Linear Unit}:
          The z-tolerance of the output feature classes.
      xy_resolution {Linear Unit}:
          The x,y-resolution of the output feature classes.
      z_resolution {Linear Unit}:
          The z-resolution of the output feature classes.

        """