# Pick up JSLint's location once here.
redo-ifchange ../../env
. ../../env

# Recheck all source JS files.
ls *.js | xargs redo-ifchange
