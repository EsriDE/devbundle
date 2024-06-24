# Generated documentation for module arcpy.parcel


class SetParcelLineLabelPosition(object):
    """
    Sets the label position of the line's COGO dimension to the left of the parcel line, to the right of the parcel line, or centered over the parcel line.
    """

    @property
    def description(self) -> str:
        return """

        SetParcelLineLabelPosition_parcel(in_parcel_features;in_parcel_features...)

        Sets the  label position of the line's COGO dimension to the left of
        the parcel line, to the right of the parcel line, or centered over the
        parcel line.

     INPUTS:
      in_parcel_features (Feature Layer):
          The input parcel line layers with label positions that will be
          updated.

        """