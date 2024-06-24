# Generated documentation for module arcpy.management


class SortCodedValueDomain(object):
    """
    Sorts the code or description of a coded value domain in either ascending or descending order.
    """

    @property
    def description(self) -> str:
        return """

        SortCodedValueDomain_management(in_workspace, domain_name, sort_by, sort_order)

        Sorts the code or description of a coded value domain in either
        ascending or descending order.

     INPUTS:
      in_workspace (Workspace):
          The geodatabase containing the domain to be sorted.
      domain_name (String):
          The name of the coded value domain to be sorted.
      sort_by (String):
          Specifies whether the code or description will be used to sort the
          domain.CODE-Records are sorted based on the code value for the
          domain.DESCRIPTION-Records are sorted based on the description value
          for the
          domain.
      sort_order (String):
          Specifies the direction the records will be sorted.ASCENDING-Records
          are sorted from low value to high
          value.DESCENDING-Records are sorted from high value to low value.

        """