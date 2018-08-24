# All we just run the CSS file through the Closure CSS compiler.
# Use this incantation to get non-compressed output CSS.
# P=--pretty-print
java -jar $clcss $P $2.gss
