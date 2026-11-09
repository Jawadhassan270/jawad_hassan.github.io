# Parametric Servo Shaft Coupler

Mechanical design by Jawad Hassan. A cylindrical coupler connecting a servo spline (including SG90 / SG90TP) to a round or D-flat output shaft.

## Files
- `servo_shaft_coupler.scad`: editable OpenSCAD source.
- `STL/`: standard ready-to-print presets generated automatically by GitHub Actions.

## Standard presets
SG90TP, 6 mm or 5 mm output shafts, round or D-shaped, 12 mm outer diameter, 24 mm total length.

## Customize
Use the [portfolio configurator](../../servo-coupler.html) to configure dimensions and download a customized `.scad` model. Open in free OpenSCAD, press F6, then File → Export → STL. **Custom STL rendering does not run in GitHub Pages; the online configurator exports a parametrized OpenSCAD source.**

## Assembly and cautions
Attach the coupler to the servo through its axial screw before inserting the output shaft. Use a suitable radial set screw for locking the shaft. The radial bore is plain, not threaded: tap it or adapt the design for a threaded insert. Verify servo spline size, screw-head clearance, and shaft tolerances on your actual hardware before printing or loading the part. 3D-printed parts are not rated for a particular torque or safety-critical use.

## Spline licensing
The spline tooth profile is adapted from Matthias Mezger's *Customizable Servo Arm*, licensed LGPL-2.1-or-later. The adapted profile remains subject to that license; retain this attribution when redistributing it. This project does not claim to relicense the upstream spline.
