module holder_for_battery() {
    // height = 4.5
    // width = 2.7
    // length = 1.8
    difference() {
        cube([2.7+0.2, 4.5+0.1, 1.8+0.2]);
        translate([0.1, -0.01, 0.1]) cube([2.7, 4.51, 1.8]);
    }
    translate([1.1, 1, 2]) difference() {
        cube([0.5+0.2, 4.6-1, 0.25+0.1]);
        translate([0.1, -0.1, -0.1]) cube([0.5, 7, 0.35]);
    }
    
}

$fn=300;
scale([10, 10, 10]) holder_for_battery();