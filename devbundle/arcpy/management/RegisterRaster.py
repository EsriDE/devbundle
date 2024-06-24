# Generated documentation for module arcpy.management


class RegisterRaster(object):
    """
    Automatically aligns a raster to a reference image or uses a control point file for georegistration. If the input dataset is a mosaic dataset, the tool will operate on each mosaic dataset item. To automatically register the image, the input raster and the reference raster must be in a relatively close geographic area. The tool will run faster if the raster datasets are in close alignment. You may need to create a link file, also known as a control point file, with a few links to get your input raster into the same map space.
    """

    @property
    def description(self) -> str:
        return """

        RegisterRaster_management(in_raster, register_mode, {reference_raster}, {input_link_file}, {transformation_type}, {output_cpt_link_file}, {maximum_rms_value})

        Automatically aligns a raster to a reference image or uses a control
        point file for georegistration. If the input dataset is a mosaic
        dataset, the tool will operate on each mosaic dataset item. To
        automatically register the image, the input raster and the reference
        raster must be in a relatively close geographic area. The tool will
        run faster if the raster datasets are in close alignment. You may need
        to create a link file, also known as a control point file, with a few
        links to get your input raster into the same map space.

     INPUTS:
      in_raster (Raster Dataset / Raster Layer / Mosaic Layer):
          The raster that you want to realign. Registering a mosaic dataset item
          will update that particular item within the mosaic dataset.A mosaic
          dataset item will have the path to the mosaic dataset
          followed by the Object ID of the item. For example, the first item in
          the mosaic dataset would have the following path:
          .\mosaicDataset\objectid=1.
      register_mode (String):
          Specifies the registration mode. You can either register the raster
          with a transformation or reset the transformation.REGISTER-Apply a
          geometric transformation to the input
          raster.REGISTER_MS-Register the multispectral input to the
          panchromatic
          input. This is only used for mosaic datasets that have a misalignment
          between the two.RESET-Remove the geometric transformation previously
          added by this
          tool.CREATE_LINKS-Create a link file with automatically generated
          links.
      reference_raster {Raster Dataset / Raster Layer / Image Service / Map Server / WMS Map / Mosaic Layer / Internet Tiled Layer / Map Server Layer}:
          The raster dataset that will align the input raster dataset. Leave
          this parameter empty if you want to register your multispectral mosaic
          dataset items to their associated panchromatic raster datasets.
      input_link_file {Feature Class / Text File}:
          The file that has the coordinates to link the input raster dataset
          with the reference. The input link table works with one mosaic item in
          the mosaic layer. The input must specify which item is being
          processed, either selecting the item or specifying the ObjectID in the
          input. Leave this parameter empty to register multispectral mosaic
          dataset items with the associated panchromatic raster datasets.
      transformation_type {String}:
          Specifies the method for shifting the raster dataset.POLYORDER0-This
          method uses a zero-order polynomial to shift your
          data. This is commonly used when your data is already georeferenced,
          but a small shift will better line up your data. Only one link is
          required to perform a zero-order polynomial shift.POLYSIMILARITY-This
          is a first-order transformation that attempts to
          preserve the shape of the original raster. The RMS error tends to be
          higher than other polynomial transformations because the preservation
          of shape is more important than the best fit.POLYORDER1-A first-order
          polynomial (affine) fits a flat plane to the
          input points.POLYORDER2-A second-order polynomial fits a somewhat more
          complicated
          surface to the input points.POLYORDER3-A third-order polynomial fits a
          more complicated surface to
          the input points.ADJUST-This method combines a polynomial
          transformation and uses a
          triangulated irregular network (TIN) interpolation technique to
          optimize for both global and local accuracy.SPLINE-This method
          transforms the source control points precisely to
          the target control points. In the output, the control points will be
          accurate, but the raster pixels between the control points are
          not.PROJECTIVE-This method warps lines so they remain straight. In
          doing
          so, lines that were once parallel may no longer remain parallel. The
          projective transformation is especially useful for oblique imagery,
          scanned maps, and for some imagery products.FRAME-This method uses an
          image resection algorithm on aerial images.
          The image resection algorithm refines the exterior orientation
          (perspective, omega, phi, and kappa) of the image from known ground
          control points, using a least-square fitting method. Each image must
          have at least three noncollinear points. When the input is a mosaic
          dataset, it will register the selected images one at a time.
      maximum_rms_value {Double}:
          The amount of modeled error (in pixels) that you want in the output.
          The default is 0.5, and values below 0.3 are not recommended as this
          leads to overfitting.

     OUTPUTS:
      output_cpt_link_file {Text File}:
          If specified, a text file will be written containing the links created
          by this tool. This file can be used in the Warp From File tool. The
          output link table works with one mosaic dataset item in the mosaic
          layer. The input must specify which item is being processed, either
          selecting the item or specifying the ObjectID in the input.

        """