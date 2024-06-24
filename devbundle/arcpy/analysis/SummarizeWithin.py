# Generated documentation for module arcpy.analysis


class SummarizeWithin(object):
    """
    Overlays a polygon layer with another layer to summarize the number of points, length of the lines, or area of the polygons within each polygon, and calculate attribute field statistics about the features within the polygons.
    """

    @property
    def description(self) -> str:
        return """

        SummarizeWithin_analysis(in_polygons, in_sum_features, out_feature_class, {keep_all_polygons}, {sum_fields;sum_fields...}, {sum_shape}, {shape_unit}, {group_field}, {add_min_maj}, {add_group_percent}, {out_group_table})

        Overlays a polygon layer with another layer to summarize the number of
        points, length of the lines, or area of the polygons within each
        polygon, and calculate attribute field statistics about the features
        within the polygons.

     INPUTS:
      in_polygons (Feature Layer):
          The polygons that will be used to summarize the features, or portions
          of features, in the input summary layer.
      in_sum_features (Feature Layer):
          The point, line, or polygon features that will be summarized for each
          polygon in the input polygons.
      keep_all_polygons {Boolean}:
          Specifies whether all input polygons or only those intersecting or
          containing at least one input summary feature will be copied to the
          output feature class.KEEP_ALL-All input polygons will be copied to the
          output feature
          class. This is the default.ONLY_INTERSECTING-Only input polygons that
          intersect or contain at
          least one input summary feature will be copied to the output feature
          class.
      sum_fields {Value Table}:
          A list of attribute field names from the input summary features, as
          well as statistical summary types that will be calculated for those
          attribute fields for all points in each polygon.Summary fields must be
          numeric. Text and other attribute field types
          are not supported. The following are the statistic types:
          Sum-The total
          value of all the points in each polygon will be
          calculated.Mean-The average or mean value of all the points in each
          polygon will
          be calculated.Min-The smallest value of all the points in each polygon
          will be
          identified.Max-The largest value of all the points in each polygon
          will be
          identified.Stddev-The standard deviation of all the points in each
          polygon will
          be calculated.
      sum_shape {Boolean}:
          Specifies whether attributes for the number of points, length of
          lines, and area of polygon features summarized in each input polygon
          will be added to the output feature class.ADD_SHAPE_SUM-Shape summary
          attributes will be added to the output
          feature class. This is the default.NO_SHAPE_SUM-Shape summary
          attributes will not be added to the output
          feature class.
      shape_unit {String}:
          Specifies the unit that will be used when calculating shape summary
          attributes. If the input summary features are points, no shape unit is
          necessary, since only the count of points in each input polygon is
          added.If the input summary features are lines, specify a linear unit.
          If the
          input summary features are polygons, specify an areal unit.METERS-The
          unit will be meters.KILOMETERS-The unit will be
          kilometers.FEET-The unit will be feet.YARDS-The unit will be
          yards.MILES-The unit will be miles.ACRES-The unit will be
          acres.HECTARES-The unit will be hectares.SQUAREMETERS-The unit will be
          square meters.SQUAREKILOMETERS-The unit will be square
          kilometers.SQUAREFEET-The unit will be square feet.SQUAREYARDS-The
          unit will be square yards.SQUAREMILES-The unit will be square miles.
      group_field {Field}:
          An attribute field from the input summary features that will be used
          for grouping. Features that have the same group field value will be
          combined and summarized with other features with the same group field
          value.When a group field is provided, the out_grouped_table parameter
          value
          is required.
      add_min_maj {Boolean}:
          Specifies whether minority and majority fields will be added to the
          output. This parameter allows you to determine which group field value
          is the minority (least dominant) and the majority (most dominant)
          within each input polygon.This parameter is enabled if you provided a
          group_field parameter
          value.NO_MIN_MAJ-Minority and majority fields will not be added to the
          output. This is the default.ADD_MIN_MAJ-Minority and majority fields
          will be added to the output.
      add_group_percent {Boolean}:
          Specifies whether a percentage attribute field will be added to the
          output. This parameter allows you to determine the percentage of each
          attribute value in each group.This parameter is enabled if you
          provided a group_field parameter
          value.NO_PERCENT-A percentage attribute field will not be added to the
          output. This is the default.ADD_PERCENT-A percentage attribute field
          will be added to the output.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class containing the same geometries and
          attributes as the input polygons. The feature class will include
          additional attributes for the number of points, length of lines, and
          area of polygons inside each input polygon and statistics about those
          features.
      out_group_table {Table}:
          An output table that includes summary fields for each group of summary
          features for each input polygon. The table will have the
          following attribute fields:
          -An ID corresponding to an ID field added to the output
          feature class          Join_IDThe group fieldA shape summary fieldOne
          field for each summary fieldA percentage fieldThis parameter is
          required when the group_field parameter value is
          provided.

        """