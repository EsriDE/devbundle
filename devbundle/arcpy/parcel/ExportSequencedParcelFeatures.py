# Generated documentation for module arcpy.parcel


class ExportSequencedParcelFeatures(object):
    """
    Exports the parcel features of a selected parcel to individual feature classes. The individual feature classes can be added to a map to create parcel layouts or title map layouts. Fields are added to the feature classes so that parcel features can be labeled and tabulated in a clockwise sequence.
    """

    @property
    def description(self) -> str:
        return """

        ExportSequencedParcelFeatures_parcel(in_parcel_polygon_feature, target_feature_dataset, {start_sequence_corner}, {points_sequence_format}, {lines_sequence_format}, {sequence_curves_separately})

        Exports the parcel features of a selected parcel to individual feature
        classes. The individual feature classes can be added to a map to
        create parcel layouts or title map layouts. Fields are added to the
        feature classes so that parcel features can be labeled and tabulated
        in a clockwise sequence.

     INPUTS:
      in_parcel_polygon_feature (Feature Layer):
          The parcel that will be exported to individual feature classes. Only
          one parcel polygon can be selected.
      target_feature_dataset (Feature Dataset):
          The feature dataset where the exported parcel feature classes will
          reside.
      start_sequence_corner {String}:
          Specifies the parcel corner where the line and point sequence
          numbering will start. The sequence number is populated in thefield on
          the exported lines and points feature class. SequenceNE-The
          line or point sequence will start at the northeast parcel
          corner point. This is the default.SE-The line or point sequence will
          start at the southeast parcel
          corner point.SW-The line or point sequence will start at the southwest
          parcel
          corner point.NW-The line or point sequence will start at the northwest
          parcel
          corner point.
      points_sequence_format {String}:
          The sequence numbering format that will be used for points in
          thefield. Use a # character to denote the incrementing sequence
          number. Multiple # characters will add zeros before the sequence
          number. Letters can be placed on either side of the # character. The
          following are examples:        Sequence# is formatted as a sequence
          starting with 1.## is formatted as a
          sequence starting with 01.P# is formatted as a sequence starting with
          P1.ABC-##1 is formatted as a sequence starting with ABC-001.#P is
          formatted as a sequence starting with 1P.
      lines_sequence_format {String}:
          The sequence numbering format that will be used for lines in
          thefield. Use a # character to denote the incrementing sequence
          number. Multiple # characters will add zeros before the sequence
          number. Letters can be placed on either side of the # character. The
          following are examples:        Sequence# is formatted as a sequence
          starting with 1.## is formatted as a
          sequence starting with 01.L# is formatted as a sequence starting with
          L1.ABC-##1 is formatted as a sequence starting with ABC-001.#L is
          formatted as a sequence starting with 1L.
      sequence_curves_separately {Boolean}:
          Specifies whether curves will be sequenced separately when exporting
          parcel lines. SEQUENCE_SEPARATELY-The sequence numbering in
          thefield will
          restart at 1 for the first curve encountered in the clockwise sequence
          and will increment for each additional curve found. Sequence
          SEQUENCE_TOGETHER-The sequence numbering in thefield will not
          be incremented separately for curved lines. This is the default.
          Sequence

        """