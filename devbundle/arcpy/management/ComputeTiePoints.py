# Generated documentation for module arcpy.management


class ComputeTiePoints(object):
    """
    Computes the tie points between overlapped mosaic dataset items. The tie points can then be used to compute the block adjustments for the mosaic dataset.
    """

    @property
    def description(self) -> str:
        return """

        ComputeTiePoints_management(in_mosaic_dataset, out_control_points, {similarity}, {in_mask_dataset}, {out_image_features}, {density}, {distribution}, {location_accuracy}, {options;options...})

        Computes the tie points between overlapped mosaic dataset items. The
        tie points can then be used to compute the block adjustments for the
        mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The input mosaic dataset that will be used to create tie points.
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
      in_mask_dataset {Feature Layer}:
          A polygon feature class used to exclude areas that will not be
          included in the computation of control points. Thefield can
          control the inclusion or exclusion of areas. A
          value of 1 indicates that the areas defined by the polygons (inside)
          will be excluded from the computation. A value of 2 indicates the
          defined polygons (inside) will be included in the computation while
          areas outside of the polygons will be excluded. mask
      density {String}:
          Specifies the number of tie points to be created.LOW-The density of
          points will be low, creating the fewest number of
          tie points.MEDIUM-The density of points will be medium, creating a
          moderate
          number of points.HIGH-The density of points will be high, creating the
          highest number
          of points.
      distribution {String}:
          Specifies whether the points will have regular or random
          distribution.RANDOM-Points will be generated randomly. Randomly
          generated points
          are better for overlapping areas with irregular shapes.REGULAR-Points
          will be generated based on a fixed pattern. Points
          based on a fixed pattern use the point density to determine how
          frequently to create points.
      location_accuracy {String}:
          Specifies the keyword that describes the accuracy of the imagery.
          LOW-Images have a large shift and a large rotation (> 5
          degrees). The SIFT algorithm will be used in the point-
          matching computation. MEDIUM-Images have a medium shift and a
          small rotation (<5
          degrees). The Harris algorithm will be used in the point-
          matching computation. HIGH-Images have a small shift and a
          small rotation.
          The Harris algorithm will be used in the point-matching computation.
      options {Value Table}:
          Additional options for the adjustment engine. The options are only
          used by third-party adjustment engines.

     OUTPUTS:
      out_control_points (Feature Class):
          The output control point table. The table will contain the tie points
          created by this tool.
      out_image_features {Feature Class}:
          The output image feature points table. This will be saved as a polygon
          feature class. This output can be quite large.

        """