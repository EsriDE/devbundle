# Generated documentation for module arcpy.management


class FeatureCompare(object):
    """
    Compares two feature classes or layers and returns the comparison results.
    """

    @property
    def description(self) -> str:
        return """

        FeatureCompare_management(in_base_features, in_test_features, sort_field;sort_field..., {compare_type}, {ignore_options;ignore_options...}, {xy_tolerance}, {m_tolerance}, {z_tolerance}, {attribute_tolerances;attribute_tolerances...}, {omit_field;omit_field...}, {continue_compare}, {out_compare_file})

        Compares two feature classes or layers and returns the comparison
        results.

     INPUTS:
      in_base_features (Feature Layer):
          Theare compared with the.refers to data that you have declared
          valid. This base data has the correct geometry definitions, field
          definitions, and spatial reference. Input Base FeaturesInput
          Test FeaturesInput Base Features
      in_test_features (Feature Layer):
          Theare compared against the.refers to data that you have made
          changes to by editing or compiling new features. Input Test
          FeaturesInput Base FeaturesInput Test Features
      sort_field (Value Table):
          The field or fields used to sort records in theand the. The
          records are sorted in ascending order. Sorting by a common field in
          both theand theensures that you are comparing the same row from each
          input dataset. Input Base FeaturesInput Test FeaturesInput Base
          FeaturesInput Test Features
      compare_type {String}:
          The comparison type. The default is, which will compare all
          properties of the features being compared. AllALL-All
          properties of the feature classes will be compared. This is
          the default.GEOMETRY_ONLY-Only the geometries of the feature classes
          will be
          compared.ATTRIBUTES_ONLY-Only the attributes and their values will be
          compared.SCHEMA_ONLY-Only the schema of the feature classes will be
          compared.SPATIAL_REFERENCE_ONLY-Only the spatial references of the two
          feature
          classes will be compared.
      ignore_options {String}:
          These properties will not be compared.IGNORE_M-Do not compare measure
          properties.IGNORE_Z-Do not compare
          elevation properties.IGNORE_POINTID-Do not compare point ID
          properties.IGNORE_EXTENSION_PROPERTIES-Do not compare extension
          properties.IGNORE_SUBTYPES-Do not compare
          subtypes.IGNORE_RELATIONSHIPCLASSES-Do not compare relationship
          classes.IGNORE_REPRESENTATIONCLASSES-Do not compare representation
          classes.IGNORE_FIELDALIAS-Do not compare field aliases.
      xy_tolerance {Linear Unit}:
          The distance that determines the range in which features are
          considered equal. To minimize error, the value you choose for the
          compare tolerance should be as small as possible. By default, the
          compare tolerance is the XY tolerance of the input base features.
      m_tolerance {Double}:
          The measure tolerance is the minimum distance between measures before
          they are considered equal.
      z_tolerance {Double}:
          The Z Tolerance is the minimum distance between z coordinates before
          they are considered equal.
      attribute_tolerances {Value Table}:
          The numeric value that determines the range in which attribute values
          are considered equal. This only applies to numeric field types.
      omit_field {String}:
          The field or fields that will be omitted during comparison. The field
          definitions and the tabular values for these fields will be ignored.
      continue_compare {Boolean}:
          Indicates whether to compare all properties after encountering the
          first mismatch.NO_CONTINUE_COMPARE-Stops after encountering the first
          mismatch. This
          is the default.CONTINUE_COMPARE-Compares other properties after
          encountering the
          first mismatch.

     OUTPUTS:
      out_compare_file {File}:
          This file will contain all similarities and differences between the
          in_base_features and the in_test_features. This file is a comma-
          delimited text file that can be viewed and used as a table in ArcGIS.

        """