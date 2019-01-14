include <globals.scad>

module base(x, y, z) {
    difference() {
        union() {
            cube([x, y, b_overall_z]);
            cube([x, b_legspace, b_legfit_z]);
            translate([b_legspace, 0, b_legfit_z]) cube([x-(b_legspace*2), b_legspace, z-b_legfit_z]);
        }
        translate([(l_arms_base_d/2), (l_arms_base_d/2), -0.01]) linear_extrude(height=1, $fn=300) circle(r=0.4);
        hull() {
            translate([(l_arms_base_d/2), (l_arms_base_d/2), -0.01]) linear_extrude(height=0.31, $fn=300) circle(r=0.4);
            translate([(l_arms_base_d/2), (l_arms_base_d/2)+1.5, -0.01]) linear_extrude(height=0.31, $fn=300) circle(r=0.2);
        } 
        
        translate([x-(l_arms_base_d/2), (l_arms_base_d/2), -0.01]) linear_extrude(height=1, $fn=300) circle(r=0.4); 
        hull() {
            translate([x-(l_arms_base_d/2), (l_arms_base_d/2), -0.01]) linear_extrude(height=0.31, $fn=300) circle(r=0.4);
            translate([x-(l_arms_base_d/2), (l_arms_base_d/2)+1.5, -0.01]) linear_extrude(height=0.31, $fn=300) circle(r=0.2);
        } 
        
        translate([x/2, base_head_fit_1, z-screw_h]) cylinder(r=screw_r, h=3);
        translate([x/2, base_head_fit_2, z-screw_h]) cylinder(r=screw_r, h=3);
    }
}

$fn=300;
scale([10, 10, 10]) base(x=total_x, y=total_y, z=base_total_z);