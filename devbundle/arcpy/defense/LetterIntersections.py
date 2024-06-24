# Generated documentation for module arcpy.defense


class LetterIntersections(object):
    """
    Identifies intersections in a line feature class and adds sequential letters to output point features.
    """

    @property
    def description(self) -> str:
        return """

        LetterIntersections_defense(in_features, out_feature_class, field_to_letter, {in_area}, {spatial_sort_method}, {lettering_format}, {starting_letter}, {omit_letters;omit_letters...}, {min_out_point_distance}, {center_point}, {add_distance_and_bearing})

        Identifies intersections in a line feature class and adds sequential
        letters to output point features.

     INPUTS:
      in_features (Feature Set):
          The input line features with intersections that will be lettered.
      field_to_letter (Field):
          The name of the field that will contain the letter designator for each
          intersection.
      in_area {Feature Set}:
          The area that will limit the intersections identified; only
          intersections within this area will be identified and lettered.
      spatial_sort_method {String}:
          Specifies how features will be spatially sorted for the purpose of
          lettering. Features are not reordered in the table.UR-Features will be
          sorted starting at the upper right corner. This is
          the default.UL-Features will be sorted starting at the upper left
          corner.LR-Features will be sorted starting at the lower right
          corner.LL-Features will be sorted starting at the lower left
          corner.PEANO-Features will be sorted using a space-filling curve
          algorithm,
          also known as a Peano curve.CENTER-Features will be sorted starting
          from a center point (the mean
          center will be used if no center is provided).CLOCKWISE-Features will
          be sorted starting from a center point and
          moving clockwise.COUNTERCLOCKWISE-Features will be sorted starting
          from a center point
          and moving counterclockwise.NONE-No spatial sort will be used. The
          same order as the feature class
          will be used.
      lettering_format {String}:
          Specifies the labeling format that will be used for each
          feature.A_B_C-An alpha character (for example, A, B, C) will be used.
          This is
          the default.AA_AB_AC-A constant alpha character with an incrementing
          second alpha
          character grid (for example, AA, AB, AC) will be used.AA_BB_CC-A
          double alpha character that is incremented for each feature
          (for example, AA, BB, CC) will be used.
      starting_letter {String}:
          The value that will be used to begin lettering.
      omit_letters {String}:
          The values that will be omitted from the lettering sequence.
      min_out_point_distance {Linear Unit}:
          The minimum distance between intersections that are identified for
          lettering.
      center_point {Feature Set}:
          The center point that will be used to sort and letter features.
      add_distance_and_bearing {Boolean}:
          Specifies whether fields will be added to the output for distance and
          bearing to a center point.DONT_ADD_DISTANCE-No distance or bearing
          fields will be added to the
          output. This is the default. ADD_DISTANCE-andfields will be
          added to the output.
          DIST_TO_CENTERANGLE_TO_CENTER

     OUTPUTS:
      out_feature_class (Feature Class):
          The output point feature class.

        """