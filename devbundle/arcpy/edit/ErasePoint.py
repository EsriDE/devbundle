# Generated documentation for module arcpy.edit


class ErasePoint(object):
    """
    Deletes points from the input that are either inside or outside the remove features, depending on the operation type.
    """

    @property
    def description(self) -> str:
        return """

        ErasePoint_edit(in_features, remove_features, {operation_type})

        Deletes points from the input that are either inside or outside the
        remove features, depending on the operation type.

     INPUTS:
      in_features (Feature Layer):
          The input point features.
      remove_features (Feature Layer):
          The polygon features that will be used to determine which features
          from the in_features value will be deleted.
      operation_type {String}:
          Specifies whether points inside or outside the remove features will be
          deleted.INSIDE-Input point features inside or on the boundary of the
          remove
          features will be deleted.OUTSIDE-Input point features outside the
          remove features will be
          deleted.

        """