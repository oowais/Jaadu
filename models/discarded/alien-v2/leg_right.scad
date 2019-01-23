module leg_right() {
    difference() {
        hull() {
            translate([0, 0, 2.5]) cube([3.8, 2, 3]);
            translate([1.65, 0.75, 0]) cube([0.5, 0.5, 1]);
        }
        
        translate([0.2, -0.1, 2.9]) cube([3, 2.2, 2.7]);
        
        difference() {
            translate([3.19, -0.01, 4.5]) cube([0.62, 2.02, 1.01]);
            translate([3.19, 1, 4.5]) rotate([0, 90, 0]) linear_extrude(height=0.62, $fn=300) circle(r=1.01);
        }
        
        difference() {
            translate([-0.01, -0.01, 4.5]) cube([0.62, 2.02, 1.01]);
            translate([-0.01, 1, 4.5]) rotate([0, 90, 0]) linear_extrude(height=0.62, $fn=300) circle(r=1.01);
        }
        
        translate([3.1, 1, 4.6]) rotate([0, 90, 0]) cylinder(h=1, r=0.4);
        
        translate([3.1, 1, 3.15]) rotate([0, 90, 0]) cylinder(h=1, d=0.1);
        
        hull() {
            translate([3.4, 1, 4.6]) rotate([0, 90, 0]) cylinder(h=1, r=0.4);
            translate([3.4, 1, 3.1]) rotate([0, 90, 0]) cylinder(h=1, r=0.2);
        }
        
        translate([0.2, 1, 4.6]) sphere(0.2);
    }  
}

$fn=300;
scale([10, 10, 10]) leg_right();