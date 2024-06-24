# Generated documentation for module arcpy.management


class MinimumBoundingGeometry(object):
    """
    Creates a feature class containing polygons which represent a specified minimum bounding geometry enclosing each input feature or each group of input features.
    """

    @property
    def description(self) -> str:
        return """

        MinimumBoundingGeometry_management(in_features, out_feature_class, {geometry_type}, {group_option}, {group_field;group_field...}, {mbg_fields_option})

        Creates a feature class containing polygons which represent a
        specified minimum bounding geometry enclosing each input feature or
        each group of input features.

     INPUTS:
      in_features (Feature Layer):
          The input features that can be point, multipoint, line, polygon, or
          multipatch.
      geometry_type {String}:
          Specifies what type of minimum bounding geometry the output polygons
          will represent.RECTANGLE_BY_AREA-The rectangle of the smallest area
          enclosing an
          input feature. This is the default.RECTANGLE_BY_WIDTH-The rectangle of
          the smallest width enclosing an
          input feature.CONVEX_HULL-The smallest convex polygon enclosing an
          input feature.CIRCLE-The smallest circle enclosing an input feature
          envelope.ENVELOPE-The envelope of an input feature.
      group_option {String}:
          Specifies how the input features will be grouped; each group will be
          enclosed with one output polygon.NONE-Input features will not be
          grouped. This is the default. This
          option is not available for point input.ALL-All input features will be
          treated as one group.LIST-Input features will be grouped based on
          their common values in
          the specified field or fields in the group field parameter.
      group_field {Field}:
          The field or fields in the input features that will be used to group
          features, when LIST is specified as group_option. At least one group
          field is required for LIST option. All features that have the same
          value in the specified field or fields will be treated as a group.
      mbg_fields_option {Boolean}:
          Specifies whether to add the geometric attributes in the output
          feature class or omit them in the output feature
          class.NO_MBG_FIELDS-Omits any input attributes in the output feature
          class.
          This is the default.MBG_FIELDS-Adds the geometric attributes in the
          output feature class.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class.

        """