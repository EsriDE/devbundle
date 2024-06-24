# Generated documentation for module arcpy.management


class TINCompare(object):
    """
    Compares two TINs and returns the comparison results.
    """

    @property
    def description(self) -> str:
        return """

        TINCompare_management(in_base_tin, in_test_tin, {compare_type}, {continue_compare}, {out_compare_file})

        Compares two TINs and returns the comparison results.

     INPUTS:
      in_base_tin (TIN Layer):
          The Input Base Tin is compared with the Input Test Tin. Input Base Tin
          refers to data that you have declared valid. This base data has the
          correct geometry, tag values (if any), and spatial reference.
      in_test_tin (TIN Layer):
          The Input Test Tin is compared against the Input Base Tin.
      compare_type {String}:
          The comparison type.ALL-This is the default.PROPERTIES_ONLY-Refers to
          both geometry and
          TIN tag values, if any,
          that are assigned to nodes and
          triangles.SPATIAL_REFERENCE_ONLY-Coordinate system information.
      continue_compare {Boolean}:
          Indicates whether to compare all properties after encountering the
          first mismatch.NO_CONTINUE_COMPARE-Stop after encountering the first
          mismatch. This
          is the default.CONTINUE_COMPARE-Compare other properties after
          encountering the first
          mismatch.

     OUTPUTS:
      out_compare_file {File}:
          The name and path of the text file which will contain the comparison
          results.

        """