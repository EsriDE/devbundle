# Generated documentation for module arcpy.rm


class ReconstructSurface(object):
    """
    Generates a digital surface model (DSM), true orthos, DSM meshes, 3D meshes, and point clouds from adjusted imagery.
    """

    @property
    def description(self) -> str:
        return """

        ReconstructSurface_rm(in_mosaic_dataset, recon_folder, {recon_options}, {scenario}, {fwd_overlap}, {swd_overlap}, {quality}, {products;products...}, {cell_size}, {aoi}, {waterbody_features}, {correction_features})

        Generates a digital surface model (DSM), true orthos, DSM meshes, 3D
        meshes, and point clouds from adjusted imagery.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The adjusted input mosaic dataset.
      recon_folder (Folder):
          The output dataset folder.
      recon_options {File / String}:
          A .json file or JSON string that specifies the values for the tool
          parameters.If this parameter value is provided, the properties of the
          .json file
          or JSON string will set the default values for the remaining optional
          parameters. See the Usages section for a list of options.
      scenario {String}:
          Specifies the type of imagery that will be used to generate the output
          products.DRONE-The input imagery will be defined as having been
          acquired with
          drones or terrestrial cameras.AERIAL_NADIR-The input imagery will be
          defined as having been acquired
          with large, photogrammetric camera systems.AERIAL_OBLIQUE-The input
          imagery will be defined as having been
          acquired with oblique camera systems.SATELLITE-The input imagery will
          be defined as having been acquired
          with a satellite.
      fwd_overlap {Long}:
          The forward (in-strip) overlap percentage that will be used between
          the images. The default is 60.This parameter is enabled when the
          scenario parameter is set to
          AERIAL_NADIR.
      swd_overlap {Long}:
          The sideward (cross-strip) overlap percentage that will be used
          between the images. The default is 30.This parameter is enabled when
          the scenario parameter is set to
          AERIAL_NADIR.
      quality {String}:
          Specifies the quality of the final product.ULTRA-The highest level of
          density point cloud will be used. Input
          images will be used at their original (full) resolution.HIGH-The high
          level of density point cloud will be used. Input images
          will be downsampled two times.
      products {String}:
          Specifies the products that will be generated.DSM-A DSM will be
          generated. This option will be specified by default
          when the scenario parameter is set to AERIAL_NADIR or
          SATELLITE.TRUE_ORTHO-The imagery will be orthorectified. This option
          will be
          specified by default when the scenario parameter is set to
          AERIAL_NADIR.DSM_MESH-A DSM mesh will be generated. This option will
          be specified
          by default when the scenario parameter is set to AERIAL_NADIR or
          SATELLITE.POINT_CLOUD-An image point cloud will be generated. This
          option will
          be specified by default when the scenario parameter is set to DRONE or
          AERIAL_OBLIQUE.MESH-A 3D mesh will be generated. This option will be
          selected by
          specified when the scenario parameter is set to DRONE or
          AERIAL_OBLIQUE.
      cell_size {Double / String}:
          The cell size of the output product.
      aoi {Feature Layer / File / String}:
          The area of interest that will be used to select images for
          processing. The area of interest can be computed automatically or
          defined using an input polygon.If the value contains 3D geometries,
          the z-component will be ignored.
          If the value includes overlapping features, the union of these
          features will be computed.
      waterbody_features {Feature Layer / File / String}:
          A polygon that will define the extent of large water bodies. The value
          must be a 3D feature.
      correction_features {Feature Layer / File / String}:
          A polygon that will define the extent of all surfaces that are not
          water bodies. The value must be a 3D feature.

        """