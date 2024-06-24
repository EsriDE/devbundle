# Generated documentation for module arcpy.indoors


class ImportBIMToIndoorDataset(object):
    """
    Imports features from a Revit file (.rvt) to an Indoors workspace that conforms to the ArcGIS Indoors Information Model. The output of this tool can be used to create floor-aware maps and scenes, as well as to generate an indoor network for routing.
    """

    @property
    def description(self) -> str:
        return """

        ImportBIMToIndoorDataset_indoors(in_bim_floorplan_layer, target_unit_features, target_detail_features, target_level_features, target_facility_features, facility_id, facility_name, ground_floor_name, {floorplan_polygon_use_type_field}, {floors_to_import;floors_to_import...}, {area_unit_of_measure}, {in_bim_rooms_layer;in_bim_rooms_layer...}, {room_properties_mapping}, {allow_insert_new_facility}, {design_options;design_options...}, {target_unit3d_features}, {target_detail3d_features}, {target_facility3d_features}, {linked_files;linked_files...})

        Imports features from a Revit file (.rvt) to an Indoors workspace that
        conforms to the ArcGIS Indoors Information Model. The output of this
        tool can be used to create floor-aware maps and scenes, as well as to
        generate an indoor network for routing.

     INPUTS:
      in_bim_floorplan_layer (Polygon):
          The Floorplan_Polygon feature layer from the source .rvt file that has
          been added to the current map.
      target_unit_features (Feature Layer):
          The target Units feature layer, feature class, or feature service that
          conforms to the Indoors model and resides in the same workspace as the
          target Facilities, Levels, and Details features.
      target_detail_features (Feature Layer):
          The target Details feature layer, feature class, or feature service
          that conforms to the Indoors model and resides in the same workspace
          as the target Facilities, Levels, and Units features.
      target_level_features (Feature Layer):
          The target Levels feature layer, feature class, or feature service
          that conforms to the Indoors model and resides in the same workspace
          as the target Facilities, Units, and Details features.
      target_facility_features (Feature Layer):
          The target Facilities feature layer, feature class, or feature service
          that conforms to the Indoors model and resides in the same workspace
          as the target Levels, Units, and Details features.
      facility_id (String):
          The unique facility ID that will be assigned to the output Indoors
          features. The facility ID cannot contain spaces.
      facility_name (String):
          The common name of the building.
      ground_floor_name (String):
          The ground floor of the building. The vertical order of the levels is
          derived from this value. Any levels with an elevation that is less
          than the specified ground floor will be assigned a negative vertical
          order.
      floorplan_polygon_use_type_field {String}:
          The field from the Floorplan_Polygon feature layer that will
          be used to populate thefield for the target unit features. If no field
          is provided, thefield value from the Floorplan_Polygon layer will be
          used. USE_TYPERoomName
      floors_to_import {String}:
          The floors in the input .rvt file that will be imported to the target
          features. If no floors are provided, all floors except roof elements
          will be imported.
      area_unit_of_measure {String}:
          Specifies the unit of measure that will be used for the area fields in
          the Levels and Units feature classes.SQUARE_METERS-The area unit will
          be square meters.SQUARE_FEET-The area
          unit will be square feet. This is the default.
      in_bim_rooms_layer {Feature Layer}:
          The Rooms layer from the Architectural dataset in the input
          .rvt file. This layer will be used to obtain extended field values
          that can be mapped to existing fields in the Units feature class using
          theparameter. Room Properties Mapping
      room_properties_mapping {Field Mappings}:
          Controls which attribute fields in the Units feature class will be
          populated with field values from the input .rvt Rooms layer. The
          fields must exist before running the tool. It is recommended that you
          map fields from the input .rvt Rooms layer to fields from the Units
          feature class that have the same field type.
      allow_insert_new_facility {Boolean}:
          Specifies whether a building from the input .rvt file will be imported
          if an intersection is detected between that building's floor plan and
          an existing Facilities feature in the target facility features.
          NO_ALLOW_INSERT_NEW_FACILITY-The tool tests whether the input
          BIM floor plan polygon intersects any existing facility polygon in the
          target facility features. If an intersection is detected, the tool
          checks whether the specified facility_id and facility_name parameter
          values match theandfield values of the intersecting Facilities
          feature. If the values match, the tool updates the existing facility.
          If the values do not match, the tool issues a warning message and
          stops running. This is the default.
          FACILITY_IDNAMEALLOW_INSERT_NEW_FACILITY-The tool does not test
          whether the input
          BIM floor plan polygon intersects any existing facility polygon in the
          target facility features. You can use this option to import a building
          that overlaps or touches an existing facility.
      design_options {String}:
          The Revit design options in the input .rvt file that will be included
          when importing features. If no value is specified, only the main model
          will be imported. This parameter is enabled when the input .rvt file
          includes Revit design options.
      target_unit3d_features {Feature Layer}:
          The target 3D Units feature layer, feature class, or feature service
          that conforms to the Indoors model. Multipatch unit features will be
          created in the target 3D units layer that represent the base of each
          room in the input .rvt file.
      target_detail3d_features {Feature Layer}:
          The target 3D Details feature layer, feature class, or feature service
          that conforms to the Indoors model. Multipatch detail features will be
          created in the target 3D details layer from the following categories
          in the input .rvt file: Doors, Ramps, Stairs, Stair supports, Stair
          Landings, Columns, Structural Columns, Walls, Windows, Cornices, and
          Curtain Wall Panels.
      target_facility3d_features {Feature Layer}:
          The target 3D Facilities feature layer, feature class, or feature
          service that conforms to the Indoors model. A multipatch facility
          feature will be created in the target 3Dfacilities layer from the
          ExteriorShell category in the input .rvt file.
      linked_files {String}:
          The linked Revit files that are associated with the input .rvt file of
          the same building. Selected linked files will be imported to the
          Indoors model along with the main model. If no value is specified,
          only the main model will be imported. This parameter is only enabled
          when the input .rvt file includes linked Revit files.

        """