# Generated documentation for module arcpy.ba


class GenerateTradeAreaRings(object):
    """
    Creates rings around point locations.
    """

    @property
    def description(self) -> str:
        return """

        GenerateTradeAreaRings_ba(in_features, out_feature_class, {radii;radii...}, {units}, {id_field}, {remove_overlap}, {dissolve_option}, {input_method}, {expression})

        Creates rings around point locations.

     INPUTS:
      in_features (Feature Layer):
          The input features containing the center points for the rings.
      radii {Double}:
          The distances, in ascending size, used to create rings around the
          input features.
      units {String}:
          The linear unit to be used with the distance values.
      id_field {Field}:
          A unique ID field in the ring center layer.
      remove_overlap {Boolean}:
          Creates overlapping concentric rings or removes
          overlap.REMOVE_OVERLAP-Thiessen polygons are used to remove overlap
          between
          output ring polygons.KEEP_OVERLAP-Output ring features are created
          with overlap. This is
          the default.
      dissolve_option {String}:
          Specifies whether overlapping or nonoverlapping service areas for a
          single location will be used when multiple distances are
          specified.OVERLAP-Each polygon will include the area reachable from
          the facility
          up to the distance value. This is the default.SPLIT-Each polygon will
          include only the area between consecutive
          distance values.
      input_method {String}:
          Specifies the type of value that is to be used for each drive
          time.VALUES-Uses a constant value (all trade areas will be the same
          size).
          This is the default.EXPRESSION-The values from a field or an
          expression (trade areas can
          be a different size).
      expression {SQL Expression}:
          A fields-based expression to calculate the radii.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will contain the output ring features.

        """