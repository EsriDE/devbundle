# Generated documentation for module arcpy.management


class TableCompare(object):
    """
    Compares two tables or table views and returns the comparison results.
    """

    @property
    def description(self) -> str:
        return """

        TableCompare_management(in_base_table, in_test_table, sort_field;sort_field..., {compare_type}, {ignore_options;ignore_options...}, {attribute_tolerances;attribute_tolerances...}, {omit_field;omit_field...}, {continue_compare}, {out_compare_file})

        Compares two tables or table views and returns the comparison results.

     INPUTS:
      in_base_table (Table View / Raster Layer):
          Theis compared with the. Therefers to tabular data that you
          have declared valid. The base data has the correct field definitions
          and attribute values. Input Base TableInput Test TableInput
          Base Table
      in_test_table (Table View / Raster Layer):
          Theis compared against the. Therefers to data that you have
          made changes to by editing or compiling new fields, new records, or
          new attribute values. Input Test TableInput Base TableInput
          Test Table
      sort_field (Value Table):
          The field or fields used to sort records in theand the. The
          records are sorted in ascending order. Sorting by a common field in
          both theand theensures that you are comparing the same row from each
          input dataset. Input Base TableInput Test TableInput Base
          TableInput Test Table
      compare_type {String}:
          The comparison type. ALL is the default. The default will compare all
          properties of the tables being compared.ALL-Compare all properties.
          This is the default.ATTRIBUTES_ONLY-Only
          compare the attributes and their values.SCHEMA_ONLY-Only compare the
          schema.
      ignore_options {String}:
          These properties will not be compared.IGNORE_EXTENSION_PROPERTIES-Do
          not compare extension
          properties.IGNORE_SUBTYPES-Do not compare
          subtypes.IGNORE_RELATIONSHIPCLASSES-Do not compare relationship
          classes.IGNORE_FIELDALIAS-Do not compare field aliases.
      attribute_tolerances {Value Table}:
          The numeric value that determines the range in which attribute values
          are considered equal. This only applies to numeric field types.
      omit_field {String}:
          The field or fields that will be omitted during comparison. The field
          definitions and the tabular values for these fields will be ignored.
      continue_compare {Boolean}:
          Indicates whether to compare all properties after encountering the
          first mismatch.NO_CONTINUE_COMPARE-Stop after encountering the first
          mismatch. This
          is the default.CONTINUE_COMPARE-Compare other properties after
          encountering the first
          mismatch.

     OUTPUTS:
      out_compare_file {File}:
          This file will contain all similarities and differences between the
          in_base_table and the in_test_table. This file is a comma-delimited
          text file that can be viewed and used as a table in ArcGIS.

        """