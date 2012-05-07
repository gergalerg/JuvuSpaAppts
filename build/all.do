# Set variables.
redo-ifchange env
source ./env

# Build CSS
redo-ifchange out/site.css

# Build JS
redo-ifchange out/site.js

redo-ifchange out/booking.js

cp -vf out/*.css ../juvume/static/css/ >&2
cp -vf out/*.js ../juvume/static/js/ >&2

