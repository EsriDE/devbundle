# Generated documentation for module arcpy.lr


class CalibrateRoutes(object):
    """
    Recalculates route measures using points.
    """

    @property
    def description(self) -> str:
        return """

        CalibrateRoutes_lr(in_route_features, route_id_field, in_point_features, point_id_field, measure_field, out_feature_class, {calibrate_method}, {search_radius}, {interpolate_between}, {extrapolate_before}, {extrapolate_after}, {ignore_gaps}, {keep_all_routes}, {build_index})

        Recalculates route measures using points.

     INPUTS:
      in_route_features (Feature Layer):
          The route features that will be calibrated.
      route_id_field (Field):
          The field containing values that uniquely identify each route. The
          field can be a numeric, text, or GUID field.
      in_point_features (Feature Layer):
          The point features that will be used to calibrate the routes.
      point_id_field (Field):
          The field that identifies the route on which each calibration point is
          located. The values in this field match those in the route identifier
          field. This field can be a numeric, text, or GUID field.
      measure_field (Field):
          The field containing the measure value for each calibration point.
          This field must be numeric.
      calibrate_method {String}:
          Specifies how route measures will be recalculated.DISTANCE-Measures
          will be recalculated using the shortest path
          distance between the calibration points. This is the
          default.MEASURES-Measures will be recalculated using the pre-existing
          measure
          distance between the calibration points.
      search_radius {Linear Unit}:
          Limits how far a calibration point can be from a route by specifying
          the distance and its unit of measure. If the unit of measure is
          unknown, the units of the coordinate system of the route feature class
          will be used.
      interpolate_between {Boolean}:
          Specifies whether measure values will be interpolated between the
          calibration points.BETWEEN-Measure values will be interpolated between
          the calibration
          points. This is the default.NO_BETWEEN-Measure values will not be
          interpolated between the
          calibration points.
      extrapolate_before {Boolean}:
          Specifies whether measure values will be extrapolated before the
          calibration points.BEFORE-Measure values will be extrapolated before
          the calibration
          points. This is the default.NO_BEFORE-Measure values will not be
          extrapolated before the
          calibration points.
      extrapolate_after {Boolean}:
          Specifies whether measure values will be extrapolated after the
          calibration points.AFTER-Measure values will be extrapolated after the
          calibration
          points. This is the default.NO_AFTER-Measure values will not be
          extrapolated after the calibration
          points.
      ignore_gaps {Boolean}:
          Specifies whether spatial gaps will be ignored when recalculating the
          measures on disjointed routes.IGNORE-Spatial gaps will be ignored.
          Measure values will be continuous
          for disjointed routes. This is the default.NO_IGNORE-Spatial gaps will
          not be ignored. The measure values on
          disjointed routes will have gaps. The gap distance is calculated using
          the straight-line distance between the endpoints of the disjointed
          parts.
      keep_all_routes {Boolean}:
          Specifies whether route features that do not have calibration points
          will be included in the output feature class.KEEP-All route features
          will be included in the output feature class.
          This is the default.NO_KEEP-All route features will not necessarily be
          included in the
          output feature class. Features with no calibration points will be
          excluded.
      build_index {Boolean}:
          Specifies whether an attribute index will be created for the route
          identifier field that is written to the out_feature_class parameter
          value.INDEX-An attribute index will be created. This is the
          default.NO_INDEX-An attribute index will not be created.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be created. It can be a shapefile or a
          geodatabase feature class.

        """