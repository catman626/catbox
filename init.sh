#!/usr/bin/env bash

vim_rc="$HOME/.vimrc"
plug_file="$HOME/.vim/autoload/plug.vim"

# 安装 vimrc
if [[ ! -f "$vim_rc" ]]; then
    cp "$HOME/catbox/share/.vimrc" "$vim_rc"
fi

# 安装 vim-plug
if [[ ! -f "$plug_file" ]]; then
    echo "正在安装 vim-plug..."

    curl -fLo "$plug_file" \
        --create-dirs \
        https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
fi

# 安装 vimrc 中声明的插件
vim +'PlugInstall --sync' +qa

# 设置全局 Git 拉取策略
git config --global pull.rebase false


