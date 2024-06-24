# Generated documentation for module arcpy.management


class GeneratePointsAlongLines(object):
    """
    Creates point features along lines or polygons at fixed intervals or by percentage of a feature's length.
    """

    @property
    def description(self) -> str:
        return """

        GeneratePointsAlongLines_management(Input_Features, Output_Feature_Class, Point_Placement, {Distance}, {Percentage}, {Include_End_Points}, {Add_Chainage_Fields})

        Creates point features along lines or polygons at fixed intervals or
        by percentage of a feature's length.

     INPUTS:
      Input_Features (Feature Layer):
          The line or polygon features to be converted into points.
      Point_Placement (String):
          Specifies the method that will be used to create points.PERCENTAGE-The
          Percentage parameter value will be used to place points
          along the features by percentage.DISTANCE-The Distance parameter value
          will be used to place points at
          fixed distances along the features. This is the default.
      Distance {Linear Unit}:
          The interval from the beginning of the feature at which points will be
          placed.
      Percentage {Double}:
          The percentage from the beginning of the feature at which points will
          be placed. For example, if a percentage of 40 is used, points will be
          placed at 40 percent and 80 percent of the feature's distance.
      Include_End_Points {Boolean}:
          Specifies whether additional points will be included at the start
          point and end point of the feature.END_POINTS-Additional points will
          be included at the start point and
          end point of the feature.NO_END_POINTS-No additional points will be
          included at the start point
          and end point of the feature. This is the default.
      Add_Chainage_Fields {Boolean}:
          Specifies whether the accumulated distance and sequence fields will be
          added to the output. ADD_CHAINAGE-The accumulated distance ()
          and sequence ()
          fields will be added to the output. Distance values are added in the
          units of the Input_Features value's spatial reference.
          ORIG_LENORIG_SEQNO_CHAINAGE-The accumulated distance or sequence
          fields will not be
          added to the output. This is the default.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          The point feature class that will be created from the input features.

        """