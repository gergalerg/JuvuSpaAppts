# Set variables.
redo-ifchange env
source ./env

# Build CSS
redo-ifchange out/site.css
cp -vf out/site.css ../juvume/static/css/site.css >&2

# Build JS
redo-ifchange out/site.js
cp -vf out/site.js ../juvume/static/js/site.js >&2

