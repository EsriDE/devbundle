# Generated documentation for module arcpy.management


class Sort(object):
    """
    Reorders records in a feature class or table, in ascending or descending order, based on one or multiple fields. The reordered result is written to a new dataset.
    """

    @property
    def description(self) -> str:
        return """

        Sort_management(in_dataset, out_dataset, sort_field;sort_field..., {spatial_sort_method})

        Reorders records in a feature class or table, in ascending or
        descending order, based on one or multiple fields. The reordered
        result is written to a new dataset.

     INPUTS:
      in_dataset (Table View):
          The input dataset with the records that will be reordered based on the
          field values in the sort field or fields.
      sort_field (Value Table):
          The field or fields whose values will be used to reorder the input
          records and the direction the records will be sorted. Sorting
          by thefield or by multiple fields is only available
          with an ArcGIS Pro Advanced license. Sorting by a single attribute
          field (excluding) is available at all license levels.
          ShapeShapeAscending-Records will be sorted from low value to high
          value.Descending-Records will be sorted from high value to low value.
      spatial_sort_method {String}:
          Specifies how features will be spatially sorted. The sort
          method is only enabled when thefield is designated as one of the sort
          fields. ShapeUR-Sorting will start at the upper right corner.
          This is the
          default.UL-Sorting will start at the upper left corner.LR-Sorting will
          start at the lower right corner.LL-Sorting will start at the lower
          left corner.PEANO-A space filling curve algorithm, also known as a
          Peano curve,
          will be used to sort.

     OUTPUTS:
      out_dataset (Feature Class / Table):
          The output feature class or table.

        """