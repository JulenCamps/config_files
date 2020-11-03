# Defined in - @ line 1
function cat --wraps=/usr/bin/bat --description 'alias cat=/usr/bin/bat'
  /usr/bin/bat  $argv;
end
