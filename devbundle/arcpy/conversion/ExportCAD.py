# Generated documentation for module arcpy.conversion


class ExportCAD(object):
    """
    Exports features to new or existing CAD files based on one or more input feature layers or feature classes.
    """

    @property
    def description(self) -> str:
        return """

        ExportCAD_conversion(in_features;in_features..., Output_Type, Output_File, {Ignore_FileNames}, {Append_To_Existing}, {Seed_File})

        Exports features to new or existing CAD files based on one or more
        input feature layers or feature classes.

     INPUTS:
      in_features (Feature Layer):
          A collection of feature classes and feature layers whose spatial
          reference and geometry will be exported to one or more CAD files. Both
          the feature geometry and the feature attributes will be added to
          AutoCAD formatted files.
      Output_Type (String):
          Specifies the CAD platform and file version that will be used for new
          output CAD files. Multiple versions of CAD software may share one file
          format version for multiple releases. The choices specify the file
          format version, not necessarily the software version that may still
          use a previous file format version.DGN_V8-The output type will be
          Microstation DGN.DWG_R2018-The output
          type will be DWG version 2018. This is the
          default.DWG_R2013-The output type will be DWG version
          2013.DWG_R2010-The output type will be DWG version 2010.DWG_R2007-The
          output type will be DWG version 2007.DWG_R2005-The output type will be
          DWG version 2005.DWG_R2004-The output type will be DWG version
          2004.DWG_R2000-The output type will be DWG version 2000.DWG_R14-The
          output type will be DWG version 14.DXF_R2018-The output type will be
          DXF version 2018.DXF_R2013-The output type will be DXF version
          2013.DXF_R2010-The output type will be DXF version 2010.DXF_R2007-The
          output type will be DXF version 2007.DXF_R2005-The output type will be
          DXF version 2005.DXF_R2004-The output type will be DXF version
          2004.DXF_R2000-The output type will be DXF version 2000.DXF_R14-The
          output type will be DXF version 14.
      Ignore_FileNames {Boolean}:
          Specifies whether valid paths included in thefield of input
          features will be ignored.
          DocPathIgnore_Filenames_in_Tables-Valid paths will be ignored and the
          output
          of all entities will be added to the Output_File parameter value. This
          is the default.Use_Filenames_in_Tables-Valid paths will be used so
          that each new CAD
          entity will be written to the file specified by that field value.
      Append_To_Existing {Boolean}:
          Specifies whether the output will be appended to an existing CAD file.
          This allows you to add information to a CAD file on
          disk.Append_To_Existing_Files-Entities will be appended to an output
          CAD
          file if one exists. The existing CAD file content will be
          retained.Overwrite_Existing_Files-If an output CAD file exists, it
          will be
          overwritten. This is the default.
      Seed_File {CAD Drawing Dataset}:
          An existing CAD drawing whose contents and document and layer
          properties will be used as a seed file when output CAD files are
          created. The CAD platform and format version of the seed file
          overrides the value specified by the Output_Type parameter. If
          appending to existing CAD files, the seed drawing is ignored.

     OUTPUTS:
      Output_File (CAD Drawing Dataset):
          The path of the output CAD drawing file. This path will be
          overridden by any valid file paths included as field values in the
          input feature's field or alias field namedunless the Ignore_FileNames
          parameter is set to Ignore_Filenames_in_Tables. DocPath

        """