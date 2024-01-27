<?php
// receiver.php

if (isset($_POST['data'])) {
    $receivedData = $_POST['data'];
    // Process the data as needed
    echo "Received data: $receivedData";
} else {
    echo "No data received.";
}
?>
