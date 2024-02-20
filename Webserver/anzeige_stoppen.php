<?php
echo "<h2>Anzeige wird gestoppt</h2>";

shell_exec("sudo systemctl stop anzeige_starten.service");

echo '<meta http-equiv="refresh" content="2; url=/">';
?>
