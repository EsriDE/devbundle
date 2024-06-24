# Generated documentation for module arcpy.management


class ComputeControlPoints(object):
    """
    Creates the control points between the mosaic dataset and the reference image. The control points can then be used in conjunction with tie points to compute the adjustments for the mosaic dataset.
    """

    @property
    def description(self) -> str:
        return """

        ComputeControlPoints_management(in_mosaic_dataset, in_reference_images, out_control_points, {similarity}, {out_image_feature_points}, {density}, {distribution}, {area_of_interest}, {location_accuracy})

        Creates the control points between the mosaic dataset and the
        reference image. The control points can then be used in conjunction
        with tie points to compute the adjustments for the mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The input mosaic dataset that will be used to create control points.
      in_reference_images (Raster Dataset / Image Service / Map Server / WMS Map / Raster Layer / Mosaic Layer / Internet Tiled Layer / Map Server Layer):
          The reference images that will be used to create control points for
          your mosaic dataset. If you have multiple images, create a mosaic
          dataset from the images and use the mosaic dataset as the reference.
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
      area_of_interest {Feature Layer}:
          Limit the area in which tie points are generated to only this polygon
          feature class.
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

     OUTPUTS:
      out_control_points (Feature Class):
          The output control point table. This table will contain the control
          points that were created.
      out_image_feature_points {Feature Class}:
          The output image feature points table. This will be saved as a polygon
          feature class. This output can be quite large.

        """