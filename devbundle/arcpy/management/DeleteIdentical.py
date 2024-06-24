# Generated documentation for module arcpy.management


class DeleteIdentical(object):
    """
    Deletes records from a feature class or table that have identical values in a set of fields. If the geometry field is selected, feature geometries are compared.
    """

    @property
    def description(self) -> str:
        return """

        DeleteIdentical_management(in_dataset, fields;fields..., {xy_tolerance}, {z_tolerance})

        Deletes records from a feature class or table that have identical
        values in a set of fields. If the geometry field is selected, feature
        geometries are compared.

     INPUTS:
      in_dataset (Table View):
          The table or feature class that will have its identical records
          deleted.
      fields (Field):
          The field or fields whose values will be compared to find identical
          records.
      xy_tolerance {Linear Unit}:
          The x,y tolerance that will be applied to each vertex when evaluating
          whether there is an identical vertex in another feature.
      z_tolerance {Double}:
          The z-tolerance that will be applied to each vertex when evaluating
          whether there is an identical vertex in another feature.

        """