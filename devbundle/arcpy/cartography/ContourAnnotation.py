# Generated documentation for module arcpy.cartography


class ContourAnnotation(object):
    """
    Creates annotation for contour features.
    """

    @property
    def description(self) -> str:
        return """

        ContourAnnotation_cartography(in_features, out_geodatabase, contour_label_field, reference_scale_value, out_layer, contour_color, {contour_type_field}, {contour_alignment}, {enable_laddering})

        Creates annotation for contour features.

     INPUTS:
      in_features (Feature Layer):
          The contour line feature class for which the annotation will be
          created.
      out_geodatabase (Workspace / Feature Dataset):
          The workspace where the output feature classes will be saved. The
          workspace can be an existing geodatabase or an existing feature
          dataset.
      contour_label_field (Field):
          The field in the input layer attribute table on which the annotation
          text will be based.
      reference_scale_value (Double):
          The scale that will be used as a reference for the annotation. This
          sets the scale on which all symbol and text sizes in the annotation
          will be based.
      contour_color (String):
          Specifies the color of the output contour layer and annotation
          features.BLACK-The output contour layer and annotation features will
          be drawn
          in black. This is the default.BROWN-The output contour layer and
          annotation features will be drawn
          in brown.BLUE-The output contour layer and annotation features will be
          drawn in
          blue.
      contour_type_field {Field}:
          The field in the input layer attribute table containing a value for
          the type of contour feature. An annotation class will be created for
          each type value.
      contour_alignment {String}:
          Specifies how the annotation will be aligned to contour elevations.
          The annotation can be aligned to the contour elevations so that the
          top of the text is always placed uphill or downhill. These options
          allow the annotation to be placed upside down. The contour annotation
          can also be aligned to the page, ensuring that the text is never
          placed upside down.PAGE-The annotation will be aligned to the page,
          ensuring that the
          text is never placed upside down. This is the default.UPHILL-The
          annotation will be aligned to the contour elevations so
          that the top of the text is always placed uphill. This option allows
          the annotation to be placed upside down.DOWNHILL-The annotation will
          be aligned to the contour elevations so
          that the top of the text is always placed downhill. This option allows
          the annotation to be placed upside down.
      enable_laddering {Boolean}:
          Specifies whether annotation will be placed in ladders. Placing
          annotation in ladders will place the text so it appears to step up and
          step down the contours in a straight path. These ladders will run from
          the top of a hill to the bottom, will not cross each other, will
          belong to a single slope, and will not cross any other
          slope.ENABLE_LADDERING-Annotation will step up and down the contours
          in a
          straight path.NOT_ENABLE_LADDERING-Annotation will not be placed up
          and down the
          contours in a straight path. This is the default.

     OUTPUTS:
      out_layer (Group Layer):
          The group layer that will contain the contour layer, the
          annotation, and the mask layer. When working in thepane, you can use
          the Save To Layer File tool to write the output group layer to a layer
          file. When using ArcGIS Pro, the tool adds the group layer to the
          display if theoption is checked on thetab on thedialog box. The group
          layer that is created is temporary and will not persist after the
          session ends unless the document is saved. CatalogAdd output
          datasets to an open mapGeoprocessingOptions

        """