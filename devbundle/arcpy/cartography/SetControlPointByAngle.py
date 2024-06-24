# Generated documentation for module arcpy.cartography


class SetControlPointByAngle(object):
    """
    Places a control point at vertices along a line or polygon outline where the angle created by a change in line direction is less than or equal to a specified maximum angle.
    """

    @property
    def description(self) -> str:
        return """

        SetControlPointByAngle_cartography(in_features, maximum_angle)

        Places a control point at vertices along a line or polygon outline
        where the angle created by a change in line direction is less than or
        equal to a specified maximum angle.

     INPUTS:
      in_features (Feature Layer):
          The feature layer containing line or polygon features.
      maximum_angle (Double):
          The angle used to determine whether a vertex along a line or polygon
          outline will be set as a control point. The angle value must be
          greater than zero and less than 180 decimal degrees.

        """