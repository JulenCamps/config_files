"Plugins
call plug#begin()
Plug 'morhetz/gruvbox'
call plug#end()

"Numerate lines
set number

"Color scheme
colorscheme gruvbox

"Shortcuts
vnoremap <C-c> "+y
map <C-v> "+P

"Background transparency as in the terminal
autocmd VimEnter * hi Normal ctermbg=none
