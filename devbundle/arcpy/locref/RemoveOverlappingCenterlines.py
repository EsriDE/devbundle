# Generated documentation for module arcpy.locref


class RemoveOverlappingCenterlines(object):
    """
    Removes overlapping centerline sections to ensure that there is one common centerline when centerline geometry overlaps.
    """

    @property
    def description(self) -> str:
        return """

        RemoveOverlappingCenterlines_locref(in_centerline_features)

        Removes overlapping centerline sections to ensure that there is one
        common centerline when centerline geometry overlaps.

     INPUTS:
      in_centerline_features (Feature Layer):
          An input layer or feature class representing an LRS centerline.

        """