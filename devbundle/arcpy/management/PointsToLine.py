# Generated documentation for module arcpy.management


class PointsToLine(object):
    """
    Creates line features from points.
    """

    @property
    def description(self) -> str:
        return """

        PointsToLine_management(Input_Features, Output_Feature_Class, {Line_Field}, {Sort_Field}, {Close_Line}, {Line_Construction_Method}, {Attribute_Source}, {Transfer_Fields;Transfer_Fields...})

        Creates line features from points.

     INPUTS:
      Input_Features (Feature Layer):
          The point features that will be used to construct lines.
      Line_Field {Field}:
          The field that will be used to identify unique attribute values so
          line features can be constructed using points of the same values.If no
          field is specified, lines will be constructed without using
          unique attribute values. This is the default.
      Sort_Field {Field}:
          The field that will be used to sort the order of the points.If no
          field is specified, points used to create output line features
          will be sorted in the order they are found. This is the default.
      Close_Line {Boolean}:
          Specifies whether the output line features will be closed.CLOSE-For a
          continuous line, an extra segment connecting the last
          point with the first point will be included to form a closed line. For
          two-point lines, an extra line feature connecting the last point with
          the first point will be included to form a closed shape.NO_CLOSE-No
          extra segment or line will be created to ensure a closed
          line or closed shape. This is the default.
      Line_Construction_Method {String}:
          Specifies the method that will be used to construct the line
          features.CONTINUOUS-Line features will be created by connecting points
          continuously. This is the default.TWO_POINT-Line features will be
          created by connecting two consecutive
          points.
      Attribute_Source {String}:
          Specifies how the specified attributes will be transferred.NONE-No
          attributes will be transferred. This is the
          default.BOTH_ENDS-The attributes from the start and end points of the
          line
          will be transferred.START-The attributes from the start point of the
          line will be
          transferred.END-The attributes from the end point of the line will be
          transferred.
      Transfer_Fields {Field}:
          The fields containing values that will be transferred from the source
          points to the output lines. If no fields are selected, no attributes
          will be transferred.If the Attribute_Source parameter value is
          specified as NONE, this
          parameter will be disabled.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          The line feature class that will be created from the input points.

        """