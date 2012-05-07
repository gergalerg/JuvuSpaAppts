# Compile all the GSS files in this directory to CSS.

# Pick up the CSS compiler's location once here.
redo-ifchange ../../env
. ../../env

# Use default.css.do to rebuild any modified GSS files.
for fn in *.gss; do
    echo ${fn%.gss}.css
done |
xargs redo-ifchange
