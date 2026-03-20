vim_rc = ~/.vimrc
if [[ ! -f "$vim_rc"]]
then
    cp ~/catbox/share/.vimrc $vim_rc
fi

git config pull.rebase false


