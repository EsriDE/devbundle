# Generated documentation for module arcpy.nd


class CreateDiagramLayerDefinition(object):
    """
    Creates a diagram layer definition for the input diagram template using the settings of the network feature layers in the active map.
    """

    @property
    def description(self) -> str:
        return """

        CreateDiagramLayerDefinition_nd(in_utility_network, template_name, {system_junctions}, {connectivity_associations}, {structural_attachments}, {reduction_edges}, {point_subLayers;point_subLayers...}, {polygon_subLayers;polygon_subLayers...}, {junction_object_point_subLayers;junction_object_point_subLayers...}, {edge_object_polyline_subLayers;edge_object_polyline_subLayers...}, {overwrite_all_layers})

        Creates a diagram layer definition for the input diagram template
        using the settings of the network feature layers in the active map.

     INPUTS:
      in_utility_network (Utility Network Layer / Trace Network Layer):
          The utility network or trace network layer in the active map.
      template_name (String):
          The name of the diagram template that will be modified.
      system_junctions {Boolean}:
          Specifies whether system junctions and system junction objects will be
          represented in the diagrams based on the specified template.SHOW-The
          system junctions along the network lines and the system
          junction objects along the network edge objects will be represented in
          the diagrams by a System Junction layer and a System Junction Objects
          layer, respectively. This is the default.HIDE-System junctions and
          system junction objects will not be
          represented in the diagrams.
      connectivity_associations {Boolean}:
          Specifies whether connectivity associations will be represented in the
          diagrams based on the specified template.SHOW-Connectivity
          associations will be represented in the diagrams by
          the Connectivity Associations layer. This is the
          default.HIDE-Connectivity associations will not be represented in the
          diagrams.
      structural_attachments {Boolean}:
          Specifies whether structural attachment associations will be
          represented in the diagrams based on the specified
          template.SHOW-Structural attachment associations will be represented
          in the
          diagrams by the Structural Attachments layer. This is the
          default.HIDE-Structural attachment associations will not be
          represented in the
          diagrams.
      reduction_edges {Boolean}:
          Specifies whether reduction edges will be represented in the diagrams
          based on the specified template.SHOW-Reduction edges will be
          represented in the diagrams by the
          Reduction Edges layer. This is the default.HIDE-Reduction edges will
          not be represented in the diagrams.
      point_subLayers {Value Table}:
          Specifies whether layers will be added to represent container polygon
          features, network line features, or network edge objects as point
          features in the diagrams. The second column is used as follows:
          True-The layer
          will be created with subtype group layers.False-The
          layer will be created as a simple layer. This is the
          default.
      polygon_subLayers {Value Table}:
          Specifies whether layers will be added to represent container point
          features or container junction objects as polygon features in the
          diagrams. The second column is used as follows:        True-The
          layer
          will be created with subtype group layers.False-The
          layer will be created as a simple layer. This is the
          default.
      junction_object_point_subLayers {Value Table}:
          Specifies whether layers will be added to represent junction objects
          as point features in the diagrams. The second column is used as
          follows:        True-The layer
          will be created with subtype group layers.False-The
          layer will be created as a simple layer. This is the
          default.
      edge_object_polyline_subLayers {Value Table}:
          Specifies whether layers will be added to represent edge objects as
          polyline features in the diagrams. The second column is used as
          follows:        True-The layer
          will be created with subtype group layers.False-The
          layer will be created as a simple layer. This is the
          default.
      overwrite_all_layers {Boolean}:
          Specifies whether all existing layers under the diagram layer will be
          overwritten or preserved, except those in the input network map and
          explicitly specified additional sublayers.OVERWRITE_ALL-The diagram
          layer definition is initialized or entirely
          reset (overwritten) including layers in the input map and specified
          additional sublayers. This is the default.MERGE-All existing layers
          under the diagram layer will be preserved
          except those in the input network map as well as additional sublayers
          explicitly specified.

        """