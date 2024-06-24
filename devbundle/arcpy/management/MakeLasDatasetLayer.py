# Generated documentation for module arcpy.management


class MakeLasDatasetLayer(object):
    """
    Creates a LAS dataset layer that can apply filters to LAS points and control the enforcement of surface constraint features.
    """

    @property
    def description(self) -> str:
        return """

        MakeLasDatasetLayer_management(in_las_dataset, out_layer, {class_code;class_code...}, {return_values;return_values...}, {no_flag}, {synthetic}, {keypoint}, {withheld}, {surface_constraints;surface_constraints...}, {overlap})

        Creates a LAS dataset layer that can apply filters to LAS points and
        control the enforcement of surface constraint features.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset that will be processed.
      class_code {String}:
          Specifies the classification codes that will be used to filter LAS
          points. All class codes will be selected by default.0-Never processed
          by a classification method1-Processed by a
          classification method but could not be determined2-Bare earth
          measurements3-Vegetation whose height is considered to be low for the
          area4-Vegetation whose height is considered to be intermediate for the
          area5-Vegetation whose height is considered to be high for the
          area6-Structure with roof and walls7-Erroneous or undesirable data
          that is closer to the ground8-Reserved for later use, but used for
          model key points in LAS 1.1 -
          1.39-Water10-Railway tracks used by trains11-Road surfaces12-Reserved
          for later use, but used for overlap points in LAS 1.1 -
          1.313-Shielding around electrical wires14-Power lines15-A lattice
          tower used to support an overhead power line16-A mechanical assembly
          that joins an electrical circuit17-The surface of a bridge18-Erroneous
          or undesirable data that is far from the ground19 - 63-Reserved class
          codes for ASPRS designation64 - 255-User-definable class codes
      return_values {String}:
          Specifies the ordinal pulse return values that will be used to filter
          LAS points. All returns will be used when no value is specified.
          Return information is only available for LAS point clouds collected
          from a lidar scanner. The return number reflects the order of discrete
          points obtained from the lidar pulse, whereby the first return is
          closest to the scanner and the last return is farthest from the
          scanner.LAST-The last point from all lidar pulses will be
          used.FIRST_OF_MANY-The first point from each lidar pulse with multiple
          returns will be used.LAST_OF_MANY-The last point from each lidar pulse
          with multiple
          returns will be used.SINGLE-All points from lidar pulses with only one
          return will be used.1-All points with a return value of 1 will be
          used.2-All points with a return value of 2 will be used.3-All points
          with a return value of 3 will be used.4-All points with a return value
          of 4 will be used.5-All points with a return value of 5 will be
          used.6-All points with a return value of 6 will be used.7-All points
          with a return value of 7 will be used.8-All points with a return value
          of 8 will be used.9-All points with a return value of 9 will be
          used.10-All points with a return value of 10 will be used.11-All
          points with a return value of 11 will be used.12-All points with a
          return value of 12 will be used.13-All points with a return value of
          13 will be used.14-All points with a return value of 14 will be
          used.15-All points with a return value of 15 will be used.
      no_flag {Boolean}:
          Specifies whether data points that do not have classification flags
          assigned will be included for display and
          analysis.INCLUDE_UNFLAGGED-Unflagged points will be included. This is
          the
          default.EXCLUDE_UNFLAGGED-Unflagged points will be excluded.
      synthetic {Boolean}:
          Specifies whether data points flagged as synthetic will be included.
          Synthetic points refer to LAS points that originated from a data
          source other than a lidar scanner.INCLUDE_SYNTHETIC-Synthetic points
          will be included. This is the
          default.EXCLUDE_SYNTHETIC-Synthetic points will be excluded.
      keypoint {Boolean}:
          Specifies whether data points flagged as model key points will be
          included. Model key points refer to LAS points that are significant
          for modeling the object they are associated
          with.INCLUDE_KEYPOINT-Model key points will be included. This is the
          default.EXCLUDE_KEYPOINT-Model key points will be excluded.
      withheld {Boolean}:
          Specifies whether data points flagged as withheld will be included.
          Withheld points represent erroneous or undesired measurements captured
          in the LAS points.INCLUDE_WITHHELD-Withheld points will be
          included.EXCLUDE_WITHHELD-Withheld points will be excluded. This is
          the
          default.
      surface_constraints {String}:
          The name of the surface constraint features that will be enabled in
          the layer. All constraints are enabled by default.
      overlap {Boolean}:
          Specifies whether data points flagged as overlap will be included.
          Overlap points refer to points collected in overlapping scans that
          typically have a larger scan angle. Filtering overlap points can help
          ensure a regular distribution of LAS points is achieved across the
          extent of the data.INCLUDE_OVERLAP-Overlap points will be included.
          This is the
          default.EXCLUDE_OVERLAP-Overlap points will be excluded.

     OUTPUTS:
      out_layer (LAS Dataset Layer):
          The name of the resulting LAS dataset layer. A backslash or forward
          slash can be used to denote a group layer.

        """