/*
  Parametric Servo-to-Shaft Coupler
  Design: Jawad Hassan
  Spline profile adapted from Matthias Mezger's Customizable Servo Arm (LGPL-2.1+).
  Units: millimetres. +Z = shaft end, -Z = servo end.
*/

/* [Servo] */
servo_preset = "SG90TP"; // [SG90TP, SG90, 3F, 2F, 1F, A1]
servo_head_gap = 0.10;
smooth_socket_depth = 1;
smooth_socket_diameter = 5.4;

/* [Body] */
coupler_diameter = 12;
coupler_length = 24;

/* [Shaft] */
shaft_type = "D-Shaped"; // [Round, D-Shaped]
shaft_diameter = 6;
shaft_clearance = 0.20;
shaft_insert_depth = 10;
shaft_flat_depth = 0.5;

/* [Radial screw] */
enable_side_screw = true;
side_screw_diameter = 2.5;
side_screw_top_offset = 5;
side_screw_angle = 0;

/* [Servo screw] */
screw_access_diameter = 5.8;
screw_clearance_diameter = 2.2;
screw_seat_thickness = 1.5;

/* [Hidden] */
$fn = 100;
eps = 0.03;
FUTABA_3F_SPLINE = [[5.92,4,1.1,2.5],[25,0.3,0.7,0.1]];
FUTABA_2F_SPLINE = [[4.5,4,1.1,2.5],[22,0.25,0.6,0.09]];
FUTABA_1F_SPLINE = [[4.0,3.75,1.1,2.4],[15,0.25,0.6,0.09]];
A15T_A1_SPLINE = [[3.9,3.2,1.1,2.4],[15,0.375,0.66,0.13]];
SG90_SPLINE = [[4.9,3.2,1.5,2.5],[21,0.25,0.65,0.25]];
SG90TP_SPLINE = [[4.7,3.2,1.5,2.5],[21,0.25,0.65,0.25]];

function servo_parameters() =
    servo_preset == "SG90TP" ? SG90TP_SPLINE :
    servo_preset == "SG90" ? SG90_SPLINE :
    servo_preset == "3F" ? FUTABA_3F_SPLINE :
    servo_preset == "2F" ? FUTABA_2F_SPLINE :
    servo_preset == "1F" ? FUTABA_1F_SPLINE :
    servo_preset == "A1" ? A15T_A1_SPLINE : SG90TP_SPLINE;

module servo_spline_2d(params, gap) {
    head = params[0];
    tooth = params[1];
    diam = head[0];
    count = tooth[0];
    tooth_h = tooth[1];
    tooth_base = tooth[2];
    tooth_tip = tooth[3];
    union() {
        circle(r=diam/2-tooth_h+0.03+gap);
        for (i=[0:count-1]) rotate(i*360/count)
            translate([0,diam/2-tooth_h+gap])
                polygon([[-tooth_base/2,0],[-tooth_tip/2,tooth_h],
                         [tooth_tip/2,tooth_h],[tooth_base/2,0]]);
    }
}

module shaft_profile_2d() {
    shaft_r = (shaft_diameter+shaft_clearance)/2;
    if (shaft_type == "Round") circle(r=shaft_r);
    else difference() {
        circle(r=shaft_r);
        translate([shaft_diameter/2-shaft_flat_depth+shaft_clearance/2,-shaft_r-1])
            square([2*shaft_r+2,2*shaft_r+2]);
    }
}

module side_screw_hole() {
    rotate([0,0,side_screw_angle])
        translate([0,0,coupler_length-side_screw_top_offset])
            rotate([0,90,0])
                cylinder(d=side_screw_diameter,h=coupler_diameter/2+eps);
}

module servo_shaft_coupler() {
    params=servo_parameters();
    spline_depth=params[0][1];
    seat_bottom=spline_depth+smooth_socket_depth;
    seat_top=seat_bottom+screw_seat_thickness;
    shaft_bottom=coupler_length-shaft_insert_depth;

    assert(coupler_length>0 && coupler_diameter>0,"Invalid body dimensions");
    assert(shaft_insert_depth>0 && shaft_bottom>seat_top,"Shaft socket overlaps screw seat");
    assert(shaft_diameter>0 && shaft_diameter+shaft_clearance<coupler_diameter,"Shaft too large");
    assert(shaft_flat_depth>=0 && shaft_flat_depth<shaft_diameter/2,"Invalid flat");
    assert(screw_access_diameter<coupler_diameter,"Access too large");
    assert(screw_access_diameter>params[0][0]+2*servo_head_gap,"Access smaller than servo spline");
    assert(shaft_diameter+shaft_clearance>=screw_access_diameter,"Socket cannot pass servo screw");
    assert(screw_clearance_diameter<screw_access_diameter,"Invalid screw clearance");
    assert(!enable_side_screw || (side_screw_top_offset>0 &&
        side_screw_top_offset<shaft_insert_depth),"Side screw misses shaft");
    assert(smooth_socket_depth==0 ||
        (smooth_socket_diameter>params[0][0]+2*servo_head_gap &&
         smooth_socket_diameter<coupler_diameter),"Invalid smooth socket");

    difference() {
        cylinder(d=coupler_diameter,h=coupler_length);
        translate([0,0,-eps])
            linear_extrude(height=spline_depth+eps)
                servo_spline_2d(params,servo_head_gap);
        if (smooth_socket_depth>0)
            translate([0,0,spline_depth-eps])
                cylinder(d=smooth_socket_diameter,h=smooth_socket_depth+2*eps);
        translate([0,0,seat_bottom-eps])
            cylinder(d=screw_clearance_diameter,h=screw_seat_thickness+2*eps);
        translate([0,0,seat_top])
            cylinder(d=screw_access_diameter,h=shaft_bottom-seat_top+eps);
        translate([0,0,shaft_bottom-eps])
            linear_extrude(height=shaft_insert_depth+2*eps)
                shaft_profile_2d();
        if (enable_side_screw) side_screw_hole();
    }
}

servo_shaft_coupler();
