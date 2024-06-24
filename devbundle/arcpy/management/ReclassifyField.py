# Generated documentation for module arcpy.management


class ReclassifyField(object):
    """
    Reclassifies values in a numerical or text field into classes based on bounds defined manually or using a reclassification method.
    """

    @property
    def description(self) -> str:
        return """

        ReclassifyField_management(in_table, field, {method}, {classes}, {interval}, {standard_deviations}, {reclass_table;reclass_table...}, {reverse_values}, {output_field_name})

        Reclassifies values in a numerical or text field into classes based on
        bounds defined manually or using a reclassification method.

     INPUTS:
      in_table (Table View / Raster Layer / Mosaic Layer):
          The input table or feature class containing the field that will be
          reclassified.
      field (Field):
          The field that will be reclassified. The field must be numeric or
          text.
      method {String}:
          Specifies the reclassification method that will be used for the field
          values in the field parameter value.DEFINED_INTERVAL-Classes will be
          created with the same class range
          over the span of the values of the field to
          reclassify.EQUAL_INTERVAL-Classes will be created with equal class
          ranges divided
          into a specified number of classes. This is the
          default.GEOMETRIC_INTERVAL-Classes will be created with geometrically
          increasing or decreasing class ranges into a specified number of
          classes.MANUAL-Class breaks and reclassed values will be manually
          specified.NATURAL_BREAKS-Classes will be created of natural groupings
          in the
          data using the Jenks natural breaks algorithm.QUANTILE-Classes will
          be created in which each class includes an
          equal number of values.STANDARD_DEVIATION-Classes will be created by
          adding and subtracting
          a fraction of the standard deviation above and below the average
          value.UNIQUE_VALUES-Classes will be created in which each unique value
          of
          the field becomes a class.
      classes {Long}:
          The target number of classes in the reclassified field. The maximum
          number of classes is 256.
      interval {Double}:
          The class interval size for the reclassified field. The provided value
          must result in at least 3 classes and not more than 1,000 classes.
      standard_deviations {String}:
          Specifies the number of standard deviations that will be used for the
          reclassified field. Class breaks and categories will be created with
          equal interval ranges that are a proportion of the standard deviation
          from the mean.ONE-Intervals will be created using one standard
          deviation. This is
          the default.HALF-Intervals will be created using half of one standard
          deviation.THIRD-Intervals will be created using a third of one
          standard
          deviation.QUARTER-Intervals will be created using a quarter of one
          standard
          deviation.
      reclass_table {Value Table}:
          The upper bound and reclassed value for the manual reclassification
          method.
      reverse_values {Boolean}:
          Specifies the order of the reclassified values.DESC-Classes will be
          assigned values in descending order; the class
          with the highest values is assigned 1, the next highest class is
          assigned 2, and so on.ASC-Classes will be assigned values in ascending
          order; the class with
          the lowest values is assigned 1, the next lowest class is assigned 2,
          and so on. This is the default.
      output_field_name {String}:
          The name or prefix of the output field. If the field to reclassify is
          a numerical field, two fields will be created, and this name will
          prefix the field names. If the field to reclassify is a text field,
          one new field will be created with this name.

        """