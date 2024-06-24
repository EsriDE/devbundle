# Generated documentation for module arcpy.topographic


class FillGaps(object):
    """
    Fills gaps between polygon features that participate in a topology where the coincident boundaries are evident.
    """

    @property
    def description(self) -> str:
        return """

        FillGaps_topographic(input_features;input_features..., max_gap_area, {fill_option}, {fill_unenclosed_gaps}, {max_gap_distance})

        Fills gaps between polygon features that participate in a topology
        where the coincident boundaries are evident.

     INPUTS:
      input_features (Feature Layer):
          A list of input polygon feature classes or layers to be analyzed for
          gaps.
      max_gap_area (Areal Unit):
          The maximum area that can be considered a gap. Areas larger than this
          threshold are not filled.
      fill_option {String}:
          Specifies how enclosed and unenclosed gaps are
          filled.FILL_BY_LENGTH-Gaps are filled by adding a gap's geometry to
          the
          polygon with the longest shared edge. This is the
          default.FILL_BY_ORDER-Gaps are filled sequentially according to the
          order of
          the input polygon features list.
      fill_unenclosed_gaps {Boolean}:
          Specifies whether the tool fills unenclosed
          gaps.SKIP_UNENCLOSED_GAPS-Only enclosed gaps are filled. Unenclosed
          gap are
          skipped. This is the default.FILL_ALL-Both enclosed and unenclosed
          gaps are filled.
      max_gap_distance {Linear Unit}:
          The maximum distance between features in which a gap can be filled.
          This parameter is used only when the fill_unenclosed_gaps parameter is
          set to FILL_ALL.

        """