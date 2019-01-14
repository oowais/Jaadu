include <globals.scad>

module raspi_case(x, y, z) {
    difference() {
        cube([x, y, z]);
        translate([(x-7) / 2, (y-3.5) / 2, 0.3]) cube([7, 3.5, z]);
        translate([(x-7) / 2 + 4.2, -0.1, 0.3]) cube([1.6, 3.5, 1]);
    }
}

$fn=300;
scale([10, 10, 10]) raspi_case(x=total_x, y=raspi_total_y, z=raspi_total_z);