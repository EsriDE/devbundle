# Generated documentation for module arcpy.locref


class ModifyNetworkCalibrationRules(object):
    """
    Modifies the network calibration rules for an LRS Network.
    """

    @property
    def description(self) -> str:
        return """

        ModifyNetworkCalibrationRules_locref(in_feature_class, {calibration_rule}, {calibration_offset}, {update_measure_cartorealign})

        Modifies the network calibration rules for an LRS Network.

     INPUTS:
      in_feature_class (Feature Layer):
          The input LRS Network feature class.
      calibration_rule {String}:
          Specifies the method that will be used to define calibration gap
          measures.AS_IS-The existing defined method in the network will be used
          while
          changing the calibration offset value.ADDING_EUCLIDEAN_DISTANCE-The
          Euclidean, or straight-line, distance
          will be calculated and added at each physical gap along an edited
          route.STEPPING_INCREMENT-A value will be defined that will adjust, or
          step,
          at each physical gap in the route. This is the
          default.ADDING_INCREMENT-A value will be defined and added to each
          measure of
          a route at each physical gap, in addition to the total length of the
          from and to measures of the route.
      calibration_offset {Double}:
          The value of theparameter'sormethod. The increment value must
          be numeric and can include decimals. Calibration RuleAdding
          IncrementStepping Increment
      update_measure_cartorealign {String}:
          Specifies whether or not to recalibrate route measures based on length
          changes in cartographic realignment.AS_IS-The existing defined method
          in the network will be used. This is
          the default.ENABLE-Enable recalibration of route measures based on
          length changes
          in cartographic realignment.DISABLE-Disable recalibration of route
          measures based on length
          changes in cartographic realignment.

        """