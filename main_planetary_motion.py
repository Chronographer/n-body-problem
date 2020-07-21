import planetaryData
import planetObjectGenerator
import nBodyExperimental
from vpython import *


title = ""  # Put a title here if you want it, or leave it as an empty string to free up ~25 extra pixels vertically to display the animation with.
scene = canvas(title=title, width=1200, height=735, forward=vector(-0, -0, -1))
axisLength = 1
maxTrailLength = -1  # To remove the limit set this to -1, to remove the trail entirely, set this to -2. Otherwise set to a positive integer to taste. Can also be set individually for each planet object, if desired.

timeStep = 0.001 * planetaryData.earthPeriod
targetFrameRate = 30
endTime = 50

vPlot = False
numPlot = True

sunObject = planetObjectGenerator.planet(planetaryData.getPlanetData("sun"), maxTrailLength)
earthObject = planetObjectGenerator.planet(planetaryData.getPlanetData('earth'), maxTrailLength)
marsObject = planetObjectGenerator.planet(planetaryData.getPlanetData('mars'), maxTrailLength)
jupiterObject = planetObjectGenerator.planet(planetaryData.getPlanetData('jupiter'), maxTrailLength)
saturnObject = planetObjectGenerator.planet(planetaryData.getPlanetData('saturn'), maxTrailLength)
uranusObject = planetObjectGenerator.planet(planetaryData.getPlanetData('uranus'), maxTrailLength)
neptuneObject = planetObjectGenerator.planet(planetaryData.getPlanetData('neptune'), maxTrailLength)
planetObjectList = [sunObject, earthObject, marsObject, jupiterObject, saturnObject, uranusObject, neptuneObject]

nBodyExperimental.run(planetObjectList, targetFrameRate, timeStep, endTime)
