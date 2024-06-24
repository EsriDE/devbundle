# Generated documentation for module arcpy.intelligence


class CreateLocationFileFromTextFile(object):
    """
    Creates a location file for use in ArcGIS LocateXT from a text file from GeoNames, National Geospatial-Intelligence Agency Geonet Names Server, or U.S. Geological Survey Geographic Names Information Service.
    """

    @property
    def description(self) -> str:
        return """

        CreateLocationFileFromTextFile_intelligence(in_placenames_file, data_source, out_location_file, {include_features;include_features...}, {in_rois})

        Creates a location file for use in ArcGIS LocateXT from a text file
        from GeoNames, National Geospatial-Intelligence Agency Geonet Names
        Server, or U.S. Geological Survey Geographic Names Information
        Service.

     INPUTS:
      in_placenames_file (File):
          A place-names text file obtained from GeoNames, NGA GNS, or USGS GNIS.
      data_source (String):
          Specifies the data source from which the input was created.GEONAMES-
          The input file is from GeoNames.org.NGA_GNS-The input file
          is from NGA GNS.USGS_GNIS-The input file is from USGS
          GNIS.USGS_ANTARCTIC_NAMES-The input file is from USGS GNIS Antarctic
          Names.
      include_features {String}:
          Specifies the feature class types from the input data source that will
          be included in the output.ADMINISTRATIVE_FEATURES-Administrative
          features such as
          administrative boundaries, town, city, state, province, tribal, and
          country borders will be included.HYDROLOGICAL_FEATURES-Features such
          as rivers, lakes, ponds, and other
          water features will be included.LOCALITY_FEATURES-Features such as
          buildings, churches, hospitals, and
          other human-made points of interest will be
          included.POPULATED_PLACES-Locations of named places such as towns,
          cities,
          villages, and other consolidated areas of people will be
          included.TRANSPORTATION_FEATURES-Features such as roads, trails,
          railroads, and
          airports will be included.SPOT_FEATURES-Hypsographic features such as
          mountain peaks and other
          natural points of interest will be included.TERRAIN_FEATURES-Features
          such as mountains, hills, cliffs, craters,
          and ridges will be included.VEGETATION_FEATURES-Features such as
          forests, bushland, scrubland, and
          other areas of consistent vegetation will be
          included.UNDERSEA_FEATURES-Undersea features such as reefs, bars, and
          shipwrecks will be included.
      in_rois {Feature Layer}:
          The feature layer that will be used to create a subset of the input
          place-names file.

     OUTPUTS:
      out_location_file (File):
          The output location file.

        """