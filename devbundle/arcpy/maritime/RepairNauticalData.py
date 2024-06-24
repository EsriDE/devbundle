# Generated documentation for module arcpy.maritime


class RepairNauticalData(object):
    """
    Repairs selected data processes on a database with the Nautical schema. Processes include repairing noncollocated structure-equipment features, deleting detached FREL and COLLECTIONS records, resolving blank or duplicate LNAM attribute values, and nudging point or line features that fall exactly at the cell or MetaDataA (M_CSCL) boundaries.
    """

    @property
    def description(self) -> str:
        return """

        RepairNauticalData_maritime(in_workspace, repair_operations;repair_operations...)

        Repairs selected data processes on a database with the Nautical
        schema. Processes include repairing noncollocated structure-equipment
        features, deleting detached FREL and COLLECTIONS records, resolving
        blank or duplicate LNAM attribute values, and nudging point or line
        features that fall exactly at the cell or MetaDataA (M_CSCL)
        boundaries.

     INPUTS:
      in_workspace (Workspace):
          The file or enterprise geodatabase that will be repaired.
      repair_operations (String):
          Specifies the repair process that will be used.
          FIX_LNAM-Records with a blankattribute will be resolved by
          populating the records with a validvalue, and duplicateattribute
          conflicts will be resolved with a newvalue provided to one of the
          records. LNAMLNAMLNAMLNAMREMOVE_ORPHAN_RELATIONSHIPS-Detached
          structure or equipment and
          collections records will be removed from the PLTS_FREL and
          PLTS_COLLECTIONS tables.MOVE_EQUIPMENT_FEATURES-Point equipment
          features that are not
          coincident with point structure features will be identified and moved
          to the location of the structure.NUDGE_BOUNDARY_FEATURES-If an
          adjacent cell exists with the same
          navigational purpose, point and line features that entirely intersect
          the cell boundary will be nudged 1e-7 West (if along a cell meridian)
          or 1e-7 South (if along a cell parallel). If there is no adjacent
          cell, the feature will be nudged in the opposite direction. Point and
          line features that entirely intersect the boundary of any MetaDataA
          (M_CSCL) and meet the extraction criteria will be nudged inside the
          M_CSCL feature. Point and line features that meet the ProductCoverage
          criteria will be nudged into the product.

        """