import arcpy
import os

arcpy.env.overwriteOutput = True

# Function to calculate hillshade and slope
def hill_slope(park_rast, output, state):
    outhill = arcpy.sa.Hillshade(park_rast)
    outslope = arcpy.sa.Slope(park_rast)

    # Save the outputs inside the function
    hillshade_output_path = os.path.join(output, f"{state}_hillshade.tif")
    slope_output_path = os.path.join(output, f"{state}_slope.tif")

    outhill.save(hillshade_output_path)
    print(f"Hillshade raster saved successfully: {hillshade_output_path}")

    outslope.save(slope_output_path)
    print(f"Slope raster saved successfully: {slope_output_path}")

    return hillshade_output_path, slope_output_path

try:
    # Parameters from the script tool
    nps_boundaries = arcpy.GetParameterAsText(0)
    DEM = arcpy.GetParameterAsText(1)
    state = arcpy.GetParameterAsText(2)
    park = arcpy.GetParameterAsText(3)
    output = arcpy.GetParameterAsText(4)

    # Ensure output directory exists
    if not os.path.exists(output):
        os.makedirs(output)

    desc = arcpy.Describe(nps_boundaries)
    spatialref = desc.spatialReference

    # Print spatial reference details for debugging
    print(f"Spatial Reference: {spatialref.name}, WKID: {spatialref.factoryCode}")

    # Create a feature layer from the shapefile
    nps_boundaries_layer = "nps_boundaries_layer"
    arcpy.management.MakeFeatureLayer(nps_boundaries, nps_boundaries_layer)

    # Select by state
    state_select = arcpy.management.SelectLayerByAttribute(nps_boundaries_layer, "NEW_SELECTION", f"STATE = '{state}'")
    print(f"State {state} has been selected")

    # Select by park name within the previously selected state
    park_select = arcpy.management.SelectLayerByAttribute(state_select, "SUBSET_SELECTION", f"UNIT_NAME = '{park}'")
    print(f"Park {park} has been selected")

    outraster = os.path.join(output, f"{state}_raster.tif")

    # Clip the raster
    park_rast = arcpy.management.Clip(in_raster=DEM, out_raster=outraster, in_template_dataset=nps_boundaries_layer, clipping_geometry="ClippingGeometry", maintain_clipping_extent="NO_MAINTAIN_EXTENT")
    print(f"Raster clipped successfully: {outraster}")

    # Calculate hillshade and slope
    hillshade_output, slope_output = hill_slope(park_rast, output, state)

    # Create Contours
    contour_output_path = os.path.join(output, f"{state}_contours.shp")
    contour = arcpy.sa.Contour(park_rast, contour_output_path, 200)
    print(f"Contours created successfully: {contour_output_path}")

    pjtlist = [hillshade_output, slope_output, contour_output_path, park_rast]

    for item in pjtlist:
        if item.endswith('.tif'):
            output_reprojected = item.replace('.tif', '_reprojected.tif')
            arcpy.management.ProjectRaster(item, output_reprojected, spatialref)
            print(f"Reprojected raster saved successfully: {output_reprojected}")
        elif item.endswith('.shp'):
            output_reprojected = item.replace('.shp', '_reprojected.shp')
            arcpy.management.Project(item, output_reprojected, spatialref)
            print(f"Reprojected shapefile saved successfully: {output_reprojected}")


except arcpy.ExecuteError:
    arcpy.AddError(arcpy.GetMessages(2))

finally:
    del park_rast, park_select, state_select, nps_boundaries_layer
    arcpy.ClearWorkspaceCache_management()
