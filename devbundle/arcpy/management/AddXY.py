# Generated documentation for module arcpy.management


class AddXY(object):
    """
    Adds the fields POINT_X and POINT_Y to the point input features and calculates their values. It also appends the POINT_Z and POINT_M fields if the input features are Z- and M-enabled.
    """

    @property
    def description(self) -> str:
        return """

        AddXY_management(in_features)

        Adds the fields POINT_X and POINT_Y to the point input features and
        calculates their values. It also appends the POINT_Z and POINT_M
        fields if the input features are Z- and M-enabled.

     INPUTS:
      in_features (Feature Layer):
          The point features whose x,y coordinates will be appended
          asandfields. POINT_XPOINT_Y

        """