# Generated documentation for module arcpy.topographic


class MergeLinesByPseudoNode(object):
    """
    Dissolves features where pseudo nodes occur.
    """

    @property
    def description(self) -> str:
        return """

        MergeLinesByPseudoNode_topographic(input_features, {merge_fields;merge_fields...}, {aggregate_operations;aggregate_operations...}, {merge_feature_rule})

        Dissolves features where pseudo nodes occur.

     INPUTS:
      input_features (Feature Layer):
          The line features from which pseudo nodes will be removed.
      merge_fields {Field}:
          The field or fields on which features will be merged.
      aggregate_operations {Value Table}:
          Specifies the fields that will be used to calculate the specified
          statistic. Multiple statistic and field combinations can be specified.
          Null values are excluded from all statistical calculations.Text
          attribute fields can be summarized using first and last
          statistics. Numeric attribute fields can be summarized using any
          statistic.Available statistic types are as follows:SUM-The total value
          for the specified field will be
          calculated.MEAN-The average for the specified field will be
          calculated.MIN-The smallest value for all records of the specified
          field will be
          found.MAX-The largest value for all records of the specified field
          will be
          found.RANGE-The range of values (maximum minus minimum) for the
          specified
          field will be calculated.STD-The standard deviation of values in the
          specified field will be
          calculated.COUNT-The number of values included in statistical
          calculations will
          be found. Each value will be counted except null values. To determine
          the number of null values in a field, create a count on the field in
          question, create a count on a different field that does not contain
          null values (for example, the OID if present), and subtract the two
          values.FIRST-The value of the first record in the input will be
          used.LAST-The value of the last record in the input will be
          used.MEDIAN-The median for all records of the specified field will be
          calculated.VARIANCE-The variance for all records of the specified
          field will be
          calculated.UNIQUE-The number of unique values of the specified field
          will be
          counted.
      merge_feature_rule {String}:
          Specifies which feature's attributes will be maintained when two
          features are merged at a pseudo node.FIRST-The feature with the lowest
          ObjectID and its attributes will be
          maintained while merging. The value for the fields with a specified
          aggregation operation will be updated with the calculated
          value.LAST-The feature with the highest ObjectID and its attributes
          will be
          maintained while merging. The value for the fields with a specified
          aggregation operation will be updated with the calculated
          value.BY_LENGTH-The feature with the longest length and its attributes
          will
          be maintained while merging. The value for the fields with a specified
          aggregation operation will be updated with the calculated
          value.USE_DEFAULTS-The feature with the lowest ObjectID will be
          maintained
          while merging. The value for the fields with a specified aggregation
          operation will be updated with the calculated value. The value for
          fields that are not merge fields or calculated with an aggregation
          operation will have the value assigned with the default value from the
          field or subtype when applicable.

        """