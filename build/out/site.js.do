# Re-check all Javascript files.
JS_SOURCE=../src-static/js
redo-ifchange $JS_SOURCE/all

# Compile the JS into one file.

CLO_LIB=/home/sforman/Software/closure/closure-library-read-only
CLO_COMPILE="java -jar /home/sforman/Software/closure/closure-compiler/compiler.jar"
JS_EXTERNS=$JS_SOURCE/../js-externs/d3-externs.js

# 1. Collect all JS and dependencies using Google's closurebuilder script.
# (The @fileoverview markers triggers errors in the compile step when there's
# more than one in a file so we grep them out of the combined JS file here.)
t=$(tempfile)
echo "Writing to $t" >&2
closurebuilder \
  --root=$CLO_LIB/ \
  --root=$JS_SOURCE/ \
  --namespace="juvume" \
  --output_mode=script \
  | grep -v '@fileoverview' \
  > $t

# 2. Compile the final output JS file.
echo "Compiling site.js from $t" >&2
$CLO_COMPILE --js $t --externs $JS_EXTERNS --compilation_level=SIMPLE_OPTIMIZATIONS
rm -vf $t >&2

