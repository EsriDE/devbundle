# Generated documentation for module arcpy.management


class FeatureEnvelopeToPolygon(object):
    """
    Creates a feature class containing polygons, each of which represents the envelope of an input feature.
    """

    @property
    def description(self) -> str:
        return """

        FeatureEnvelopeToPolygon_management(in_features, out_feature_class, {single_envelope})

        Creates a feature class containing polygons, each of which represents
        the envelope of an input feature.

     INPUTS:
      in_features (Feature Layer):
          The input features that can be multipoint, line, polygon, or
          annotation.
      single_envelope {Boolean}:
          Specifies whether to use one envelope for each entire multipart
          feature or one envelope per part of a multipart feature. This
          parameter will affect the results of multipart input features
          only.SINGLEPART-Uses one envelope containing an entire multipart
          feature;
          therefore, the resulting polygon will be singlepart. This is the
          default.MULTIPART-Uses one envelope for each part of a multipart
          feature; the
          resulting polygon of the multipart feature will remain multipart.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class.

        """