# Generated documentation for module arcpy.aviation


class UpdateAviationAnno(object):
    """
    Batch updates Aviation-specific annotation layers to streamline chart production and finishing.
    """

    @property
    def description(self) -> str:
        return """

        UpdateAviationAnno_aviation(in_map, in_anno_layers;in_anno_layers..., {aoi_features}, {apply_scaling})

        Batch updates Aviation-specific annotation layers to streamline chart
        production and finishing.

     INPUTS:
      in_map (Map):
          The input value for this tool will update the domains for the
          in_anno_layers parameter value.
      in_anno_layers (Value Table):
          The feature-linked annotation layers and the specified sublayers that
          will be updated.Annotation Layers-The input feature-linked annotation
          layers.Sublayers-The sublayers that determine which annotation
          features will
          be processed.
      aoi_features {Feature Layer}:
          The AOI boundary within which features will be processed.
      apply_scaling {Boolean}:
          Specifies whether scaling will be applied to annotation features based
          on linked cartographic feature reference scale and annotation
          reference scale. The formula for scaling is ((
          LinkedFeature.ReferenceScale * value) / AnnotationLayer.ReferenceScale
          ).SCALED-No annotation scaling will be applied. This is the
          default.NOT_SCALED-Annotation scaling will be applied.

        """