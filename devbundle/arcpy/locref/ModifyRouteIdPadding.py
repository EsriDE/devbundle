# Generated documentation for module arcpy.locref


class ModifyRouteIdPadding(object):
    """
    Modifies the padding, null, and length properties for fields that are part of a multifield route ID.
    """

    @property
    def description(self) -> str:
        return """

        ModifyRouteIdPadding_locref(in_feature_class, route_id_padding;route_id_padding...)

        Modifies the padding, null, and length properties for fields that are
        part of a multifield route ID.

     INPUTS:
      in_feature_class (Feature Layer):
          The input multifield route ID network layer that contains fields for
          padding, null, and length values that need to be modified.
      route_id_padding (Value Table):
          A table of values that specifies the field to be modified and its
          corresponding padding, null, and length values.Field-The field to be
          modified.Length-The length value of the field to
          be modified. The field length
          should be between 1 and the length of the database field.
          Variable Length-Specifies if thevalue is a variable value or
          a fixed value. LengthEnable Padding-Specifies if the field
          supports padding.Padding Character-The padding character for the
          field. The default is
          a space. Padding Location-                  Specifies where
          the
          padding should be applied to the field
          value. Left-Adds the padding characters to the left of the
          value in the
          field. This is the default.Right-Adds the padding characters to the
          right of the value in the
          field.Left and Right-Adds the padding characters to the left and right
          of
          the value in the field.Pad if Null-Specifies if the padding characters
          are added when the
          field has a null value.Allow Null Values-Specifies if the field
          supports null values.

        """