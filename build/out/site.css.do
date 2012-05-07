# Prepare and gather all CSS files into 'site.css'.
CSS_SOURCE=../src-static/css
redo-ifchange $CSS_SOURCE/all

# This CSS file is just for one page.
mv -vf $CSS_SOURCE/splash.css . >&2

# Collect the rest of the CSS into one pile.
t=$(tempfile)
cat $CSS_SOURCE/*.css > $t

# Re-compile the whole thing to get any further bytes
# (This is probably pointless, but also probably harmless.)
java -jar $clcss $P $t
