# Generated documentation for module arcpy.management


class SelectLayerByAttribute(object):
    """
    Adds, updates, or removes a selection based on an attribute query.
    """

    @property
    def description(self) -> str:
        return """

        SelectLayerByAttribute_management(in_layer_or_view, {selection_type}, {where_clause}, {invert_where_clause})

        Adds, updates, or removes a selection based on an attribute query.

     INPUTS:
      in_layer_or_view (Table View / Raster Layer / Mosaic Layer):
          The data to which the selection will be applied.
      selection_type {String}:
          Specifies how the selection will be applied and what to do if a
          selection already exists.NEW_SELECTION-The resulting selection will
          replace the current
          selection. This is the default.ADD_TO_SELECTION-The resulting
          selection will be added to the current
          selection if one exists. If no selection exists, this is the same as
          the new selection option.REMOVE_FROM_SELECTION-The resulting selection
          will be removed from the
          current selection. If no selection exists, this option has no
          effect.SUBSET_SELECTION-The resulting selection will be combined with
          the
          current selection. Only records that are common to both remain
          selected.SWITCH_SELECTION-The selection will be switched. All records
          that were
          selected will be removed from the current selection, and all records
          that were not selected will be added to the current selection. The
          where_clause parameter is ignored when this option is
          specified.CLEAR_SELECTION-The selection will be cleared or removed.
          The
          where_clause parameter is ignored when this option is specified.
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of records.
      invert_where_clause {Boolean}:
          Specifies whether the expression will be used as is, or the opposite
          of the expression will be used.NON_INVERT-The query will be used as
          is. This is the
          default.INVERT-The opposite of the query will be used. If the
          selection_type
          parameter is used, the reversal of the selection occurs before it is
          combined with existing selections.

        """