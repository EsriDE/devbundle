# Generated documentation for module arcpy.management


class Analyze(object):
    """
    Updates database statistics of business tables, feature tables, and delta tables, along with the statistics of those tables' indexes.
    """

    @property
    def description(self) -> str:
        return """

        Analyze_management(in_dataset, components;components...)

        Updates database statistics of business tables, feature tables, and
        delta tables, along with the statistics of those tables' indexes.

     INPUTS:
      in_dataset (Layer / Table View / Dataset):
          The table or feature class to be analyzed.
      components (String):
          The component type to be analyzed.BUSINESS-Updates business rules
          statistics.FEATURE-Updates feature
          statistics.RASTER-Updates statistics on raster tables.ADDS-Updates
          statistics on added datasets.DELETES-Updates statistics on deleted
          datasets.

        """