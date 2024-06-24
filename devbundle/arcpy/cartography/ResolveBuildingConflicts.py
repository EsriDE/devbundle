# Generated documentation for module arcpy.cartography


class ResolveBuildingConflicts(object):
    """
    Resolves symbol conflicts among buildings with respect to linear barrier features by moving, resizing, or hiding buildings.
    """

    @property
    def description(self) -> str:
        return """

        ResolveBuildingConflicts_cartography(in_buildings;in_buildings..., invisibility_field, in_barriers;in_barriers..., building_gap, minimum_size, {hierarchy_field})

        Resolves symbol conflicts among buildings with respect to linear
        barrier features by moving, resizing, or hiding buildings.

     INPUTS:
      in_buildings (Layer):
          The input layers containing building features that may be in conflict
          or smaller than allowable size. Buildings can be either points or
          polygons. Buildings will be modified to resolve conflicts with other
          buildings and with barrier features. When point building layers
          are used as inputs, theproperty of
          the marker symbol layer must be set to a field in the feature class.
          This field will store the rotation adjustments. If multiple marker
          symbol layers in the same point symbol have theproperty connected to
          the same field, thesetting must match in each of those marker symbol
          layers. AngleAngleRotate clockwise
      invisibility_field (String):
          The short or long integer field that stores the invisibility values
          that can be used to remove some buildings from display to resolve
          symbol conflicts. Buildings with a value of 1 will be removed from
          display; those with a value of 0 will not be removed. Use a definition
          query on the layer to display visible buildings only. No features are
          deleted.
      in_barriers (Value Table):
          The layers containing the linear or polygon features that are conflict
          barriers for input building features. Buildings will be modified to
          resolve conflicts between buildings and barriers. The orient value is
          Boolean, specifying whether buildings will be oriented to the barrier
          layer. Gap specifies the distance that buildings will move
          toward or
          away from the barrier layer. A unit must be provided with the value.
          A gap value of 0 will snap buildings directly to the edge of the
          barrier line or outline symbology.A null (unspecified) gap value means
          that buildings will not be moved
          toward or away from barrier lines or outlines except movement required
          by conflict resolution.If no unit is provided with the gap value (that
          is, 10 instead of 10
          meters), the linear unit from the input feature's coordinate system
          will be used.
      building_gap (Linear Unit):
          The minimum allowable distance between symbolized buildings at scale.
          Buildings that are closer together will be displaced or hidden to
          enforce this distance. The minimum allowable distance is set relative
          to the reference scale (that is, 15 meters at 1:50,000 scale). The
          value is 0 if the reference scale is not set.
      minimum_size (Linear Unit):
          The minimum allowable size of the shortest side of a rotated best-fit
          bounding box around the symbolized building feature drawn at the
          reference scale. Buildings with a bounding box side smaller than this
          value will be enlarged to meet it. Resizing may occur
          nonproportionally, resulting in a change to the building morphology.
      hierarchy_field {String}:
          The short or long integer field that contains hierarchical ranking of
          feature importance in which 1 is very important and larger integers
          reflect decreasing importance. A value of 0 causes the building to
          retain visibility, although it may be moved somewhat to resolve
          conflicts. If this parameter is not used, feature importance will be
          assessed by the tool based on perimeter length and proximity to
          barrier features.

        """