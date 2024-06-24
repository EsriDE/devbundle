# Generated documentation for module arcpy.ba


class RemoveOverlap(object):
    """
    Removes overlap between two or more areas to form adjacent boundaries.
    """

    @property
    def description(self) -> str:
        return """

        RemoveOverlap_ba(in_features, out_feature_class, {method}, {define_trade_area}, {ring_id_field}, {weight_field}, {store_id}, {in_stores_layer}, {link_field})

        Removes overlap between two or more areas to form adjacent boundaries.

     INPUTS:
      in_features (Feature Layer):
          The input features containing the overlapping polygons.
      method {String}:
          Specifies how the overlap between trade areas will be
          removed.CENTER_LINE-Overlap will be removed by creating a border that
          evenly
          distributes the area of intersection between polygons. This is the
          default.THIESSEN-Overlap will be removed using straight lines to
          divide the
          area of intersection.GRID-Overlap will be removed by creating a grid
          of parallel lines
          used to define a natural division between polygons.
      define_trade_area {Boolean}:
          Specifies whether ring overlap in a trade area will be
          removed.DEFINE_TRADE_AREA-Overlap will only be removed between
          polygons with
          equal values in the ring_id_field
          parameter.DO_NOT_DEFINE_TRADE_AREA-Overlap will be removed from all
          intersecting
          polygons. This is the default.
      ring_id_field {Field}:
          A field from the input that defines common trade areas. Overlap
          between polygons will only be removed if their values in this field
          are equal.
      weight_field {Field}:
          A field from the input used to influence removal of overlap based on
          its values.
      store_id {Field}:
          A unique ID field in the stores feature layer.
      in_stores_layer {Feature Layer}:
          The input features containing the center points for the overlapping
          trade areas.
      link_field {Field}:
          A unique ID field representing a store or facility location.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class containing the new trade area features.

        """