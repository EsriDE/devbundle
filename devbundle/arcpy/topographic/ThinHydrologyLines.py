# Generated documentation for module arcpy.topographic


class ThinHydrologyLines(object):
    """
    Generates a simplified hydrographic line network for display at a smaller scale. The resulting hydrographic network maintains the main arteries while thinning less significant features based on hierarchy, length, and spacing between features.
    """

    @property
    def description(self) -> str:
        return """

        ThinHydrologyLines_topographic(in_features, invisibility_field, min_length, {min_spacing}, {hierarchy_field}, {intersecting_features;intersecting_features...}, {unsplit_lines}, {use_angles})

        Generates a simplified hydrographic line network for display at a
        smaller scale. The resulting hydrographic network maintains the main
        arteries while thinning less significant features based on hierarchy,
        length, and spacing between features.

     INPUTS:
      in_features (Feature Layer):
          The hydrography line feature to be thinned.
      invisibility_field (Field):
          Features that participate in the thinned hydrography collection will
          have a value of 0. Those that are extraneous have a value of 1. A
          layer definition query can be used to display the results.
      min_length (Linear Unit):
          An indication of the shortest hydrographic segment that is sensible to
          display at the output scale. It defines a sense of the resolution or
          granularity of the resulting thinned hydrography. It should correspond
          to a length that is visually significant to include at the final
          scale. The results of this tool are a balanced compromise between the
          requirements posed by hierarchy, minimum length, minimum spacing,
          angle of connecting features, and directionality of the hydro
          geometry. Therefore, the minimum length value cannot necessarily be
          measured directly in the resulting feature set.
      min_spacing {Linear Unit}:
          An indication of the shortest distance between a hydrographic segment
          that is sensible to display at the output scale. If the spacing
          between two parallel trending features is smaller than this value, one
          of the features will be set as invisible. It defines a sense of the
          density of the resulting thinned hydrography. It should correspond to
          the distance between two parallel trending features that is visually
          significant to include at the final scale. When the density of
          features is too high (that is, the features are too closely spaced),
          at least one feature will be hidden. This can result in important
          features or features longer than the min_length being hidden.
          An indication of the shortest distance between a hydrographic
          segment that is sensible to display at the output scale. If the
          spacing between two parallel trending features is smaller than this
          value, one of the features will be set as invisible. It defines a
          sense of the density of the resulting thinned hydrography. It should
          correspond to the distance between two parallel trending features that
          is visually significant to include at the final scale. When the
          density of features is too high (that is, the features are too closely
          spaced), at least one feature will be hidden. This can result in
          important features or features longer than thebeing hidden.
          Minimum Length
      hierarchy_field {Field}:
          This field contains the hierarchical ranking of feature importance,
          where 1 is very important, and larger integers reflect decreasing
          importance. A value of 0 forces the feature to remain visible in the
          final results. It identifies the relative importance of features to
          help establish which features are significant. For optimal results,
          use no more than five levels of hierarchy. Input features with
          Hierarchy = 0 are considered locked and will remain visible, along
          with adjacent features necessary for connectivity.
      intersecting_features {Feature Layer}:
          If a segment is snapped to features in the provided layers, it will
          not be removed. An example would be a small river segment snapped to a
          lake. Even if the segment is under the min_length, it would need to
          remain to ensure that it remains connected to the water body into
          which it flows.
      unsplit_lines {Boolean}:
          This will merge any split features in the in_features to help ensure
          that the main waterway is preserved. If set to NO_UNSPLIT_LINES, the
          ends of the waterway may be removed due to them being under the
          min_length.UNSPLIT_LINES-Features that are closed on both end points
          will be
          merged before thinning to preserve main hydrographic arteries that
          traverse a long distance. This is the
          default.NO_UNSPLIT_LINES-Features will remain split before the
          thinning
          process.
      use_angles {Boolean}:
          If set to USE_ANGLES, the angles between waterway branches will be
          used to help determine the main waterway; the highest angle will be
          used. If disabled, the longest branch will be considered part of the
          main waterway.USE_ANGLES-In junctions with 3 or more waterways,
          features that are
          closer together in angle will be kept.NO_USE_ANGLES-In junctions with
          3 or more waterways, features that are
          longer will be kept. This is the default.

        """