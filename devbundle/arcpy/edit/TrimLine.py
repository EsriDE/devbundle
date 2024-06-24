# Generated documentation for module arcpy.edit


class TrimLine(object):
    """
    Removes portions of a line that extend a specified distance past a line intersection (dangles). Any line that does not touch another line at both endpoints can be trimmed, but only the portion of the line that extends past the intersection by the specified distance will be removed.
    """

    @property
    def description(self) -> str:
        return """

        TrimLine_edit(in_features, {dangle_length}, {delete_shorts})

        Removes portions of a line that extend a specified distance past a
        line intersection (dangles). Any line that does not touch another line
        at both endpoints can be trimmed, but only the portion of the line
        that extends past the intersection by the specified distance will be
        removed.

     INPUTS:
      in_features (Feature Layer):
          The line input features to be trimmed.
      dangle_length {Linear Unit}:
          Line segments that are shorter than the specified dangle length and do
          not touch another line at both endpoints (dangles) will be trimmed.If
          a dangle length is not specified, all dangling lines (line segments
          that do not touch another line at both endpoints), regardless of
          length, will be trimmed back to the point of intersection.
      delete_shorts {Boolean}:
          Specifies whether line segments which are less than the dangle length
          and are free-standing will be deleted.DELETE_SHORT-Delete short free-
          standing features. This is the
          default.KEEP_SHORT-Do not delete short free-standing features.

        """