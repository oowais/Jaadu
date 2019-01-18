use <battery_holder.scad>
use <bluetooth_holder.scad>
use <side_part.scad>
use <button_holder.scad>

module powerhand() {
    translate([0, 0, 1-0.6]) button_holder();
    translate([0.5, 0, 0]) holder_for_battery();
    translate([2.8, 0, 0]) holder_for_bluetooth();
    translate([1.95, 4.6, 0]) connector();
}

$fn=300;
powerhand();