$fn=100;

translate([0, 0, 1.6]) difference() {
    linear_extrude(0.3) circle(r=2.5);
    translate([0, 0, -0.01]) linear_extrude(0.32) circle(r=2);
}
for(i=[45: 45: 135]) {
        rotate([0, 0, -i]) translate([2.2, 0, 0]) scale([1, 12, 1]) cylinder(r=0.05, h=2);
    }