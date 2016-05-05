<?php

$tag = $argv[1];
$shaSum = $argv[2];
$currentTime = $argv[3];
$resultsFile = $argv[4];
$statsFile = $argv[5];

$response = [];
$response['measurement'] = json_decode(file_get_contents($statsFile), true);
$response['measurement']['performance'] = [];
$fh = fopen($resultsFile, 'r');
while (($line = fgets($fh)) !== false) {
    $parts = explode(',', $line);
    $type = trim($parts[0], '"');
    $cardinality = trim($parts[1], '"');
    $unit = $parts[2] === '"WalltimeMilliseconds"' ? 'ms' : 'unknown';
    if($type === 'propfind') {
        $type .= '-' . $cardinality;
        $cardinality = 1;
    }
    $cardinality = str_replace(['k', 'M'], ['000', '000000'], $cardinality);
    $response['measurement']['performance'][] = [
        'type' => $type,
        'unit' => $unit,
        'cardinality' => intval($cardinality),
        'repeats' => intval(trim($parts[5])),
        'value' => intval($parts[4]),
    ];
}
fclose($fh);
/* get mysql version */
preg_match('@[0-9]+\.[0-9]+\.[0-9]+@', shell_exec('mysql -V'), $version);
$mysqlVersion = $version[0];
$response['environment'] = [
    'git.tag' => $tag,
    'time' => $currentTime,
    'php' => phpversion(),
    'mysql' => $mysqlVersion,
    'opcache' => ini_get('opcache.enable') === '1' ? '1' : '0'
];
echo json_encode($response, JSON_PRETTY_PRINT);
echo PHP_EOL;

?>
