# Generated documentation for module arcpy.management


class BuildLasDatasetPyramid(object):
    """
    Constructs or updates a LAS dataset display cache, which optimizes its rendering performance.
    """

    @property
    def description(self) -> str:
        return """

        BuildLasDatasetPyramid_management(in_las_dataset, {point_selection_method}, {class_codes_weights;class_codes_weights...})

        Constructs or updates a LAS dataset display cache, which optimizes its
        rendering performance.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The input LAS dataset.It is only possible to construct a LAS dataset
          pyramid if the LAS
          dataset has an .lasd extension. The pyramid construction process does
          not support individual .las or .zlas files.
      point_selection_method {String}:
          Specifies how the point in each binned region will be selected to
          construct the pyramid. This parameter is disabled if the LAS dataset
          contains a pyramid.Z_MIN-The point with the lowest z-value will be
          selected.Z_MAX-The
          point with the highest z-value will be selected.CLOSEST_TO_CENTER-The
          point that is closest to the center of the
          binned region will be selected.CLASS_CODE-The point with the highest
          weight value will be selected.
      class_codes_weights {Value Table}:
          The weights assigned to each class code that determine which
          points are retained in each thinning region. This parameter is only
          enabled when theoption is specified in theparameter. The class code
          with the highest weight will be retained in the thinning region. If
          two class codes with the same weight exist in a given thinning region,
          the class code with the smallest point source ID will be retained.
          Class Code WeightsPoint Selection Method

        """