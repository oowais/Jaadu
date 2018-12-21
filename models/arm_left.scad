$fn=500;

scale([10, 10, 10]) {
    mirror([1, 0, 0]) {
        union() {
            difference() {
                cube([1.8, 2.7, 1.7]); // servo holding case 
                translate([0.2, 0.2, 0.2]) cube([1.61, 2.3, 1.3]); // servo holding
                translate([0.2, -0.1, 0.5]) cube([1.35, 0.31, 0.6]); // bringing out the servo wire
            }
         
            difference() {
                union() {
                    translate([0, 2.7, 0]) cube([1.8, 2, 0.85]); // the joint between circle and holder case
                    translate([0.9, 5.95, 0]) linear_extrude(height=0.85, $fn=300) circle(d=3.5); // the bigger circle
                }
                translate([0.9, 5.95, -0.1]) linear_extrude(height=1.2, $fn=300) circle(r=0.6); // The gear big circle
                translate([0.9, 5.35, -0.1]) linear_extrude(height=1.2, $fn=300) circle(r=0.3); // the gear small circle
                translate([0.6, 5.35, -0.1]) cube([0.6, 0.6, 1.2]); // To chip of a portion for the gear small circle
                translate([0.25, 4.2, 0.45]) cube([1.3, 2.4, 0.41]); // For the sitting of the gear box
            }
            
            translate([0, 0.8, 0.8]) sphere(0.15);
        }
    }
}