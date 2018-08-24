# Just run each file though Closure Linter then JSLint.
gjslint $1 1>&2
rhino $rhinolint $1 1>&2
