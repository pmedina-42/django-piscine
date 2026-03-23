if [ $# -eq 1 ]
  then
    curl -s --head {$1} | grep Location | cut -d ' ' -f2
fi
