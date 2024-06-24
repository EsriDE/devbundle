# Generated documentation for module arcpy.management


class Compact(object):
    """
    Compacts a file or mobile geodatabase, SQLite database, or Open Geospatial Consortium (OGC) GeoPackage file. Compacting rearranges data storage, often reducing the file's size and improving performance.
    """

    @property
    def description(self) -> str:
        return """

        Compact_management(in_workspace)

        Compacts a file or mobile geodatabase, SQLite database, or Open
        Geospatial Consortium (OGC) GeoPackage file. Compacting rearranges
        data storage, often reducing the file's size and improving
        performance.

     INPUTS:
      in_workspace (Workspace):
          The file or mobile geodatabase, SQLite database, or GeoPackage that
          will be compacted.

        """