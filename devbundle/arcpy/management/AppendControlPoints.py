# Generated documentation for module arcpy.management


class AppendControlPoints(object):
    """
    Combines control points to an existing control point table.
    """

    @property
    def description(self) -> str:
        return """

        AppendControlPoints_management(in_master_control_points, in_input_control_points, {in_z_field}, {in_tag_field}, {in_dem}, {in_xy_accuracy}, {in_z_accuracy}, {Geoid}, {area_of_interest}, {append_option})

        Combines control points to an existing control point table.

     INPUTS:
      in_master_control_points (Feature Class / Feature Layer):
          The input control point table. This is usually the output from the
          Compute Tie Points tool.
      in_input_control_points (Feature Class / Feature Layer / File / String):
          A point feature class that stores control points. It could be the
          control point table created from the Compute Control Points tool, the
          Compute Tie Points tool, or a point feature class that has ground
          control points.
      in_z_field {Field}:
          The field that stores the control point z-values. If both
          theand theparameters are set, the Z value field is
          used. If neither thenor theparameter is set, the z-value is set to 0
          for all ground control points and check points. Z Value Field
          NameInput DEMZ Value Field NameInput DEM
      in_tag_field {Field}:
          A field in the input control point table that has a unique value. This
          field will be added to the target control point table, where the tag
          field can be used to bring in identifiers associated with ground
          control points.
      in_dem {Raster Layer / Mosaic Layer / Raster Dataset / Mosaic Dataset}:
          A DEM to use to obtain the z-value for the control points in the input
          control point table. If both theandparameters are set, the Z
          value field is used.
          If neither thenor theparameter is set, the z-value is set to 0 for all
          ground control points and check points. Z Value Field NameInput
          DEMZ Value Field NameInput DEM
      in_xy_accuracy {Double}:
          The input accuracy for the X and Y coordinates. The accuracy is in the
          same units as the in_input_control_points.This information should be
          provided by the data provider. If the
          accuracy information is not available, skip this optional parameter.
      in_z_accuracy {Double}:
          The input accuracy for the vertical coordinates. The accuracy is in
          the units of the in_input_control_points.This information should be
          provided by the data provider. If the
          accuracy information is not available, skip this optional parameter.
      Geoid {Boolean}:
          The geoid correction is required by rational polynomial coefficients
          (RPC) that reference ellipsoidal heights. Most elevation datasets are
          referenced to sea level orthometric heights, so this correction would
          be required in these cases to convert to ellipsoidal heights.NONE-No
          geoid correction is made. Use NONE only if your DEM is already
          expressed in ellipsoidal heights. This is the default.GEOID-A geoid
          correction will be made to convert orthometric heights
          to ellipsoidal heights (based on EGM96 geoid).
      area_of_interest {Envelope / Feature Layer / Feature Class}:
          Defines an area of interest extent by entering minimum and maximum x-
          and y-coordinates in the spatial reference of the input control point
          table.
      append_option {String}:
          Specifies how control points will be appended to the control point
          table.ALL-Add all points in the input control point table to the
          target
          control point table, including GCPs, check points, and all tie points.
          This is the default.GCP-Add only GCPs in the input point table to the
          target control point
          table. GCPSET-Add GCPs and tie points specifically associated
          with
          the GCPs to the target control point table. Use caution with
          this option-it is applicable only when the tie points
          in the input and target control point table have the same
          transformation. The tie points might not be in the desired positions
          if they were computed using a different adjustment process.

        """