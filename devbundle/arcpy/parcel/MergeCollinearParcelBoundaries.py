# Generated documentation for module arcpy.parcel


class MergeCollinearParcelBoundaries(object):
    """
    Merges connected collinear parcel lines into a single parcel line. Shared parcel fabric points between connected collinear lines are deleted and vertices are created in their place.
    """

    @property
    def description(self) -> str:
        return """

        MergeCollinearParcelBoundaries_parcel(in_parcel_boundaries, offset_tolerance)

        Merges connected collinear parcel lines into a single parcel line.
        Shared parcel fabric points between connected collinear lines are
        deleted and vertices are created in their place.

     INPUTS:
      in_parcel_boundaries (Feature Layer):
          The parcel lines to be merged. Lines can be parcel lines or connection
          lines.
      offset_tolerance (Linear Unit):
          The maximum distance that parcel points between collinear lines can be
          offset for the line to be considered collinear. The offset is the
          distance between the collinear parcel points and the straight lines
          between the endpoints of the connected parcel lines.

        """