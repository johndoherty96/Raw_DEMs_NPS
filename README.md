<h1>Precoessing Raw DEM's for User Specified National Parks</h1>

<h2>Description</h2>
For this project, I developed a Python scripting tool designed for ArcGIS Pro to process raw Digital Elevation Models (DEMs) and clip them to the boundaries of a user-specified National Park. The script generates hillshade and slope raster datasets, as well as a contour vector dataset. These output datasets are then reprojected to match the spatial reference system of the boundaries dataset.
<br />

<h2>Languages and Environments Used</h2>

- <b>Python</b> 
- <b>ArcGIS Pro</b>
- <b>Pyscripter</b>

<h2>Walk-through:</h2>

<p align="center">
Launch Scripting Tool & Input Boundaries and DEM Band: <br/>
<img src="https://imgur.com/nOWgLaw.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
<p align="center">
Specify the State and National Park. Here we are Focusing on Yosemite in Califonia: <br/>
<img src="https://imgur.com/F53AhcS.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
<p align="center">
Here we can Observe our Raw DEM and National Park Boundaries: <br/>
<img src="https://imgur.com/pe7u2T8.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
<p align="center">
When the Tool is Run, we are provided with a clipped & Reprojected Hillshade Raster: <br/>
<img src="https://imgur.com/7ZxSFFj.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
<p align="center">
A clipped & Reprojected Slope Raster: <br/>
<img src="https://imgur.com/aeAzkyF.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
<p align="center">
And a clipped & Reprojected Vector Contour: <br/>
<img src="https://imgur.com/Vvd6LWH.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />


<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
