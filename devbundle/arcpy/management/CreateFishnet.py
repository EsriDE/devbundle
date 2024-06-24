# Generated documentation for module arcpy.management


class CreateFishnet(object):
    """
    Creates a fishnet of rectangular cells. The output can be polyline or polygon features.
    """

    @property
    def description(self) -> str:
        return """

        CreateFishnet_management(out_feature_class, origin_coord, y_axis_coord, cell_width, cell_height, number_rows, number_columns, {corner_coord}, {labels}, {template}, {geometry_type})

        Creates a fishnet of rectangular cells. The output can be polyline or
        polygon features.

     INPUTS:
      origin_coord (Point):
          The starting pivot point of the fishnet.
      y_axis_coord (Point):
          The y-axis coordinate is used to orient the fishnet. The fishnet is
          rotated by the same angle as defined by the line connecting the origin
          and the y-axis coordinate.
      cell_width (Double):
          The width of each cell. To calculate the cell width using the
          number_rows parameter value, leave this parameter unspecified or set
          the value to zero; the width will be calculated when the tool is run.
      cell_height (Double):
          The height of each cell. To calculate the cell height using the
          number_columns parameter value, leave this parameter unspecified or
          set the value to zero; the height will be calculated when the tool is
          run.
      number_rows (Long):
          The number of rows the fishnet will have. To calculate the number of
          rows using the cell_width parameter value, leave this parameter
          unspecified or set the value to zero; the number of rows will be
          calculated when the tool is run.
      number_columns (Long):
          The number of columns the fishnet will have. To calculate the number
          of columns using the cell_height parameter value, leave this parameter
          unspecified or set the value to zero; the number of columns will be
          calculated when the tool is run.
      corner_coord {Point}:
          The opposite corner of the fishnet set by the origin_coord
          parameter.This parameter is disabled if the origin_coord,
          y_axis_coord,
          cell_width, cell_height, number_rows and number_columns parameters are
          specified.
      labels {Boolean}:
          Specifies whether a point feature class will be created containing
          label points at the center of each fishnet cell.LABELS-A point feature
          class will be created. This is the
          default.NO_LABELS-A point feature class will not be created.
      template {Extent}:
          The extent of the fishnet. The extent can be entered by specifying the
          coordinates or using a template dataset.MAXOF-The maximum extent of
          all inputs will be used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      geometry_type {String}:
          Specifies whether the output fishnet cells will be polyline or polygon
          features.POLYLINE-Output will be a polyline feature class. Each cell
          is defined
          by four line features.POLYGON-Output will be a polygon feature class.
          Each cell is defined
          by one polygon feature.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the fishnet of rectangular cells.

        """