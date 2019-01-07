use <arm_right.scad>

module arm_left() {
    mirror([1, 0, 0]) arm_right();
}

$fn=300;
scale([10, 10, 10]) arm_left();