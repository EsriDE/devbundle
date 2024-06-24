# Generated documentation for module arcpy.management


class AddRastersToMosaicDataset(object):
    """
    Adds raster datasets to a mosaic dataset from various sources, including a file, folder, table, or web service.
    """

    @property
    def description(self) -> str:
        return """

        AddRastersToMosaicDataset_management(in_mosaic_dataset, raster_type, input_path;input_path..., {update_cellsize_ranges}, {update_boundary}, {update_overviews}, {maximum_pyramid_levels}, {maximum_cell_size}, {minimum_dimension}, {spatial_reference}, {filter}, {sub_folder}, {duplicate_items_action}, {build_pyramids}, {calculate_statistics}, {build_thumbnails}, {operation_description}, {force_spatial_reference}, {estimate_statistics}, {aux_inputs;aux_inputs...}, {enable_pixel_cache}, {cache_location})

        Adds raster datasets to a mosaic dataset from various sources,
        including a file, folder, table, or web service.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The path and name of the mosaic dataset to which the raster data will
          be added.
      raster_type (Raster Type):
          The type of raster that will be added. The raster type is specific to
          imagery products. It identifies metadata-such as georeferencing,
          acquisition date, and sensor type-along with a raster format.If you
          are using a LAS, LAS Dataset, or Terrain raster type, an .art
          file must be used when the cell size is specified.For a list of
          supported sensors and raster types, see the list of
          supported sensors.
      input_path (Workspace / File / WCS Coverage / Image Service / Map Server / WMS Map / Raster Catalog / Table View / Raster Layer / Mosaic Layer / Terrain Layer / LAS Dataset Layer / Layer File / WMTS Layer):
          Specifies the path and name of the input file, folder, raster dataset,
          mosaic dataset, table, or service.Not all input options will be
          available. The selected raster type
          determines the available options.Dataset-An ArcGIS geographic dataset,
          such as a raster or mosaic
          dataset in a geodatabase or table, will be used as input.
          Folder-A folder containing multiple raster datasets will be
          used as input. The folder can contain subfolders.
          This option is affected by theandparameters.
          Include Sub FoldersInput Data Filter         File-One or more raster
          datasets stored in a folder on disk,
          an image service definition file (.ISDef), or a raster process
          definition file (.RPDef) will be used as input. Files that do
          not correspond to the raster type being added will be
          ignored. Do not use this option with file formats that are
          raster
          datasets, such as TIFF or MrSID files; use theoption instead.
          DatasetService-A WCS, a map, an image service, or a web service layer
          file
          will be used as input.
      update_cellsize_ranges {Boolean}:
          Specifies whether the cell size ranges of each raster in the
          mosaic dataset will be calculated. These values will be written to the
          attribute table in theandfields.
          minPSmaxPSUPDATE_CELL_SIZES-The cell size ranges will be calculated
          for all the
          rasters in the mosaic dataset. This is the default.NO_CELL_SIZES-The
          cell size ranges will not be calculated.
      update_boundary {Boolean}:
          Specifies whether the boundary polygon of a mosaic dataset will be
          generated or updated. By default, the boundary merges all the
          footprint polygons to create a single boundary representing the extent
          of the valid pixels.UPDATE_BOUNDARY-The boundary will be generated or
          updated. This is the
          default.NO_BOUNDARY-The boundary will not be generated or updated.
      update_overviews {Boolean}:
          Specifies whether overviews for a mosaic dataset will be defined and
          generated.UPDATE_OVERVIEWS-Overviews will be defined and
          generated.NO_OVERVIEWS-Overviews will not be defined or generated.
          This is the
          default.
      maximum_pyramid_levels {Long}:
          The maximum number of pyramid levels that will be used in the mosaic
          dataset. For example, a value of 2 will use only the first two pyramid
          levels from the source raster. Leaving this parameter blank or typing
          a value of -1 will build pyramids for all levels.This value can affect
          the display and number of overviews that will be
          generated.
      maximum_cell_size {Double}:
          The maximum pyramid cell size that will be used in the mosaic dataset.
      minimum_dimension {Long}:
          The minimum dimensions of a raster pyramid that will be used in the
          mosaic dataset.
      spatial_reference {Spatial Reference}:
          The spatial reference system of the input data.This should be
          specified if the data does not have a coordinate
          system; otherwise, the coordinate system of the mosaic dataset will be
          used. This can also be used to override the coordinate system of the
          input data.
      filter {String}:
          A filter for the data being added to the mosaic dataset. You can use
          SQL expressions to create the data filter. The wildcards for the
          filter work on the full path to the input data. The following
          SQL statement will select the rows in which the
          following object IDs match:        OBJECTID IN (19745, 19680, 19681,
          19744, 5932, 5931, 5889, 5890,
          14551, 14552, 14590, 14591)        To add only a TIFF image, add an
          asterisk before a file
          extension. *.TIF        To add an image with the word sensor in
          the file path or file
          name, add an asterisk before and after the word sensor.
          *sensor2009*        You can also use PERL syntax to create a data
          filter.
          REGEX:.*1923.*|.*1922.*REGEX:.*192[34567].*|.*194.*|.*195.*        The
          following PERL syntax with multiple lexical groupings as
          part of the expression is not supported:        REGEX:.*
          map_mean_.*(?:(?:[a-z0-9]*)_pptPct_(?:[0-9]|1[0-2]*?)_2[0-9]_*\w*).img
          Alternatively, you can use the following syntax:
          REGEX:.*map_mean_*[a-z0-9]*_pptPct_([0-9]|1[0-2])_2[0-9]*_\w*.img
      sub_folder {Boolean}:
          Specifies whether subfolders will be recursively
          explored.SUBFOLDERS-All subfolders will be explored for data. This is
          the
          default.NO_SUBFOLDERS-Only the top-level folder will be explored for
          data.
      duplicate_items_action {String}:
          Specifies how duplicate rasters will be handled. A check will be
          performed to determine whether each raster has already been added,
          using the original path and file name. Choose the action to be
          performed when a duplicate path and file name are
          found.ALLOW_DUPLICATES-All rasters will be added even if they already
          exist
          in the mosaic dataset. This is the
          default.EXCLUDE_DUPLICATES-Duplicate rasters will not be
          added.OVERWRITE_DUPLICATES-Duplicate rasters will overwrite existing
          rasters.
      build_pyramids {Boolean}:
          Specifies whether pyramids will be built for each source
          raster.NO_PYRAMIDS-Pyramids will not be built. This is the
          default.BUILD_PYRAMIDS-Pyramids will be built.
      calculate_statistics {Boolean}:
          Specifies whether statistics will be calculated for each source
          raster.NO_STATISTICS-Statistics will not be calculated. This is the
          default.CALCULATE_STATISTICS-Statistics will be calculated.
      build_thumbnails {Boolean}:
          Specifies whether thumbnails will be built for each source
          raster.NO_THUMBNAILS-Thumbnails will not be built. This is the
          default.BUILD_THUMBNAILS-Thumbnails will be built.
      operation_description {String}:
          The description used to represent the operation of adding raster data.
          It will be added to the raster type table, which can be used as part
          of a search or as a reference at another time.
      force_spatial_reference {Boolean}:
          Specifies the coordinate system that will be used. Use the coordinate
          system specified in the spatial_reference parameter for all the
          rasters when loading data into the mosaic
          dataset.NO_FORCE_SPATIAL_REFERENCE-The coordinate system of each
          raster data
          will be used when loading data. This is the
          default.FORCE_SPATIAL_REFERENCE-The coordinate system specified in the
          spatial_reference parameter will be used for each raster when loading
          data.
      estimate_statistics {Boolean}:
          Specifies whether statistics will be estimated on the mosaic dataset
          for faster rendering and processing at the mosaic dataset
          level.NO_STATISTICS-Statistics will not be estimated. Statistics
          generated
          from each item in the mosaic dataset will be used for display and
          processing. This is the default.ESTIMATE_STATISTICS-Statistics will be
          estimated at the mosaic dataset
          level. This will use the distribution of pixels to display the mosaic
          dataset rather than the distribution of the source item in the mosaic
          dataset.
      aux_inputs {Value Table}:
          The raster type settings that will be defined on thepage. This
          parameter will override the settings defined on thepage. Auxiliary
          input options include the following:        Raster Type
          PropertiesRaster Type PropertiesCameraFile-A .cam or .csv file that
          stores the camera model
          information, such as the focal length, sensor pixel size, columns,
          rows and similar attributes.CameraProperties-A JSON string that
          defines the camera model.ConstantZ-A value, in meters, that is used to
          provide an initial
          estimate of the flight height for each image.CorrectGeoid-A value of 0
          represents false, and a value of 1
          represents true. This option is only available when a DEM is
          used.DEM-A DEM used to provide an initial estimate of the flight
          height for
          each image.EstimateFlightHeight-An estimated flight height which can
          be directly
          used to compute footprint and estimate photo scale.GPSAltRef-Define
          the altitude used as the reference altitude. 0
          indicates above sea level, and 1 is below sea level.
          GPSFile-A GPS text file, such as a comma-separated value
          file (.csv), which includes values for the,,, andfields, and
          optionally, the,, andfields. The geolocation file is provided by the
          supplier along with the drone imagery. Image
          NameLatitudeLongitudeAltitudeOmegaPhiKappaGPSLatRef-Define whether the
          latitude is north or south latitude. N
          indicates north latitude, and S is south latitude.GPSLonRef-Define
          whether the longitude is east or west longitude. E
          indicates east longitude, and W is west longitude.GPSSRS-Define the
          spatial reference of the GPS.GPSVCS-Define the vertical coordinate
          system of the GPS.IsAltitudeFlightHeight-A Boolean value defines
          whether the drone
          reports heights relative to the takeoff point, or altitude for heights
          relative to a vertical datum. Use a value of 0 when the altitude value
          is altitude above a datum, and a value of 1 when the altitude value is
          flight height from a takeoff point.MinimumFlightHeight-Define the
          minimum flight height. If the estimated
          flight height of an image is smaller than this number, the image will
          be considered invalid and will not be added to the image collection
          for future processing.ZFactor-The scaling factor used to convert the
          elevation values. This
          option is only available when using a DEM.ZOffset-The base value to be
          added to the elevation value in the DEM.
          This can be used to offset elevation values that do not start at sea
          level. This option is only available when using a DEM.
      enable_pixel_cache {Boolean}:
          Specifies whether the pixel cache will be generated for faster display
          and processing of the mosaic dataset.NO_PIXEL_CACHE-The pixel cache
          will not be generated. This is the
          default.USE_PIXEL_CACHE-The pixel cache will be generated.
      cache_location {Folder / String}:
          The location of the pixel cache. If no location is defined, the cache
          will be written to
          C:\Users\<Username>\AppData\Local\ESRI\rasterproxies\. Once the
          location is defined, you do not need to redefine the
          path when adding new rasters to the mosaic dataset. You do need to
          check theparameter (enable_pixel_cache = "USE_PIXEL_CACHE" in Python)
          when adding the new data. Enable Pixel Cache

        """