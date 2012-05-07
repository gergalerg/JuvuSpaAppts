# Set variables.
redo-ifchange env
source ./env

# Build CSS
redo-ifchange out/site.css
cp -vf out/site.css ../juvume/static/css/site.css >&2

# Build JS
redo-ifchange out/site.js

redo-ifchange out/booking.js
cp -vf out/*.js ../juvume/static/js/ >&2

