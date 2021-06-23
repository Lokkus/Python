#!/usr/bin/env bash
#declare bash string variable

bash_var="Bash script"

echo $bash_var
echo \$bash_var

# Single quotes in bash will suppress special meaning of every meta characters
function single_quotes
{
  echo $bash_var    # Bash script
  echo '$bash_var "$bash_var"' #$bash_var "$bash_var"
}

# Double quotes in bash will suppress special meaning of every meta characters except "$", "\" and "`".
function double_quotes
{
  echo "It's $bash_var and \"$bash_var\" using backticks: `date`"
}

single_quotes
double_quotes