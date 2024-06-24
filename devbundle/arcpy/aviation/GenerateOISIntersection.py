# Generated documentation for module arcpy.aviation


class GenerateOISIntersection(object):
    """
    Creates the most restrictive (lowest) surfaces within the extent of all collective surfaces. Obstruction identification surfaces (OIS) determine objects that are vertical obstructions. An object is considered a vertical obstruction if it penetrates the OIS surface. Surfaces are used to support planning and design activities.
    """

    @property
    def description(self) -> str:
        return """

        GenerateOISIntersection_aviation(in_ois_features;in_ois_features..., out_ois_features, {multipart_feature})

        Creates the most restrictive (lowest) surfaces within the extent of
        all collective surfaces. Obstruction identification surfaces (OIS)
        determine objects that are vertical obstructions. An object is
        considered a vertical obstruction if it penetrates the OIS surface.
        Surfaces are used to support planning and design activities.

     INPUTS:
      in_ois_features (Feature Layer):
          The input OIS features. The feature class must be a multipatch.
      multipart_feature {Boolean}:
          Specifies whether multipart features will be created in the output.
          Multipart features are composed of more than one physical part that
          only references one set of attributes.MULTIPART-Multipart features
          will be created. This is
          default.MERGE_ADJACENT-Adjacent triangulated multipart features will
          be
          created as individual features.

     OUTPUTS:
      out_ois_features (Feature Layer):
          The updated feature class containing the meshed OIS with the lowest
          z-value.

        """