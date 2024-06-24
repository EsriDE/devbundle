# Generated documentation for module arcpy.oi


class CreateOrientedImageryDataset(object):
    """
    Creates an empty oriented imagery dataset in a geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        CreateOrientedImageryDataset_oi(out_dataset_path, out_dataset_name, spatial_reference, {elevation_source}, {constant_elevation}, {dem}, {lod}, {raster_function}, {template;template...}, {out_dataset_alias}, {config_keyword}, {has_z})

        Creates an empty oriented imagery dataset in a geodatabase.

     INPUTS:
      out_dataset_path (Workspace / Feature Dataset):
          The geodatabase in which the output oriented imagery dataset will be
          created. This workspace must already exist.
      out_dataset_name (String):
          The name of the oriented imagery dataset that will be created.
      spatial_reference (Spatial Reference):
          The spatial reference of the output oriented imagery dataset.
      elevation_source {String}:
          Specifies the elevation source for the dataset.DEM-The elevation
          source will be a digital elevation model that is a
          dynamic image service or a tile image service.CONSTANT_ELEVATION-The
          elevation source will be a constant ground
          elevation value for the entire dataset.
      constant_elevation {Double}:
          The constant ground elevation value (in meters) for the entire
          dataset.This parameter is enabled when the elevation_source parameter
          value is
          specified as CONSTANT_ELEVATION.
      dem {Image Service}:
          The name of the input digital elevation model. A dynamic image service
          or a tile image service can be used as the digital elevation
          model.This parameter is enabled when the elevation_source parameter
          value is
          specified as DEM.
      lod {String}:
          The scale in a tiling schema. The scale represents the zoom level
          value. Each successive level improves resolution and map scale by
          double when compared to the previous level.This parameter is enabled
          when the dem parameter value is a tile image
          service.
      raster_function {String}:
          The raster function processing template that will be applied to the
          image service.This parameter is enabled when the dem parameter value
          is a dynamic
          image service.
      template {Table View}:
          The oriented imagery dataset or table that will be used as a template
          to define the attribute fields of the new oriented imagery dataset.
      out_dataset_alias {String}:
          The alternate name for the oriented imagery dataset that will be
          created.
      config_keyword {String}:
          The configuration keyword for the data. This parameter applies to
          enterprise data only. It determines the storage parameters of the
          database table.
      has_z {String}:
          Specifies whether the output oriented imagery dataset will have
          elevation values (z-values).DISABLED-The output oriented imagery
          dataset will not have z-values.
          This is the defaultENABLED-The output oriented imagery dataset will
          have z-values.

        """