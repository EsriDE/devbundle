# Generated documentation for module arcpy.parcel


class ApplyParcelLeastSquaresAdjustment(object):
    """
    Applies the results of a least squares adjustment to parcel fabric feature classes. Least squares adjustment results stored in the AdjustmentLines and AdjustmentPoints feature classes are applied to the corresponding parcel line, connection line, and parcel fabric point feature classes.
    """

    @property
    def description(self) -> str:
        return """

        ApplyParcelLeastSquaresAdjustment_parcel(in_parcel_fabric, {movement_tolerance}, {update_attributes})

        Applies the results of a least squares adjustment to parcel fabric
        feature classes. Least squares adjustment results stored in the
        AdjustmentLines and AdjustmentPoints feature classes are applied to
        the corresponding parcel line, connection line, and parcel fabric
        point feature classes.

     INPUTS:
      in_parcel_fabric (Parcel Layer):
          The parcel fabric to be updated.
      movement_tolerance {Linear Unit}:
          The tolerance representing the minimum allowable coordinate shift when
          updating parcel fabric points. If the distance between the adjustment
          point and the parcel fabric point is greater than the specified
          tolerance, the parcel fabric point is updated to the location of the
          adjustment point. The default tolerance is 0.05 meters.
      update_attributes {Boolean}:
          Specifies whether attribute fields in the parcel fabric Points
          feature class will be updated with statistical metadata. The,,,
          andfields will be updated with the values stored in the same fields in
          the AdjustmentPoints feature class. XY UncertaintyError Ellipse
          Semi MajorError Ellipse Semi MinorError Ellipse
          DirectionUPDATE_ATTRIBUTES-Attribute fields in the parcel fabric
          Points feature
          class will be updated with statistical
          metadata.NO_UPDATE_ATTRIBUTES-Attribute fields will not be updated.
          This is the
          default.

        """