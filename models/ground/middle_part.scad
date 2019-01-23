module middle_part() {
    difference() {
        linear_extrude(0.2) circle(r=7);
        translate([-15/2, -7, -0.5]) cube([15, 7, 1]);
        rotate([0, 0, -70]) translate([-15/2, -7, -0.5]) cube([15, 7, 1]);
        translate([1.1, -0.1, -0.1]) cube([0.4, 2.4, 1]);
        translate([1, -0.1, -0.1]) cube([0.8, 0.6, 1]);
        difference() {
            sphere(r=6.5);
            sphere(r=6.5-0.4);
            rotate([0, 0, 10]) translate([-7, 0, -0.5]) cube([7, 7, 2]);
            rotate([0, 0, 370-180]) translate([-7, 0, -0.5]) cube([7, 7, 2]);
        }
        difference() {
            sphere(r=5.5);
            sphere(r=5.5-0.4);
            rotate([0, 0, -30]) translate([-2, 0, -0.5]) cube([4, 7, 2]);
        }
        difference() {
            sphere(r=4.5);
            sphere(r=4.5-0.4);
            rotate([0, 0, 10]) translate([-7, 0, -0.5]) cube([7, 7, 2]);
            rotate([0, 0, 370-180]) translate([-7, 0, -0.5]) cube([7, 7, 2]);
        }
    }
}

$fn=300;
scale([10, 10, 10]) middle_part();