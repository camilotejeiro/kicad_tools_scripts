#!/bin/bash

# Absolute path to this script. /home/user/bin/foo.sh
##SCRIPT=$(readlink -f $0)
# Absolute path this script is in. /home/user/bin
##SCRIPTPATH=`dirname $SCRIPT`
##echo $SCRIPTPATH
##cd $SCRIPTPATH

#!/bin/bash

#realpath() {
#    [[ $1 = /* ]] && echo "$1" || echo "$PWD/${1#./}"
#}

#realpath "$0"

pushd `dirname $0` > /dev/null
SCRIPTPATH=`pwd -P`
popd > /dev/null

cd $SCRIPTPATH

echo  $SCRIPTPATH

kicad demo.pro
