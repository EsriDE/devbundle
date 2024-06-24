# Generated documentation for module arcpy.cartography


class MergeDividedRoads(object):
    """
    Generates single-line road features in place of matched pairs of divided road lanes.
    """

    @property
    def description(self) -> str:
        return """

        MergeDividedRoads_cartography(in_features, merge_field, merge_distance, out_features, {out_displacement_features}, {character_field}, {out_table})

        Generates single-line road features in place of matched pairs of
        divided road lanes.

     INPUTS:
      in_features (Feature Layer):
          The input linear road features that contain matched pairs of divided
          road lanes that will be merged into a single output line feature.
      merge_field (Field):
          The field that contains road classification information. Only
          parallel, proximate roads of equal classification will be merged. A
          value of 0 (zero) locks a feature to prevent it from participating in
          merging. The data type must be short or long integer.
      merge_distance (Linear Unit):
          The minimum distance apart, in the specified units, for equal-class,
          relatively parallel road features to be merged. This distance must be
          greater than zero. If the units are in points, millimeters,
          centimeters, or inches, the value is considered in page units and
          takes into account the reference scale.
      character_field {Field}:
          A short or long integer field that indicate the character of road
          segments, independent of their road classification. The tool uses
          these values to refine the assessment of candidate feature pairs for
          merging. Use this parameter in unusual or complex road networks to
          improve the quality of the output. If there are null values (or if
          this parameter is not specified), the road character (and merge
          candidacy) is based only on the shapes and arrangement of features.
          Use value 999 to lock features from participating in a merge.
          Field values are assessed as follows:        0-Traffic circles
          or roundabouts1-Carriageways, boulevards, dual-lane
          highways, or other parallel
          trending roads2-On- or off-ramps, highway intersection
          connectors999-Features will not be merged

     OUTPUTS:
      out_features (Feature Class):
          The output feature class containing single-line merged road features
          and all unmerged road features.
      out_displacement_features {Feature Class}:
          The output polygon features containing the degree and direction of
          road displacement.
      out_table {Table}:
          A many-to-many relationship table that links the merged road
          features to their source features. This table contains two fields,and,
          which store the merged feature IDs and their source feature IDs,
          respectively. Use this table to derive necessary attributes for the
          output features from their source features. No table is created when
          this parameter is left blank. OUTPUT_FIDINPUT_FID

        """