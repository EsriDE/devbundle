# Generated documentation for module arcpy.edit


class TransformFeatures(object):
    """
    Converts the coordinates of input features from one location to another through scaling, shifting, and rotating based on the transformation links between known corresponding control points.
    """

    @property
    def description(self) -> str:
        return """

        TransformFeatures_edit(in_features, in_link_features, {method}, {out_link_table})

        Converts the coordinates of input features from one location to
        another through scaling,  shifting, and rotating based on the
        transformation links between known corresponding control points.

     INPUTS:
      in_features (Feature Layer):
          The input features, the coordinates of which will be transformed. They
          can be points, lines, polygons, or annotations.
      in_link_features (Feature Layer):
          The input link features that link known control points for the
          transformation.
      method {String}:
          Specifies the transformation method that will be used to convert input
          feature coordinates.AFFINE-Aa minimum of three transformation links is
          required. This is
          the default.PROJECTIVE-A minimum of four transformation links is
          required.SIMILARITY-A minimum of two transformation links is required.

     OUTPUTS:
      out_link_table {Table}:
          The output table containing the input links and their residual errors.

        """