# Generated documentation for module arcpy.indoors


class ImportIFCToIndoorDataset(object):
    """
    Imports features from an .ifc file to an indoor dataset that conforms to the ArcGIS Indoors Information Model. The output of this tool can be used to create floor-aware maps and scenes, as well as to generate an indoor network for routing.
    """

    @property
    def description(self) -> str:
        return """

        ImportIFCToIndoorDataset_indoors(in_bim_file_workspace, target_facility_features, facility_name, target_level_features, target_unit_features, target_detail_features, ground_floor_name, {unit_properties_mapping}, {load_floorplan_layers}, {in_floorplan_footprint}, {in_floorplan_polygon}, {in_floorplan_polyline}, {target_unit3d_features}, {target_detail3d_features}, {target_facility3d_features}, {load_roofs})

        Imports features from an .ifc file to an indoor dataset that conforms
        to the ArcGIS Indoors Information Model. The output of this tool can
        be used to create floor-aware maps and scenes, as well as to generate
        an indoor network for routing.

     INPUTS:
      in_bim_file_workspace (BIM File Workspace):
          The input IFC workspace.
      target_facility_features (Feature Layer):
          The target Facilities feature layer, feature class, or feature service
          that conforms to the Indoors model and resides in the same workspace
          as the target Levels, Units, and Details features.
      facility_name (String):
          The common name of the building. If a feature with the same name
          exists in the target Facilities layer, it will be updated, along with
          all of the associated Levels, Units, and Details features.
      target_level_features (Feature Layer):
          The target Levels feature layer, feature class, or feature service
          that conforms to the Indoors model and resides in the same workspace
          as the target Facilities, Units, and Details features.
      target_unit_features (Feature Layer):
          The target Units feature layer, feature class, or feature service that
          conforms to the Indoors model and resides in the same workspace as the
          target Facilities, Levels, and Details features.
      target_detail_features (Feature Layer):
          The target Details feature layer, feature class, or feature service
          that conforms to the Indoors model and resides in the same workspace
          as the target Facilities, Levels, and Units features.
      ground_floor_name (String):
          The ground floor of the building. The vertical order of the levels is
          derived from this value. Any levels with an elevation that is less
          than the specified ground floor will be assigned a negative vertical
          order.
      unit_properties_mapping {Field Mappings}:
          Controls which attribute fields in the Units layer will be populated
          with field values from the input IFC Spaces layer. The fields must
          exist before running the tool. It is recommended that you map fields
          from the input IFC Spaces layer to fields from the Units layer that
          have the same field type.
      load_floorplan_layers {Boolean}:
          Specifies whether features will be loaded from input floor plan layers
          created by the Extract BIM File Floorplan
          tool.LOAD_FROM_FLOORPLAN_LAYERS-Features will be loaded from the input
          floor plan layers created by the Extract BIM File Floorplan tool. Any
          selections set on the input layers will be
          honored.NO_LOAD_FROM_FLOORPLAN_LAYERS-Features will be loaded from the
          .ifc
          file. All levels will be loaded and no selections will be honored.
          This is the default.
      in_floorplan_footprint {Feature Layer}:
          The Floorplan Footprint feature layer created using the Extract BIM
          File Floorplan tool. Features in this layer will be used to create
          features in the target Facilities layer.
      in_floorplan_polygon {Feature Layer}:
          The Floorplan Polygon feature layer created using the Extract BIM File
          Floorplan tool. Features in this layer will be used to create features
          in the target Levels and Units layers.
      in_floorplan_polyline {Feature Layer}:
          The Floorplan Polyline feature layer created using the Extract BIM
          File Floorplan tool. Features in this layer will be used to create
          features in the target details layer.
      target_unit3d_features {Feature Layer}:
          The target Units3D feature layer, feature class, or feature service
          that conforms to the Indoors model. Multipatch unit features will be
          created in the target Units3D layer from the Spaces category of the
          input .ifc file.
      target_detail3d_features {Feature Layer}:
          The target Details3D feature layer, feature class, or feature service
          that conforms to the Indoors model. Multipatch detail features will be
          created in the target Details3D layer from the following categories in
          the input .ifc file: Doors, Columns, Walls, Ramps, Stairs, Windows,
          Curtain Walls, and Structural Columns.
      target_facility3d_features {Feature Layer}:
          The target 3D Facilities feature layer, feature class, or feature
          service that conforms to the Indoors model. A multipatch facility
          feature will be created in the target Facilities3D layer from the
          ExteriorShell category in the input .ifc file.
      load_roofs {Boolean}:
          Specifies whether roof features will be imported as levels
          features.LOAD_ROOFS-Roof elements will be loaded from the input .ifc
          file and
          used along with floors features to create levels features in the
          Indoors workspace.NO_LOAD_ROOFS-Roof features will not be loaded from
          the input .ifc
          file. This is the default.

        """