# Generated documentation for module arcpy.intelligence


class BatchImportData(object):
    """
    Imports KML, KMZ, shapefiles, Excel worksheets, tabular text files, GeoJSON, and GPX files to feature classes stored in a single geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        BatchImportData_intelligence(in_data;in_data..., target_gdb, {filter}, {include_sub_folders}, {include_groundoverlay})

        Imports KML, KMZ, shapefiles, Excel worksheets, tabular text files,
        GeoJSON, and GPX files to feature classes stored in a single
        geodatabase.

     INPUTS:
      in_data (Folder / File):
          The folders containing the data files or the data files to convert to
          geodatabase feature classes.
      target_gdb (Workspace):
          The target geodatabase where output feature classes will be stored.
      filter {String}:
          Applies a filter to limit which files are imported from
          folders. The following wildcard characters for the filter work on the
          full path to the input data:Multiple patterns can be added to the
          filter by separating each pattern with the vertical bar or pipe
          delimiter (|). Pattern comparisons are not case sensitive, so using
          the *airport.shp, *AIRPORT.SHP, or *Airport.shp pattern, for example,
          will import the same shapefile. *-Match any character?-Match a
          single character[range]-Match a single
          character in the range[!range]-Match any character not in the range
          The following are filter examples:        To import all
          shapefiles, use *.shp.To import all shapefiles and all
          .kml files, use *.shp|*.kml.To import all files that have airport in
          the file path or file name,
          use *airport*.To import all .geojson files that have airport in the
          file path or
          file name, use *airport*.geojson.To import all .kmz files that have
          airport appended with any two
          characters in the name, use *airport??.kmz.To import all files that
          have 1990 through 1997 in the file path or
          file name, use *199[0-7]*.To import all shapefiles that have the exact
          folder name airfacilities
          in their file path, use *\airfacilities\*.shp.
      include_sub_folders {Boolean}:
          Specifies whether subfolders will be recursively
          explored.SUBFOLDERS-All subfolders will be explored This is the
          default.NO_SUBFOLDERS-Only the top-level folder will be explored.
      include_groundoverlay {Boolean}:
          Specifies whether KML or KMZ ground overlays (raster, air photos, and
          so on) are included in the output.Use caution if the KMZ points to a
          service that serves raster imagery.
          The tool will attempt to translate the raster imagery at all available
          scales. This process may be lengthy and possibly overwhelm the
          service.GROUNDOVERLAY-Ground overlays will be included in the output.
          This is
          the default.NO_GROUNDOVERLAY-Ground overlays will not be included in
          the output.

        """