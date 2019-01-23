use <leg_right.scad>

module leg_left() {
    mirror([1, 0, 0]) leg_right();
}

$fn=300;
scale([10, 10, 10]) leg_left();