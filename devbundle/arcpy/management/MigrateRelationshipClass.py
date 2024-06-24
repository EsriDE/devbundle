# Generated documentation for module arcpy.management


class MigrateRelationshipClass(object):
    """
    Migrates an object ID-based relationship class to a global ID-based relationship class.
    """

    @property
    def description(self) -> str:
        return """

        MigrateRelationshipClass_management(in_relationship_class)

        Migrates an object ID-based relationship class to a global ID-based
        relationship class.

     INPUTS:
      in_relationship_class (Relationship Class):
          An object ID-based relationship class that will be migrated to
          a global ID-based relationship class. The origin and destination
          feature classes or tables must have an existingfield. GlobalID

        """