# Generated documentation for module arcpy.rm


class MatchControlPoints(object):
    """
    Creates matching tie points for a given ground control point and initial tie point in one of the overlapping images.
    """

    @property
    def description(self) -> str:
        return """

        MatchControlPoints_rm(in_mosaic_dataset, in_control_points, out_control_points, {similarity})

        Creates matching tie points for a given ground control point and
        initial tie point in one of the overlapping images.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The mosaic dataset that contains the source imagery from which the tie
          points will be created.
      in_control_points (File / Feature Class / Feature Layer / String):
          The input control point set that contains a list of ground control
          point features and at least one initial tie point for each ground
          control point.
      similarity {String}:
          Specifies the similarity level that will be used for matching tie
          points.LOW-The similarity criteria for the two matching points will be
          low.
          This option will produce the most matching points, but some of the
          matches may have a higher level of error.MEDIUM-The similarity
          criteria for the matching points will be medium.HIGH-The similarity
          criteria for the matching points will be high.
          This option will produce the fewest matching points, but each match
          will have a lower level of error.

     OUTPUTS:
      out_control_points (Feature Class):
          The output control point features that contain ground control points.

        """