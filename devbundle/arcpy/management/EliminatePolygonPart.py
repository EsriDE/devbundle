# Generated documentation for module arcpy.management


class EliminatePolygonPart(object):
    """
    Creates a new output feature class containing the features from the input polygons with some parts or holes of a specified size deleted.
    """

    @property
    def description(self) -> str:
        return """

        EliminatePolygonPart_management(in_features, out_feature_class, {condition}, {part_area}, {part_area_percent}, {part_option})

        Creates a new output feature class containing the features from the
        input polygons with some parts or holes of a specified size deleted.

     INPUTS:
      in_features (Feature Layer):
          The input feature class or layer whose features will be copied to the
          output feature class, with some parts or holes eliminated.
      condition {String}:
          Specify how the parts to be eliminated will be determined.AREA-Parts
          with an area less than that specified will be
          eliminated.PERCENT-Parts with a percent of the total outer area less
          than that
          specified will be eliminated.AREA_AND_PERCENT-Parts with an area and
          percent less than that
          specified will be eliminated. Only if a polygon part meets both the
          area and percent criteria will it be deleted.AREA_OR_PERCENT-Parts
          with an area or percent less than that specified
          will be eliminated. If a polygon part meets either the area or percent
          criteria, it will be deleted.
      part_area {Areal Unit}:
          Eliminate parts smaller than this area.
      part_area_percent {Double}:
          Eliminate parts smaller than this percentage of a feature's total
          outer area.
      part_option {Boolean}:
          Determines what parts can be eliminated.CONTAINED_ONLY-Only parts
          totally contained by other parts can be
          eliminated. This is the default.ANY-Any parts can be eliminated.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class containing the remaining parts.

        """