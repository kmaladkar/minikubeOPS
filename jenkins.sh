set -ex

addLinterPlugins(){
    pip install pep8-naming==0.*
}

runLinter(){
    flake9 . --count --statistics
}

lint(){
    addLinterPlugins
    runLinter
}