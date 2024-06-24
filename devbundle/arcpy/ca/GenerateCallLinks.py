# Generated documentation for module arcpy.ca


class GenerateCallLinks(object):
    """
    Creates line features that represent the call links between phones, using cell site points or cell site antenna sectors, based on the start date and time of the call.
    """

    @property
    def description(self) -> str:
        return """

        GenerateCallLinks_ca(in_primary_features, in_secondary_features, out_feature_class, {output_type}, {primary_subscriber_field}, {primary_destination_field}, {primary_start_time_field}, {secondary_subscriber_field}, {secondary_destination_field}, {secondary_start_time_field})

        Creates line features that represent the call links between phones,
        using cell site points or cell site antenna sectors, based on the
        start date and time of the call.

     INPUTS:
      in_primary_features (Feature Layer):
          The point feature class for the primary phone or sector derived from
          the Cell Phone Records To Feature Class tool.
      in_secondary_features (Feature Layer):
          The point feature class for the secondary phone or sector derived from
          the Cell Phone Records To Feature Class tool.
      output_type {String}:
          Specifies how the relationship of calls between two phones will be
          analyzed and symbolized.SUMMARY-A summary record of the total number
          of calls between two
          phones at various locations will be created. This is the
          default.DETAIL-An individual record of each call between two phones at
          various
          locations will be created.
      primary_subscriber_field {Field}:
          The unique ID field for the primary phone subscriber, usually a phone
          number.
      primary_destination_field {Field}:
          The field containing the phone number of the secondary phone.
      primary_start_time_field {Field}:
          The start date and time field of the primary phone records.
      secondary_subscriber_field {Field}:
          The unique ID field for the secondary phone subscriber, usually a
          phone number.
      secondary_destination_field {Field}:
          The field containing the phone number of the primary phone.
      secondary_start_time_field {Field}:
          The start date and time field of the secondary phone records.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output line features representing the call links between two
          phones at various locations.

        """