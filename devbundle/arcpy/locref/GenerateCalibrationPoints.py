# Generated documentation for module arcpy.locref


class GenerateCalibrationPoints(object):
    """
    Generates calibration points for any route shape provided, including complex shapes such as self-closing, self-intersecting, and branched routes.
    """

    @property
    def description(self) -> str:
        return """

        GenerateCalibrationPoints_locref(in_polyline_features, route_id_field, from_date_field, to_date_field, in_calibration_point_feature_class, lrs_network, {calibration_direction}, {calibration_method}, {from_measure_field}, {to_measure_field})

        Generates calibration points for any route shape provided, including
        complex shapes such as self-closing, self-intersecting, and branched
        routes.

     INPUTS:
      in_polyline_features (Feature Layer):
          The features that will be used as the source to calculate the measure
          values for calibration points.
      route_id_field (Field):
          The field containing values that uniquely identify each route.
          The field type must match thefield in the calibration point feature
          class. Route ID
      from_date_field (Field):
          The field containing the from date values of a route.
      to_date_field (Field):
          The field containing the to date values of a route.
      in_calibration_point_feature_class (Feature Layer):
          The existing calibration point feature class to which new features
          will be added.
      lrs_network (String):
          The LRS Network for which the measure values will be generated in the
          calibration points feature class.
      calibration_direction {String}:
          Specifies the direction of increasing calibration on a route when
          creating calibration points.DIGITIZED_DIRECTION-The direction of
          digitization of the individual
          polyline features determines the direction of calibration for the
          route. This is the default. MEASURE_DIRECTION-The direction of
          increasing m-values of the
          individual polyline feature determines the direction of calibration
          for the route. If the individual polyline feature does not
          include m-values, the
          digitized direction will be used.
      calibration_method {String}:
          Specifies the method that will be used to determine the measures on a
          route when creating calibration points.GEOMETRY_LENGTH-The geometrical
          length of the input route feature will
          be used as the calibration method. This is the default.M_ON_ROUTE-The
          measure values on the input route feature will be used
          as the calibration method.ATTRIBUTE_FIELDS-The measure values stored
          in attribute fields of the
          input route feature will be used as the calibration method.
      from_measure_field {Field}:
          The field containing the from measure for the selected route.This
          parameter is enabled when the calibration_method parameter is set
          to ATTRIBUTE_FIELDS.
      to_measure_field {Field}:
          The field containing the to measure for the selected route.This
          parameter is enabled when the calibration_method parameter is set
          to ATTRIBUTE_FIELDS.

        """