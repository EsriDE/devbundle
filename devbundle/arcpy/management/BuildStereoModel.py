# Generated documentation for module arcpy.management


class BuildStereoModel(object):
    """
    Builds a stereo model of a mosaic dataset based on a user-provided stereo pair.
    """

    @property
    def description(self) -> str:
        return """

        BuildStereoModel_management(in_mosaic_dataset, {minimum_angle}, {maximum_angle}, {minimum_overlap}, {maximum_diff_OP}, {maximum_diff_GSD}, {group_by}, {same_flight})

        Builds a stereo model of a mosaic dataset based on a user-provided
        stereo pair.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The mosaic dataset on which the stereo model will be built.Running the
          Apply Block Adjustment tool on the input mosaic dataset
          first will help create a more accurate stereo model.
      minimum_angle {Double}:
          The value, in degrees, that defines the minimum angle the stereo pair
          must meet. The default is 10.
      maximum_angle {Double}:
          The value, in degrees, that defines the maximum angle the stereo pair
          must meet. The default is 90.
      minimum_overlap {Double}:
          The percentage of the overlapping area over the whole image. The
          default is 0.5.
      maximum_diff_OP {Double}:
          The maximum threshold for the Omega and Phi difference between the two
          image pairs. The Omega values and Phi values for the image pairs are
          compared. If the difference between either the two Omega or the two
          Phi values is above the threshold, the pairs will not be formatted as
          a stereo pair.
      maximum_diff_GSD {Double}:
          The threshold for the maximum GSD between two images in a pair. If the
          resolution ratio between the two images is greater than the threshold
          value, the pairs will not be built as a stereo pair. The default is 2.
      group_by {Field}:
          Builds the stereo model from raster items within the same group,
          defined by a mosaic dataset field such as RGB, Panchromatic, or
          Infrared.
      same_flight {Boolean}:
          Specifies how the stereo models will be selected.SAMEFLIGHT-Stereo
          pairs will be selected along the same flight
          line.NO_SAMEFLIGHT-Stereo pairs will be selected across flight
          lines.This parameter is not applicable to satellite-based sensors.

        """