# Config generator
Generates config files from jinja2 templates. Uses yaml as data source.

## Usage
Template files in the templates folder.
Output in the out folder.

## Build
`docker build -t config-gen .`

## Example run
`docker run --volume $PWD:/app config-gen`

