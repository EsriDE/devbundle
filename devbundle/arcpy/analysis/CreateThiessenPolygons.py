# Generated documentation for module arcpy.analysis


class CreateThiessenPolygons(object):
    """
    Creates Thiessen polygons from point features.
    """

    @property
    def description(self) -> str:
        return """

        CreateThiessenPolygons_analysis(in_features, out_feature_class, {fields_to_copy})

        Creates Thiessen polygons from point features.

     INPUTS:
      in_features (Feature Layer):
          The point input features from which Thiessen polygons will be
          generated.
      fields_to_copy {String}:
          Specifies which fields from the input features will be transferred to
          the output feature class. ONLY_FID-Only thefield from the
          input features will be
          transferred to the output feature class. This is the default.
          FIDALL-All fields from the input features will be transferred to the
          output feature class.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the Thiessen polygons that are
          generated from the point input features.

        """