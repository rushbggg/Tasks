# state file generated using paraview version 5.12.0-RC1
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 12

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1153, 778]
renderView1.AxesGrid = 'Grid Axes 3D Actor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-1.1058589153296086, 7.59940840984502, 2.5681150535198096]
renderView1.CameraViewUp = [0.07900639839203122, -0.30881123355501894, 0.9478362786068844]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.7320508075688772
renderView1.LegendGrid = 'Legend Grid Actor'
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1153, 778)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
oceandata_temperaturenc = NetCDFReader(registrationName='oceandata_temperature.nc', FileName=['E:\pyproject\task\task1\oceandata_temperature.nc'])
oceandata_temperaturenc.Dimensions = '(lat, lon)'

# create a new 'Clip'
southernHemisphere_si_fraction = Clip(registrationName='Southern Hemisphere_s-i_fraction', Input=oceandata_temperaturenc)
southernHemisphere_si_fraction.ClipType = 'Plane'
southernHemisphere_si_fraction.HyperTreeGridClipper = 'Plane'
southernHemisphere_si_fraction.Scalars = ['CELLS', 'analysed_sst']
southernHemisphere_si_fraction.Value = 125.49000000000004

# init the 'Plane' selected for 'ClipType'
southernHemisphere_si_fraction.ClipType.Normal = [0.0, 0.0, 1.0]

# create a new 'Clip'
sphere_temp = Clip(registrationName='sphere_temp', Input=oceandata_temperaturenc)
sphere_temp.ClipType = 'Sphere'
sphere_temp.HyperTreeGridClipper = 'Plane'
sphere_temp.Scalars = ['CELLS', 'analysed_sst']
sphere_temp.Value = 125.49000000000004

# create a new 'Clip'
southernHemisphere_temp = Clip(registrationName='Southern Hemisphere_temp', Input=oceandata_temperaturenc)
southernHemisphere_temp.ClipType = 'Plane'
southernHemisphere_temp.HyperTreeGridClipper = 'Plane'
southernHemisphere_temp.Scalars = ['CELLS', 'analysed_sst']
southernHemisphere_temp.Value = 125.49000000000004

# init the 'Plane' selected for 'ClipType'
southernHemisphere_temp.ClipType.Normal = [0.0, 0.0, 1.0]

# create a new 'Clip'
northernHemisphere_si_fraction = Clip(registrationName='Northern Hemisphere_s-i_fraction', Input=oceandata_temperaturenc)
northernHemisphere_si_fraction.ClipType = 'Plane'
northernHemisphere_si_fraction.HyperTreeGridClipper = 'Plane'
northernHemisphere_si_fraction.Scalars = ['CELLS', 'analysed_sst']
northernHemisphere_si_fraction.Value = 125.49000000000004

# init the 'Plane' selected for 'ClipType'
northernHemisphere_si_fraction.ClipType.Normal = [0.0, 0.0, -1.0]

# create a new 'Clip'
northernHemisphere_temp = Clip(registrationName='Northern Hemisphere_temp', Input=oceandata_temperaturenc)
northernHemisphere_temp.ClipType = 'Plane'
northernHemisphere_temp.HyperTreeGridClipper = 'Plane'
northernHemisphere_temp.Scalars = ['CELLS', 'analysed_sst']
northernHemisphere_temp.Value = 125.49000000000004

# init the 'Plane' selected for 'ClipType'
northernHemisphere_temp.ClipType.Normal = [0.0, 0.0, -1.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from oceandata_temperaturenc
oceandata_temperaturencDisplay = Show(oceandata_temperaturenc, renderView1, 'StructuredGridRepresentation')

# get 2D transfer function for 'analysed_sst'
analysed_sstTF2D = GetTransferFunction2D('analysed_sst')

# get color transfer function/color map for 'analysed_sst'
analysed_sstLUT = GetColorTransferFunction('analysed_sst')
analysed_sstLUT.TransferFunction2D = analysed_sstTF2D
analysed_sstLUT.RGBPoints = [-54.52999999999997, 0.231373, 0.298039, 0.752941, 125.49000000000004, 0.865003, 0.865003, 0.865003, 305.51000000000005, 0.705882, 0.0156863, 0.14902]
analysed_sstLUT.ColorSpace = 'HSV'
analysed_sstLUT.ScalarRangeInitialized = 1.0
analysed_sstLUT.EnableOpacityMapping = 1

# get opacity transfer function/opacity map for 'analysed_sst'
analysed_sstPWF = GetOpacityTransferFunction('analysed_sst')
analysed_sstPWF.Points = [-54.52999999999997, 0.0, 0.5, 0.0, 15.010436058044434, 0.4285714626312256, 0.5, 0.0, 99.1319351196289, 0.7008928656578064, 0.5, 0.0, 198.9561004638672, 0.9017857313156128, 0.5, 0.0, 305.51000000000005, 1.0, 0.5, 0.0]
analysed_sstPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
oceandata_temperaturencDisplay.Representation = 'Surface'
oceandata_temperaturencDisplay.ColorArrayName = ['CELLS', 'analysed_sst']
oceandata_temperaturencDisplay.LookupTable = analysed_sstLUT
oceandata_temperaturencDisplay.SelectTCoordArray = 'None'
oceandata_temperaturencDisplay.SelectNormalArray = 'None'
oceandata_temperaturencDisplay.SelectTangentArray = 'None'
oceandata_temperaturencDisplay.OSPRayScaleFunction = 'Piecewise Function'
oceandata_temperaturencDisplay.Assembly = ''
oceandata_temperaturencDisplay.SelectOrientationVectors = 'None'
oceandata_temperaturencDisplay.ScaleFactor = 0.2
oceandata_temperaturencDisplay.SelectScaleArray = 'None'
oceandata_temperaturencDisplay.GlyphType = 'Arrow'
oceandata_temperaturencDisplay.GlyphTableIndexArray = 'None'
oceandata_temperaturencDisplay.GaussianRadius = 0.01
oceandata_temperaturencDisplay.SetScaleArray = [None, '']
oceandata_temperaturencDisplay.ScaleTransferFunction = 'Piecewise Function'
oceandata_temperaturencDisplay.OpacityArray = [None, '']
oceandata_temperaturencDisplay.OpacityTransferFunction = 'Piecewise Function'
oceandata_temperaturencDisplay.DataAxesGrid = 'Grid Axes Representation'
oceandata_temperaturencDisplay.PolarAxes = 'Polar Axes Representation'
oceandata_temperaturencDisplay.ScalarOpacityFunction = analysed_sstPWF
oceandata_temperaturencDisplay.ScalarOpacityUnitDistance = 0.03422622178043525
oceandata_temperaturencDisplay.SelectInputVectors = [None, '']
oceandata_temperaturencDisplay.WriteLog = ''

# setup the color legend parameters for each legend in this view

# get color legend/bar for analysed_sstLUT in view renderView1
analysed_sstLUTColorBar = GetScalarBar(analysed_sstLUT, renderView1)
analysed_sstLUTColorBar.Title = 'analysed_sst'
analysed_sstLUTColorBar.ComponentTitle = ''

# set color bar visibility
analysed_sstLUTColorBar.Visibility = 1

# show color legend
oceandata_temperaturencDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation scene

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.ViewModules = renderView1
animationScene1.Cues = timeAnimationCue1
animationScene1.AnimationTime = 1356868800.0
animationScene1.StartTime = 1356868800.0
animationScene1.EndTime = 1356868801.0

# ----------------------------------------------------------------
# restore active source
SetActiveSource(None)
# ----------------------------------------------------------------


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://kitware.github.io/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------