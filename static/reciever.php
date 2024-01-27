<?php
// get_x.php

if (isset($_GET['x'])) {
    // Retrieve the value of the "x" parameter
    $xValue = $_GET['x'];

    // Return the number 12
    echo "The value of x is: $xValue, and the result is 12";
} else {
    // If "x" parameter is not provided
    echo "Please provide a value for the 'x' parameter.";
}
?>