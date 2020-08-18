<?php
    $directorio = "converted_files/";        #carpeta con archivos
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mis archivos</title>
</head>
<body>
    <h1>Archivos convertidos</h1>
    <div class="section">
        <h2>Tus archivos subidos </h2>
    </div>

    <div class="caja">
        <?php
            $dir = opendir($directorio)
                while ($archivo = readdir($dir)){
                    if ($archivo != '.' && $archivo != '..'){           #muestro los archivos mas el contador
                        $contador++;
                        echo  "Nombre: <strong> $archivo </strong>";
                    }
                }
                echo "total de archivos: <strong> $contador </strong></br>";
            
            closedir($dir);
        ?>
    </div>
</body>
</html>