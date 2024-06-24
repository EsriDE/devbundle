# Generated documentation for module arcpy.ga


class ArealInterpolationLayerToPolygons(object):
    """
    Reaggregates the predictions of an Areal Interpolation layer to a new set of polygons.
    """

    @property
    def description(self) -> str:
        return """

        ArealInterpolationLayerToPolygons_ga(in_areal_interpolation_layer, in_polygon_features, out_feature_class, {append_all_fields})

        Reaggregates the predictions of an Areal Interpolation layer to a new
        set of polygons.

     INPUTS:
      in_areal_interpolation_layer (Geostatistical Layer):
          Input geostatistical layer resulting from an Areal Interpolation
          model.
      in_polygon_features (Feature Layer):
          The polygons where predictions and standard errors will be aggregated.
      append_all_fields {Boolean}:
          Determines whether all fields will be copied from the input features
          to the output feature class.ALL-All fields from the input features
          will be copied to the output
          feature class. This is the default. FID_ONLY-Only the feature
          ID will be copied, and it will be
          namedon the output feature class. Source_ID

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the aggregated predictions and
          standard errors for the new polygons.

        """