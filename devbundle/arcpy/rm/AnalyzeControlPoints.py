# Generated documentation for module arcpy.rm


class AnalyzeControlPoints(object):
    """
    Analyzes the control point coverage and identifies the areas that need additional control points to improve the block adjust result.
    """

    @property
    def description(self) -> str:
        return """

        AnalyzeControlPoints_rm(in_mosaic_dataset, in_control_points, out_coverage_table, {out_overlap_table}, {in_mask_dataset}, {minimum_area}, {maximum_level})

        Analyzes the control point coverage and identifies the areas that need
        additional control points to improve the block adjust result.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The input mosaic dataset against which to analyze the control points.
      in_control_points (Feature Layer):
          The input control point feature class.It is normally created from the
          Compute Tie Points or the Compute
          Control Points tool.
      in_mask_dataset {Feature Layer}:
          A polygon feature class used to exclude areas that you do not want in
          the analysis of the control points computation. Thefield can
          control the inclusion or exclusion of areas. A
          value of 1 indicates that the areas defined by the polygons (inside)
          will be excluded from the computation. A value of 2 indicates the
          defined polygons (inside) will be included in the computation while
          areas outside of the polygons will be excluded. mask
      minimum_area {Double}:
          Specify the minimum percent that the overlap area must be, in relation
          to the image. Areas that are lower than the specified percent
          threshold will be excluded from the analysis.Ensure that you do not
          have areas that are too small; otherwise, you
          will have small slivers being analyzed.
      maximum_level {Long}:
          The maximum number of images that can be overlapped when analyzing the
          control points. For example, if there are four images in your
          mosaic dataset,
          and a maximum overlap value of 3 was specified, then there are ten
          different combinations that will appear in the. If the four images
          were named i1, i2, i3, and i4, the ten combinations that would appear
          are [i1, i2, i3], [i1 i2 i4], [i1 i3 i4], [i2 i3 i4], [i1, i2], [i1,
          i3], [i1, i4], [i2, i3], [i2, i4], and [i3, i4]. Overlap Window

     OUTPUTS:
      out_coverage_table (Feature Class):
          A polygon feature class output that contains the control point
          coverage and the percentage of the area within the corresponding
          image.
      out_overlap_table {Feature Class}:
          A polygon feature class output that contains all the overlap areas
          between images.

        """