# Generated documentation for module arcpy.edit


class RubbersheetFeatures(object):
    """
    Modifies input features by spatially adjusting them through rubbersheeting, using the specified rubbersheet links, so they are better aligned with the intended target features.
    """

    @property
    def description(self) -> str:
        return """

        RubbersheetFeatures_edit(in_features, in_link_features, {in_identity_links}, {method})

        Modifies input features by spatially adjusting them through
        rubbersheeting, using the specified rubbersheet links, so they are
        better aligned with the intended target features.

     INPUTS:
      in_features (Feature Layer):
          The input features that will be adjusted. They can be points, lines,
          polygons, or annotations.
      in_link_features (Feature Layer):
          The input line features representing regular links for rubbersheeting.
      in_identity_links {Feature Layer}:
          The input point features representing identity links for
          rubbersheeting.
      method {String}:
          Specifies the rubbersheeting method that will be used to adjust
          features.LINEAR-This method is slightly faster and produces good
          results when
          you have many links spread uniformly over the data you are adjusting.
          This is the default.NATURAL_NEIGHBOR-This method should be used when
          you have few links
          spaced widely apart.

        """