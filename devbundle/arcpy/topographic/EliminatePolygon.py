# Generated documentation for module arcpy.topographic


class EliminatePolygon(object):
    """
    Eliminates a polygon by merging it with the polygon from the surrounding features that it shares the longest boundary with.
    """

    @property
    def description(self) -> str:
        return """

        EliminatePolygon_topographic(in_features, surrounding_features;surrounding_features..., {min_area})

        Eliminates a polygon by merging it with the polygon from the
        surrounding features that it shares the longest boundary with.

     INPUTS:
      in_features (Feature Layer):
          The feature layers that contain the polygons to be deleted.
      surrounding_features (Feature Layer):
          The polygon features that theare compared against. If the
          feature is smaller than the, it becomes part of the input features.
          Input FeaturesMinimum Area
      min_area {Areal Unit}:
          Polygons smaller than thewill be deleted. If theis left blank,
          all features or a selection set from thewill be considered for
          elimination. Minimum AreaMinimum AreaInput Features

        """