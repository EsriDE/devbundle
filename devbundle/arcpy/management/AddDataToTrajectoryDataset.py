# Generated documentation for module arcpy.management


class AddDataToTrajectoryDataset(object):
    """
    Adds trajectory data to an existing trajectory dataset.
    """

    @property
    def description(self) -> str:
        return """

        AddDataToTrajectoryDataset_management(in_trajectory_dataset, trajectory_type, input_path;input_path..., {filter}, {sub_folder}, {aux_inputs;aux_inputs...})

        Adds trajectory data to an existing trajectory dataset.

     INPUTS:
      in_trajectory_dataset (Trajectory Layer):
          The trajectory dataset to which the data will be added.
      trajectory_type (Raster Type):
          Specifies the data type that will be added.Cryosat-2-Cryosat-2 data
          will be added.ICESat-2-ICESat-2 data will be
          added.Sentinel-3 SRAL-Sentinel-3 SRAL data will be
          added.Sentinel-6-Sentinel-6 data will be added.
      input_path (Workspace / File / WCS Coverage / Image Service / Map Server / WMS Map / Raster Catalog / Table View / Raster Layer / Mosaic Layer / Terrain Layer / LAS Dataset Layer / Layer File / WMTS Layer):
          The input files or folder. The inputs can be netCDF or HDF (.nc or
          .hdf files).
      filter {String}:
          The filter for the input data. The default will be determined by the
          trajectory_type parameter value. Custom filter criteria can also be
          provided. For example, a value of STD_ will filter files that start
          with STD_ in the file name.
      sub_folder {Boolean}:
          Specifies whether data in the input_path subfolders will be searched
          and added.SUBFOLDERS-All subfolders will be searched and the data
          added. This is
          the default.NO_SUBFOLDERS-Only the top-level folder will be searched
          and the data
          added.
      aux_inputs {Value Table}:
          The properties that are determined by the trajectory_type parameter
          value. Supported property names are ProductFilter, Frequency,
          PredefinedVariables, and Variables. For a list of supported values
          associated with each property name, see Trajectory type properties.

        """