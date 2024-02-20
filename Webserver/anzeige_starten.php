<?php
echo "<h2>Anzeige wird verbunden</h2>";

shell_exec("sudo systemctl stop anzeige_starten.service");
shell_exec("sudo systemctl start anzeige_starten.service");

echo '<meta http-equiv="refresh" content="2; url=/">';
?>
