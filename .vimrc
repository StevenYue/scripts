"read arduino .ino file as cpp file
autocmd BufNewFile,BufReadPost *.ino set filetype=cpp

set tabstop=4     " tabs are at proper location
set expandtab     " don't use actual tab character (ctrl-v)
set shiftwidth=4  " indenting is 4 spaces
set autoindent    " turns it on
set smartindent   " does the right thing (mostly) in programs
set cindent       " stricter rules for C programs

set showcmd             " Show (partial) command in status line.
set showmatch           " Show matching brackets.
set smartcase           " Do smart case matching
set incsearch           " Incremental search
set autowrite           " Automatically save before commands like :next and :make
set hidden              " Hide buffers when they are abandoned
set mouse=a             " Enable mouse usage (all modes) in terminals
set backspace=2         " make backspace work normal
set noerrorbells        " don't make noise
set novisualbell        " don't blink

set background=light
"highlight Normal ctermfg=grey ctermbg=black
colorscheme desert

set ai                  " autoindent
set si                  " smartindent 
set nowrap              " do not wrap lines  
set guifont=Liberation\ Mono\ 20        " do not wrap lines  
set guioptions+=l       " don't move screen around 
set softtabstop=4       " unify
set noic                " case sensitive search set ic for insensitive

" ============vim diff options============
set diffopt+=iwhite     " ignore whitespace when diffing


set autochdir           " set working direction to current file

set ignorecase          " case insensitive
set incsearch           " show next word while entering search text

"set clipboard=unnamed
"set number
